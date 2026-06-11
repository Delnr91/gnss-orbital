import os

ROOT = r'c:\Users\invde\OneDrive\Documents\gnss-orbital-py\frontend'
index_file = os.path.join(ROOT, 'index.html')
app_file = os.path.join(ROOT, 'js', 'app.js')
css_file = os.path.join(ROOT, 'css', 'style.css')

# 1. Update index.html
with open(index_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Inject Constellation button properly
const_btn = '<button id="btn-constellation" class="btn-preset glow-green" style="width: 100%; margin-top: 10px;" data-i18n="ctrl.constellation">⚡ MULTI-ORBIT VIEW</button>'
if 'id="btn-constellation"' not in html:
    html = html.replace('id="preset-heo">HEO (Molniya)</button>', f'id="preset-heo">HEO (Molniya)</button>\n                            {const_btn}')

# Hide the static jarvis-avatar in HTML, because the organism will be the whole background
html = html.replace('<div class="agent-avatar-container">', '<div class="agent-avatar-container" style="display:none;">')

with open(index_file, 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Update style.css
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace hard variables with Glassmorphism variables
css = css.replace('--bg-surface: rgba(12, 12, 12, 0.85);', '--bg-surface: rgba(25, 25, 35, 0.25);')
css = css.replace('border-radius: 8px;', 'border-radius: 18px;')
css = css.replace('border-radius: 12px;', 'border-radius: 24px;')
css = css.replace('border-radius: 0;', 'border-radius: 18px;')

# Add strong blur to glass elements
css = css.replace('backdrop-filter: blur(25px);', 'backdrop-filter: blur(40px) saturate(180%); -webkit-backdrop-filter: blur(40px) saturate(180%); border: 1px solid rgba(255,255,255,0.1);')

# Organism Background Injection
organism_css = '''
/* --- THE LIVING DIGITAL ORGANISM --- */
.chat-agent-layout {
    position: relative;
    border-radius: 24px;
    overflow: hidden;
}

/* The liquid entity */
.jarvis-core {
    position: absolute !important;
    top: -50% !important;
    left: -50% !important;
    width: 200% !important;
    height: 200% !important;
    margin: 0 !important;
    z-index: 0 !important;
    background: radial-gradient(circle at center, rgba(0,255,200,0.15) 0%, rgba(0,168,255,0.05) 40%, transparent 70%);
    filter: blur(40px) contrast(1.5);
    animation: breatheOrganism 12s ease-in-out infinite alternate;
    pointer-events: none;
}

.jarvis-core::before {
    content: '';
    position: absolute;
    top: 25%; left: 25%;
    width: 50%; height: 50%;
    background: linear-gradient(45deg, rgba(0,255,200,0.3), rgba(0,168,255,0.1));
    border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%;
    animation: liquidMorphOrganism 15s ease-in-out infinite, pulseHeartbeat 4s infinite;
    mix-blend-mode: screen;
}

@keyframes breatheOrganism {
    0% { transform: scale(0.9) rotate(0deg); opacity: 0.8; }
    100% { transform: scale(1.1) rotate(5deg); opacity: 1; }
}

@keyframes liquidMorphOrganism {
    0%, 100% { border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%; transform: rotate(0deg); }
    34% { border-radius: 70% 30% 50% 50% / 30% 30% 70% 70%; transform: rotate(120deg); }
    67% { border-radius: 100% 60% 60% 100% / 100% 100% 60% 60%; transform: rotate(240deg); }
}

@keyframes pulseHeartbeat {
    0%, 100% { opacity: 0.6; transform: scale(1); }
    50% { opacity: 0.9; transform: scale(1.05); }
}

/* Glassmorphism Chat adjustments */
.jarvis-chat {
    background: rgba(10, 10, 15, 0.4);
    backdrop-filter: blur(30px) saturate(150%);
    -webkit-backdrop-filter: blur(30px) saturate(150%);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 24px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.5);
    z-index: 1;
}

.jarvis-chat .chat-history {
    background: transparent !important;
    border: none;
    border-radius: 24px 24px 0 0;
}

.jarvis-chat .chat-input-bar {
    background: rgba(0,0,0,0.3) !important;
    border: none;
    border-top: 1px solid rgba(255,255,255,0.1);
    border-radius: 0 0 24px 24px;
}

.chat-bubble.bot {
    background: rgba(0, 255, 200, 0.1);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(0, 255, 200, 0.2);
    border-radius: 4px 18px 18px 18px;
}

.chat-bubble.user {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 18px 4px 18px 18px;
}
'''
with open(css_file, 'a', encoding='utf-8') as f:
    f.write(organism_css)


# 3. Update app.js (Translations and Video toggle)
with open(app_file, 'r', encoding='utf-8') as f:
    app_js = f.read()

# Add ES, EN, ZH translations
translations_code = '''
const translations = {
    en: {
        "nav.overview": "Overview",
        "nav.simulator": "3D Simulator",
        "nav.brain": "Space Agent",
        "nav.jupyter": "Jupyter Lab",
        "ctrl.presets": "Orbit Presets",
        "preset.custom": "Custom",
        "preset.leo": "LEO (ISS)",
        "preset.meo": "MEO (GPS)",
        "preset.geo": "GEO",
        "preset.heo": "HEO (Molniya)",
        "ctrl.constellation": "⚡ MULTI-ORBIT VIEW",
        "ctrl.elements": "Classical Elements",
        "element.a": "Semi-major axis (a)",
        "element.e": "Eccentricity (e)",
        "element.i": "Inclination (i)",
        "element.argp": "Arg. of Periapsis (ω)",
        "metric.period": "Orbital Period",
        "metric.perigee": "Perigee Altitude",
        "metric.apogee": "Apogee Altitude",
        "brain.agent_title": "APEX-1 Space Agent",
        "brain.agent_subtitle": "ONLINE | KNOWLEDGE BASE SYNCED",
        "brain.send": "Send"
    },
    es: {
        "nav.overview": "Resumen",
        "nav.simulator": "Simulador 3D",
        "nav.brain": "Agente Espacial",
        "nav.jupyter": "Laboratorio Jupyter",
        "ctrl.presets": "Órbitas Predefinidas",
        "preset.custom": "Personalizada",
        "preset.leo": "LEO (ISS)",
        "preset.meo": "MEO (GPS)",
        "preset.geo": "GEO",
        "preset.heo": "HEO (Molniya)",
        "ctrl.constellation": "⚡ VISTA MULTI-ÓRBITA",
        "ctrl.elements": "Elementos Clásicos",
        "element.a": "Semieje mayor (a)",
        "element.e": "Excentricidad (e)",
        "element.i": "Inclinación (i)",
        "element.argp": "Arg. del Perigeo (ω)",
        "metric.period": "Periodo Orbital",
        "metric.perigee": "Altitud Perigeo",
        "metric.apogee": "Altitud Apogeo",
        "brain.agent_title": "Agente Espacial APEX-1",
        "brain.agent_subtitle": "EN LÍNEA | BASE DE CONOCIMIENTO SINCRONIZADA",
        "brain.send": "Enviar"
    },
    zh: {
        "nav.overview": "概览",
        "nav.simulator": "3D 模拟器",
        "nav.brain": "太空智能体",
        "nav.jupyter": "Jupyter 实验室",
        "ctrl.presets": "预设轨道",
        "preset.custom": "自定义",
        "preset.leo": "低地轨道 (ISS)",
        "preset.meo": "中地轨道 (GPS)",
        "preset.geo": "地球同步轨道",
        "preset.heo": "高椭圆轨道 (Molniya)",
        "ctrl.constellation": "⚡ 多轨道星座视图",
        "ctrl.elements": "经典轨道根数",
        "element.a": "半长轴 (a)",
        "element.e": "偏心率 (e)",
        "element.i": "轨道倾角 (i)",
        "element.argp": "近地点幅角 (ω)",
        "metric.period": "轨道周期",
        "metric.perigee": "近地点高度",
        "metric.apogee": "远地点高度",
        "brain.agent_title": "APEX-1 太空智能体",
        "brain.agent_subtitle": "在线 | 知识库已同步",
        "brain.send": "发送"
    }
};
'''
if 'const translations =' in app_js:
    # We replace the old translations block
    import re
    app_js = re.sub(r'const translations\s*=\s*\{.*?\};', translations_code, app_js, flags=re.DOTALL)
else:
    app_js = translations_code + '\n' + app_js

# Toggle Video Background based on tab
video_toggle = '''
    const bgVideo = document.getElementById('bg-video');
    if (bgVideo) {
        if (tabId === 'brain') {
            bgVideo.style.display = 'none';
        } else {
            bgVideo.style.display = 'block';
        }
    }
'''
if "bgVideo.style.display" not in app_js:
    app_js = app_js.replace("tabPane.classList.add('active');", f"tabPane.classList.add('active');\n{video_toggle}")

with open(app_file, 'w', encoding='utf-8') as f:
    f.write(app_js)

print("Glassmorphism & Organism injected successfully.")
