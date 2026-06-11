import os
import sys
import glob
import re
from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse, FileResponse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from src.orbital.orbits import PropagadorOrbital

app = FastAPI(title="APEX-1 Backend")

# 1. Advanced Agent: Header-based Chunking & TF-IDF
kb_chunks = []
kb_display = []
kb_metadata = []

def load_knowledge_base():
    global kb_chunks, kb_display, kb_metadata
    # main.py is in src/backend/, so project root is 2 levels up
    docs_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'docs')
    md_files = glob.glob(os.path.join(docs_dir, '*.md'))
    
    header_regex = re.compile(r'^(#{1,4})\s+(.*)$')
    
    for file_path in md_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
            current_header = os.path.basename(file_path).replace('.md', '').replace('_', ' ')
            current_chunk = []
            
            for line in lines:
                match = header_regex.match(line)
                if match:
                    # Save the previous chunk if it has content
                    text = "".join(current_chunk).strip()
                    if len(text) > 20:
                        # Indexing content: Header heavily weighted + body
                        index_text = f"{current_header} {current_header} {current_header} {text}"
                        kb_chunks.append(index_text)
                        kb_display.append(f"### {current_header}\n\n{text}")
                        kb_metadata.append(os.path.basename(file_path))
                        
                    current_header = match.group(2).strip()
                    current_chunk = []
                else:
                    current_chunk.append(line)
            
            # Save the last chunk
            text = "".join(current_chunk).strip()
            if len(text) > 20:
                index_text = f"{current_header} {current_header} {current_header} {text}"
                kb_chunks.append(index_text)
                kb_display.append(f"### {current_header}\n\n{text}")
                kb_metadata.append(os.path.basename(file_path))

load_knowledge_base()

# We include Spanish and English stop words conceptually, or just build a basic vectorizer
vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
if kb_chunks:
    tfidf_matrix = vectorizer.fit_transform(kb_chunks)

class ChatQuery(BaseModel):
    message: str

@app.post("/api/chat")
async def chat_endpoint(query: ChatQuery):
    if not kb_chunks:
        return {"response": "Error: Knowledge base empty.", "doc": ""}
        
    # Standardize query
    q = query.message.lower()
    query_vec = vectorizer.transform([q])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    
    best_idx = np.argmax(similarities)
    best_score = similarities[best_idx]
    
    if best_score < 0.05:
        return {"response": "I couldn't find a highly confident match for that in my orbital database. Could you rephrase or ask about Keplerian elements, J2, GNSS, or Hohmann transfers?", "doc": ""}
        
    return {
        "response": kb_display[best_idx],
        "doc": kb_metadata[best_idx]
    }

# 2. Orbital Physics API
class OrbitalElements(BaseModel):
    a: float
    e: float
    i: float
    raan: float
    argp: float
    nu0: float

@app.post("/api/orbit/propagate")
async def propagate_orbit(elements: OrbitalElements):
    try:
        propagator = PropagadorOrbital(
            a=elements.a, 
            e=elements.e, 
            i=elements.i, 
            raan=elements.raan, 
            argp=elements.argp, 
            nu0=elements.nu0
        )
        T = propagator.period()
        x, y, z = propagator.propagate(T, num_points=200)

        points = [{"x": float(x[i]), "y": float(y[i]), "z": float(z[i])} for i in range(len(x))]
        return {"points": points, "period_s": T}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})

# Serve the frontend statically
frontend_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'frontend')

@app.get("/")
async def read_index():
    return FileResponse(os.path.join(frontend_path, 'index.html'))

app.mount("/", StaticFiles(directory=frontend_path), name="frontend")
