from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="APEX-1 Backend API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    language: Optional[str] = "en"

class ChatResponse(BaseModel):
    response: str

KNOWLEDGE_BASE = {
    "en": {
        "hohmann": "A Hohmann Transfer Orbit is an elliptical orbit used to transfer between two circular orbits of different radii in the same plane. It is the most fuel-efficient maneuver.",
        "kepler": "Kepler's Laws:\n1. Orbits are ellipses with the planet at one focus.\n2. A line segment sweeps out equal areas during equal intervals of time.\n3. The square of the orbital period is proportional to the cube of the semi-major axis.",
        "gps": "GPS satellites operate in Medium Earth Orbit (MEO) at an altitude of approximately 20,200 km, with a period of 12 hours.",
        "vis-viva": "The Vis-Viva equation is: v^2 = GM * (2/r - 1/a). It calculates the velocity of a body in an elliptical orbit.",
        "orbit": "An orbit is a regular, repeating path that one object in space takes around another one.",
        "jupyter": "To run JupyterLab locally for the APEX-1 console, launch it from the project root:\n\n```bash\njupyter lab --no-browser\n```\n\nJupyter prints a tokenized URL in the terminal — open that link, and the APEX-1 console will detect the kernel automatically. For a friction-free local dev session you can also use the provided `scripts/start.ps1`.",
        "password": "JupyterLab shows a token prompt to keep your local kernel private — that is expected and correct. Copy the tokenized URL Jupyter prints in the terminal when you start it with `jupyter lab`, or use `scripts/start.ps1` which wires up a local-only dev session for you.",
        "hello": "Hello Commander! I am the APEX-1 Tactical Space Agent. How can I assist your orbital operations today?",
        "hi": "Hello Commander! I am the APEX-1 Tactical Space Agent. How can I assist your orbital operations today?",
        "who are you": "I am APEX-1, an advanced multi-agent system designed by Lattice Startup to handle orbital dynamics, telemetry, and spatial analysis.",
        "thank": "You are welcome, Commander. Awaiting further telemetry.",
        "fallback": "Query recorded. My current context is limited to basic orbital dynamics. For full intelligence, please connect me to a global LLM like Gemini Flash 1.5 or Ollama."
    },
    "es": {
        "hohmann": "Una órbita de transferencia de Hohmann es una trayectoria elíptica usada para transferirse entre dos órbitas circulares. Es la maniobra más eficiente en combustible.",
        "kepler": "Leyes de Kepler:\n1. Las órbitas son elipses con el planeta en un foco.\n2. La línea que une al planeta y el sol barre áreas iguales en tiempos iguales.\n3. El cuadrado del período orbital es proporcional al cubo del semieje mayor.",
        "gps": "Los satélites GPS operan en Órbita Terrestre Media (MEO) a una altitud de aproximadamente 20,200 km, con un período de 12 horas.",
        "vis-viva": "La ecuación Vis-Viva es: v^2 = GM * (2/r - 1/a). Calcula la velocidad de un cuerpo en una órbita elíptica.",
        "orbita": "Una órbita es la trayectoria regular y repetitiva que un objeto en el espacio sigue alrededor de otro.",
        "jupyter": "Para ejecutar JupyterLab en local con la consola APEX-1, inícialo desde la raíz del proyecto:\n\n```bash\njupyter lab --no-browser\n```\n\nJupyter imprime una URL con token en la terminal — abre ese enlace y la consola APEX-1 detectará el kernel automáticamente. Para una sesión de desarrollo local sin fricción también puedes usar el script `scripts/start.ps1`.",
        "contraseña": "JupyterLab muestra un token para mantener privado tu kernel local — eso es esperado y correcto. Copia la URL con token que Jupyter imprime en la terminal al arrancar con `jupyter lab`, o usa `scripts/start.ps1`, que prepara una sesión de desarrollo solo-local por ti.",
        "hola": "¡Hola Comandante! Soy el agente táctico espacial APEX-1. ¿En qué puedo asistir tus operaciones orbitales hoy?",
        "quien eres": "Soy APEX-1, un avanzado sistema multi-agente diseñado por Lattice Startup para manejar dinámicas orbitales, telemetría y análisis espacial.",
        "gracias": "De nada, Comandante. Esperando nueva telemetría.",
        "fallback": "Consulta registrada. Mi contexto actual está limitado a dinámicas orbitales básicas. Para inteligencia completa, por favor conéctame a un modelo gratuito de LLM como Gemini Flash 1.5 u Ollama local."
    },
    "zh": {
        "hohmann": "霍曼转移轨道是一种用于在同一平面内不同半径的两个圆形轨道之间转移的椭圆轨道。它是最节省燃料的机动。",
        "kepler": "开普勒定律：\n1. 轨道是椭圆，行星位于一个焦点上。\n2. 连接行星和太阳的线段在相等的时间间隔内扫过相等的面积。\n3. 轨道周期的平方与半长轴的立方成正比。",
        "gps": "GPS卫星在距离地面约20,200公里的中地球轨道(MEO)运行，周期为12小时。",
        "vis-viva": "活力公式为：v^2 = GM * (2/r - 1/a)。它计算椭圆轨道上物体的速度。",
        "轨道": "轨道是太空中一个物体围绕另一个物体运行的有规律的重复路径。",
        "jupyter": "要在本地为 APEX-1 控制台运行 JupyterLab，请在项目根目录启动：\n\n```bash\njupyter lab --no-browser\n```\n\nJupyter 会在终端打印带令牌的 URL —— 打开该链接，APEX-1 控制台会自动检测内核。若想要顺畅的本地开发会话，也可以使用提供的 `scripts/start.ps1`。",
        "密码": "JupyterLab 显示令牌提示是为了保护你的本地内核，这是预期且正确的行为。复制 Jupyter 启动时在终端打印的带令牌 URL，或使用 `scripts/start.ps1`，它会为你配置仅限本地的开发会话。",
        "你好": "你好，指挥官！我是 APEX-1 战术太空智能体。今天我能为您的轨道任务提供什么帮助？",
        "你是谁": "我是 APEX-1，由 Lattice Startup 设计的高级多智能体系统，负责处理轨道动力学、遥测和空间分析。",
        "谢谢": "不客气，指挥官。等待进一步的遥测数据。",
        "fallback": "已记录查询。我当前的上下文仅限于基本轨道动力学。如需完整情报，请将我连接到免费的 LLM 模型，例如 Gemini Flash 1.5 或本地 Ollama。"
    }
}

@app.get("/")
def read_root():
    return {"status": "APEX-1 Backend is running", "version": "2.0.0"}

@app.post("/api/chat", response_model=ChatResponse)
def agent_chat(req: ChatRequest):
    msg = req.message.lower()
    lang = req.language if req.language in KNOWLEDGE_BASE else "en"
    db = KNOWLEDGE_BASE[lang]
    
    # Check for exact or partial keyword matches
    for keyword, answer in db.items():
        if keyword != "fallback" and keyword in msg:
            return ChatResponse(response=answer)
            
    # Also check English database as fallback for technical terms if using other languages
    if lang != "en":
        for keyword, answer in KNOWLEDGE_BASE["en"].items():
            if keyword not in ["hello", "hi", "who are you", "thank", "fallback"] and keyword in msg:
                return ChatResponse(response=db.get("fallback", "Fallback") + f" [Data retrieved in EN: {answer}]")
    
    return ChatResponse(response=db["fallback"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
