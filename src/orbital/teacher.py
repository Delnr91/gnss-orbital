"""Interactive Second Brain and Teacher Companion for Space Astrodynamics.

Implements a deterministic anti-troll filter and provides a Jupyter widget-based
interface to navigate interlinked markdown documents like an Obsidian vault.
"""

from __future__ import annotations

import os
import re
from typing import Dict, List, Tuple, Optional
import ipywidgets as widgets
from IPython.display import display, Markdown

# List of keywords allowed in the anti-troll space filter
SPACE_KEYWORDS = {
    "en": [
        "orbit", "space", "satellite", "kepler", "gnss", "gps", "galileo", "beidou", 
        "glonass", "iris2", "drag", "j2", "radiation", "propagate", "trajectory", 
        "hohmann", "apogee", "perigee", "eccentricity", "inclination", "raan", 
        "anomaly", "time", "clock", "precision", "relativity", "mass", "gravity", 
        "transfer", "constellation", "earth", "physics", "numerical", "solver"
    ],
    "es": [
        "orbita", "espacio", "satelite", "kepler", "gnss", "gps", "galileo", "beidou", 
        "glonass", "iris2", "arrastre", "radiacion", "propagar", "trayectoria", 
        "hohmann", "apogeo", "perigeo", "excentricidad", "inclinacion", "raan", 
        "anomalia", "tiempo", "reloj", "precision", "relatividad", "masa", "gravedad", 
        "transferencia", "constelacion", "tierra", "fisica", "numerico", "solucionador"
    ],
    "zh": [
        "轨道", "空间", "太空", "卫星", "开普勒", "星座", "重力", "引力", "速度", 
        "高度", "偏心率", "倾角", "升交点", "近地点", "远地点", "时间", "时钟", 
        "精度", "相对论", "霍曼", "转移", "地球", "物理", "求解器"
    ]
}


class SpaceTeacher:
    """Deterministic knowledge registry and navigator for orbital mechanics.

    Filters queries to ensure they are on-topic, parses wiki-links, and displays
    markdown context documents like an Obsidian vault.
    """

    def __init__(self, docs_dir: Optional[str] = None) -> None:
        if docs_dir is None:
            self.docs_dir = os.path.join(
                os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "docs"
            )
        else:
            self.docs_dir = docs_dir
            
        self.documents: Dict[str, str] = {}
        self._load_documents()

    def _load_documents(self) -> None:
        """Loads all markdown files in the docs/ directory."""
        if not os.path.exists(self.docs_dir):
            return

        # Load main README as a document too
        readme_path = os.path.join(os.path.dirname(self.docs_dir), "README.md")
        if os.path.exists(readme_path):
            try:
                with open(readme_path, "r", encoding="utf-8") as f:
                    self.documents["readme.md"] = f.read()
            except OSError:
                pass

        for root, _, files in os.walk(self.docs_dir):
            for file in files:
                if file.endswith(".md"):
                    rel_path = os.path.relpath(os.path.join(root, file), self.docs_dir)
                    doc_key = rel_path.replace("\\", "/").lower()
                    try:
                        with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                            self.documents[doc_key] = f.read()
                    except OSError:
                        pass

    def check_on_topic(self, query: str) -> bool:
        """Determines if a query is related to space/orbital dynamics (anti-troll filter)."""
        clean_query = query.lower()
        
        # Check against all language keywords
        for lang, words in SPACE_KEYWORDS.items():
            for word in words:
                if word in clean_query:
                    return True
        return False

    def query_knowledge(self, query: str, lang: str = "en") -> str:
        """Answers queries using localized text search or rejects if off-topic."""
        if not self.check_on_topic(query):
            if lang == "es":
                return "Solo proceso temas relacionados a Dinámica Orbital, Sistemas GNSS, Precisión Espacial, e Infraestructura Espacial al 2030."
            elif lang == "zh":
                return "我仅处理与轨道动力学、GNSS系统、空间精度以及2030年空间基础设施相关的课题。"
            else:
                return "I only process topics related to Orbital Dynamics, GNSS Systems, Space Precision, and Space Infrastructure to 2030."

        # Search documents for best matches
        search_terms = re.findall(r"\w+", query.lower())
        best_doc = None
        best_score = 0

        for key, content in self.documents.items():
            score = 0
            for term in search_terms:
                if term in key or term in content.lower():
                    # Weigh matches in title/keys higher
                    score += 5 if term in key else 1
            if score > best_score:
                best_score = score
                best_doc = key

        if best_doc:
            # Replace wiki-style links [[docs/filename.md]] with clickable labels for visual representation
            content = self.documents[best_doc]
            return f"### Document: {best_doc.upper()}\n\n---\n\n{content}"

        if lang == "es":
            return "No encontré documentos que coincidan con los términos de búsqueda. Intente con palabras clave como: Kepler, GNSS, J2, o IRIS2."
        elif lang == "zh":
            return "未找到匹配的文档。请尝试使用其他关键词，例如：开普勒、GNSS、J2 或 IRIS2。"
        else:
            return "No matching documents found. Try terms like Kepler, GNSS, J2, or IRIS2."

    def get_document_names(self) -> List[str]:
        return sorted(list(self.documents.keys()))

    def get_document(self, name: str) -> str:
        return self.documents.get(name.lower(), "Document not found.")


def create_teacher_workspace() -> widgets.VBox:
    """Generates a complete Jupyter Widget UI for the Space Teacher workspace."""
    teacher = SpaceTeacher()
    
    # Widgets
    lang_select = widgets.Dropdown(
        options=[("English", "en"), ("Español", "es"), ("简体中文", "zh")],
        value="en",
        description="Language:"
    )
    
    search_input = widgets.Text(
        value="",
        placeholder="Enter space/orbital keywords...",
        description="Search Vault:",
        layout=widgets.Layout(width="450px")
    )
    
    doc_select = widgets.Dropdown(
        options=["Select document..."] + teacher.get_document_names(),
        value="Select document...",
        description="Browse Vault:"
    )
    
    search_btn = widgets.Button(
        description="Query Teacher",
        button_style="primary"
    )
    
    output = widgets.Output()

    def render_markdown(text: str) -> None:
        with output:
            output.clear_output()
            # Convert wiki-style [[path/file.md]] to standard markdown links or markers
            # For this UI, we can just replace [[filename]] with bold identifiers
            processed_text = re.sub(r"\[\[(.*?)\]\]", r"**\1**", text)
            display(Markdown(processed_text))

    def on_search(b):
        query = search_input.value.strip()
        if not query:
            return
        res = teacher.query_knowledge(query, lang_select.value)
        render_markdown(res)

    def on_doc_select(change):
        val = change["new"]
        if val == "Select document...":
            return
        doc_content = teacher.get_document(val)
        render_markdown(f"### Document: {val.upper()}\n\n---\n\n{doc_content}")

    search_btn.on_click(on_search)
    doc_select.observe(on_doc_select, names="value")

    # Layout
    title = widgets.HTML(
        value="<h2 style='color:#4a9eff; font-family:Inter, sans-serif; margin-bottom:5px;'>🎓 MIT-Stanford Space Systems Second Brain</h2>"
              "<p style='color:#aaa; font-family:Inter, sans-serif; margin-top:0;'>Search or browse our localized astrodynamics knowledge vault. Anti-troll filter active.</p>"
    )
    
    controls = widgets.HBox([lang_select, search_input, search_btn])
    browser = widgets.HBox([doc_select])
    
    layout = widgets.VBox([
        title,
        widgets.HTML("<hr style='border-color:#333;'>"),
        controls,
        browser,
        widgets.HTML("<hr style='border-color:#333;'>"),
        output
    ])
    
    # Initialize with default help text
    with output:
        display(Markdown("Welcome to the Training Workspace. Enter an orbital query above or select a document from the dropdown to begin studying."))
        
    return layout
