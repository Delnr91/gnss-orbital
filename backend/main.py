from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="APEX-1 Backend API")

# Setup CORS to allow Vercel and localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for demo purposes. Replace with Vercel URL in prod.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

# Simple knowledge base for the agent (Moved from JS)
KNOWLEDGE_BASE = {
    "hohmann": "A Hohmann Transfer Orbit is an elliptical orbit used to transfer between two circular orbits of different radii in the same plane. It is the most fuel-efficient maneuver.",
    "kepler": "Kepler's Laws:\n1. Orbits are ellipses with the planet at one focus.\n2. A line segment joining a planet and the Sun sweeps out equal areas during equal intervals of time.\n3. The square of the orbital period is proportional to the cube of the semi-major axis.",
    "gps": "GPS satellites operate in Medium Earth Orbit (MEO) at an altitude of approximately 20,200 km, with a period of 12 hours.",
    "vis-viva": "The Vis-Viva equation is: v^2 = GM * (2/r - 1/a). It calculates the velocity of a body in an elliptical orbit at a given distance 'r'."
}

@app.get("/")
def read_root():
    return {"status": "APEX-1 Backend is running", "version": "1.0.0"}

@app.post("/api/chat", response_model=ChatResponse)
def agent_chat(req: ChatRequest):
    msg = req.message.lower()
    
    # Search knowledge base
    for keyword, answer in KNOWLEDGE_BASE.items():
        if keyword in msg:
            return ChatResponse(response=f"According to my knowledge base: {answer}")
    
    return ChatResponse(response="Query recorded. No exact match found in the tactical database. Try asking about Hohmann, Kepler, GPS, or the Vis-Viva equation.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
