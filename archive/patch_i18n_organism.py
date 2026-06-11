import re

app_file = r'c:\Users\invde\OneDrive\Documents\gnss-orbital-py\frontend\js\app.js'
html_file = r'c:\Users\invde\OneDrive\Documents\gnss-orbital-py\frontend\index.html'

# 1. Update app.js tab switcher
with open(app_file, 'r', encoding='utf-8') as f:
    js = f.read()

old_tab_switcher = '''// Navigation Tabs Switcher
document.querySelectorAll(".nav-item").forEach(btn => {
    btn.addEventListener("click", () => {
        document.querySelectorAll(".nav-item").forEach(item => item.classList.remove("active"));
        document.querySelectorAll(".tab-pane").forEach(pane => pane.classList.remove("active"));
        
        btn.classList.add("active");
        const tab = btn.getAttribute("data-tab");
        document.getElementById(`tab-${tab}`).classList.add("active");
        
        // Trigger resize on WebGL canvas when Simulator becomes visible to avoid black areas
        if (tab === "simulator") {
            setTimeout(() => {
                onWindowResize();
                updatePlot();
            }, 60);
        }
    });
});'''

new_tab_switcher = '''// Navigation Tabs Switcher
document.querySelectorAll(".nav-item").forEach(btn => {
    btn.addEventListener("click", () => {
        document.querySelectorAll(".nav-item").forEach(item => item.classList.remove("active"));
        document.querySelectorAll(".tab-pane").forEach(pane => pane.classList.remove("active"));
        
        btn.classList.add("active");
        const tab = btn.getAttribute("data-tab");
        document.getElementById(`tab-${tab}`).classList.add("active");
        
        const bgVideo = document.getElementById("bg-video");
        const canvasContainer = document.getElementById("canvas-container");
        const organism = document.getElementById("ai-organism-container");
        
        if (tab === "brain") {
            if(bgVideo) bgVideo.style.opacity = "0";
            if(canvasContainer) canvasContainer.style.opacity = "0";
            if(organism) organism.style.opacity = "1";
        } else {
            if(bgVideo) bgVideo.style.opacity = "1";
            if(canvasContainer) canvasContainer.style.opacity = "1";
            if(organism) organism.style.opacity = "0";
        }
        
        // Trigger resize on WebGL canvas when Simulator becomes visible to avoid black areas
        if (tab === "simulator") {
            setTimeout(() => {
                onWindowResize();
                updatePlot();
            }, 60);
        }
    });
});'''

js = js.replace(old_tab_switcher, new_tab_switcher)

# Expand translations dictionary in app.js
translations_patch = '''    en: {
        "nav.overview": "Overview",
        "nav.simulator": "3D Simulator",
        "nav.brain": "Space Agent",
        "nav.jupyter": "Jupyter Lab",
        "sidebar.header1": "APEX-1",
        "sidebar.header2": "ACADEMY DECK 2050",
        "sidebar.logs": "DECK LOGS",
        "sidebar.hologram": "Hologram:",
        "sidebar.cores": "Cores:",
        "sidebar.db": "Database:",
        "sidebar.stable": "STABLE",
        "sidebar.online": "100% ONLINE",
        "hud.stardate": "STARDATE:",
        "hud.telemetry": "TELEMETRY LINK:",
        "hud.sector": "SECTOR:",
        "hud.active": "ACTIVE",
        "overview.system_monitor": "SYSTEM MONITOR",
        "overview.ionosphere": "Ionosphere Density",
        "overview.solar_wind": "Solar Wind Speed",
        "overview.clock_shift": "Clock Relativistic Shift",
        "overview.gravitational": "Gravitational Parameter:",
        "overview.earth_radius": "Earth Equatorial Radius:",
        "overview.zonal_harmonics": "Zonal Harmonics Bulge:",
        "ctrl.presets": "Orbit Presets",
        "preset.custom": "Custom",
        "preset.leo": "LEO (ISS)",
        "preset.meo": "MEO (GPS)",
        "preset.geo": "GEO",
        "preset.heo": "HEO (Molniya)",
        "ctrl.constellation": "◈ MULTI-ORBIT VIEW",
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
        "brain.send": "Send",
        "brain.welcome": "System connection established. How can I assist your orbital operations today?",
        "brain.placeholder": "Query APEX-1 (e.g. Hohmann, J2, GNSS)...",
        "teacher.reply_intro": "According to the archival records in `{document}`:",
        "teacher.no_match": "No match found in current tactical database. Try expanding your parameters.",
        "teacher.offtopic": "Query rejected: Irrelevant to orbital dynamics or current mission parameters.",
        "topics.1": "What is a Hohmann Transfer?",
        "topics.2": "Explain Kepler's Laws",
        "topics.3": "How does GPS work?",
        "topics.4": "Show Vis-Viva equation"
    },
    es: {
        "nav.overview": "Resumen",
        "nav.simulator": "Simulador 3D",
        "nav.brain": "Agente Espacial",
        "nav.jupyter": "Laboratorio Jupyter",
        "sidebar.header1": "APEX-1",
        "sidebar.header2": "CUBIERTA ACADEMIA 2050",
        "sidebar.logs": "REGISTROS DE CUBIERTA",
        "sidebar.hologram": "Holograma:",
        "sidebar.cores": "Núcleos:",
        "sidebar.db": "Base de Datos:",
        "sidebar.stable": "ESTABLE",
        "sidebar.online": "100% EN LÍNEA",
        "hud.stardate": "FECHA ESTELAR:",
        "hud.telemetry": "ENLACE TELEMETRÍA:",
        "hud.sector": "SECTOR:",
        "hud.active": "ACTIVO",
        "overview.system_monitor": "MONITOR DEL SISTEMA",
        "overview.ionosphere": "Densidad Ionosférica",
        "overview.solar_wind": "Velocidad Viento Solar",
        "overview.clock_shift": "Desplazamiento Relativista",
        "overview.gravitational": "Parámetro Gravitacional:",
        "overview.earth_radius": "Radio Ecuatorial Terrestre:",
        "overview.zonal_harmonics": "Achatamiento Armónico Zonal:",
        "ctrl.presets": "Órbitas Predefinidas",
        "preset.custom": "Personalizada",
        "preset.leo": "LEO (ISS)",
        "preset.meo": "MEO (GPS)",
        "preset.geo": "GEO",
        "preset.heo": "HEO (Molniya)",
        "ctrl.constellation": "◈ VISTA MULTI-ÓRBITA",
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
        "brain.send": "Enviar",
        "brain.welcome": "Conexión al sistema establecida. ¿Cómo puedo asistir en tus operaciones orbitales hoy?",
        "brain.placeholder": "Consulta a APEX-1 (ej. Hohmann, J2, GNSS)...",
        "teacher.reply_intro": "Según los registros de archivo en `{document}`:",
        "teacher.no_match": "No se encontraron coincidencias en la base de datos táctica. Intenta expandir los parámetros.",
        "teacher.offtopic": "Consulta rechazada: Irrelevante a la dinámica orbital o parámetros de la misión actual.",
        "topics.1": "¿Qué es una Transferencia de Hohmann?",
        "topics.2": "Explica las Leyes de Kepler",
        "topics.3": "¿Cómo funciona el GPS?",
        "topics.4": "Ecuación Vis-Viva"
    },
    zh: {
        "nav.overview": "概览",
        "nav.simulator": "3D 模拟器",
        "nav.brain": "太空智能体",
        "nav.jupyter": "Jupyter 实验室",
        "sidebar.header1": "APEX-1",
        "sidebar.header2": "2050 学院甲板",
        "sidebar.logs": "甲板日志",
        "sidebar.hologram": "全息投影:",
        "sidebar.cores": "核心:",
        "sidebar.db": "数据库:",
        "sidebar.stable": "稳定",
        "sidebar.online": "100% 在线",
        "hud.stardate": "星历:",
        "hud.telemetry": "遥测链接:",
        "hud.sector": "扇区:",
        "hud.active": "活跃",
        "overview.system_monitor": "系统监视器",
        "overview.ionosphere": "电离层密度",
        "overview.solar_wind": "太阳风速度",
        "overview.clock_shift": "相对论时钟偏移",
        "overview.gravitational": "引力常数:",
        "overview.earth_radius": "地球赤道半径:",
        "overview.zonal_harmonics": "带谐系数:",
        "ctrl.presets": "预设轨道",
        "preset.custom": "自定义",
        "preset.leo": "低地轨道 (ISS)",
        "preset.meo": "中地轨道 (GPS)",
        "preset.geo": "地球同步轨道",
        "preset.heo": "高椭圆轨道 (Molniya)",
        "ctrl.constellation": "◈ 多轨道星座视图",
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
        "brain.send": "发送",
        "brain.welcome": "系统连接已建立。今天我能为您提供什么轨道操作协助？",
        "brain.placeholder": "查询 APEX-1 (例如：Hohmann, J2, GNSS)...",
        "teacher.reply_intro": "根据 `{document}` 中的档案记录：",
        "teacher.no_match": "当前战术数据库中未找到匹配项。请尝试扩展您的参数。",
        "teacher.offtopic": "查询被拒绝：与轨道动力学或当前任务参数无关。",
        "topics.1": "什么是霍曼转移？",
        "topics.2": "解释开普勒定律",
        "topics.3": "GPS 是如何工作的？",
        "topics.4": "显示活力方程 (Vis-Viva)"
    }'''

# Find the start and end of translations object
start_idx = js.find('en: {')
end_idx = js.find('};', start_idx)
if start_idx != -1 and end_idx != -1:
    js = js[:start_idx] + translations_patch + js[end_idx:]

with open(app_file, 'w', encoding='utf-8') as f:
    f.write(js)

# 2. Update index.html
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Add organism container
organism_html = '''
    <!-- Living Digital AI Organism Background -->
    <div id="ai-organism-container" style="position: absolute; top:0; left:0; width:100%; height:100%; z-index:0; opacity:0; pointer-events:none; transition: opacity 1s ease;">
        <div class="organism-core"></div>
        <div class="organism-ring ring-1"></div>
        <div class="organism-ring ring-2"></div>
        <div class="organism-particles"></div>
    </div>
'''
if 'id="ai-organism-container"' not in html:
    html = html.replace('<!-- UI Overlay -->', organism_html + '\n    <!-- UI Overlay -->')

# Add missing data-i18n tags using precise replaces
replaces = {
    '<h2>APEX-1</h2>': '<h2 data-i18n="sidebar.header1">APEX-1</h2>',
    '<span class="brand-subtitle">ACADEMY DECK 2050</span>': '<span class="brand-subtitle" data-i18n="sidebar.header2">ACADEMY DECK 2050</span>',
    '<h3 class="logs-title">DECK LOGS</h3>': '<h3 class="logs-title" data-i18n="sidebar.logs">DECK LOGS</h3>',
    '<span class="log-label">Hologram:</span>': '<span class="log-label" data-i18n="sidebar.hologram">Hologram:</span>',
    '<span class="log-label">Cores:</span>': '<span class="log-label" data-i18n="sidebar.cores">Cores:</span>',
    '<span class="log-label">Database:</span>': '<span class="log-label" data-i18n="sidebar.db">Database:</span>',
    '<span class="log-val glow-cyan">STABLE</span>': '<span class="log-val glow-cyan" data-i18n="sidebar.stable">STABLE</span>',
    '<span class="log-val">100% ONLINE</span>': '<span class="log-val" data-i18n="sidebar.online">100% ONLINE</span>',
    '<span class="hud-label">STARDATE:</span>': '<span class="hud-label" data-i18n="hud.stardate">STARDATE:</span>',
    '<span class="hud-label">TELEMETRY LINK:</span>': '<span class="hud-label" data-i18n="hud.telemetry">TELEMETRY LINK:</span>',
    '<span class="hud-label">SECTOR:</span>': '<span class="hud-label" data-i18n="hud.sector">SECTOR:</span>',
    '<span class="hud-value glow-green">ACTIVE</span>': '<span class="hud-value glow-green" data-i18n="hud.active">ACTIVE</span>',
    '<h4 class="sensor-title">SYSTEM MONITOR</h4>': '<h4 class="sensor-title" data-i18n="overview.system_monitor">SYSTEM MONITOR</h4>',
    '<span class="sensor-label">Ionosphere Density</span>': '<span class="sensor-label" data-i18n="overview.ionosphere">Ionosphere Density</span>',
    '<span class="sensor-label">Solar Wind Speed</span>': '<span class="sensor-label" data-i18n="overview.solar_wind">Solar Wind Speed</span>',
    '<span class="sensor-label">Clock Relativistic Shift</span>': '<span class="sensor-label" data-i18n="overview.clock_shift">Clock Relativistic Shift</span>',
    '<span class="label">Gravitational Parameter:</span>': '<span class="label" data-i18n="overview.gravitational">Gravitational Parameter:</span>',
    '<span class="label">Earth Equatorial Radius:</span>': '<span class="label" data-i18n="overview.earth_radius">Earth Equatorial Radius:</span>',
    '<span class="label">Zonal Harmonics Bulge:</span>': '<span class="label" data-i18n="overview.zonal_harmonics">Zonal Harmonics Bulge:</span>',
    '<h2>APEX-1 ORBITAL OPERATIONS</h2>': '<h2 data-i18n="overview.title">APEX-1 ORBITAL OPERATIONS</h2>',
}

for k, v in replaces.items():
    html = html.replace(k, v)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)
