// Astrodynamics Lab Core Application Controller (Year 2050 Theme)
// Coordinates WebGL/Three.js starfield, realistic Earth textures, parallax backgrounds, and AI chat agent

// Constants
const MU_EARTH = 398600.4418; // km^3/s^2
const EARTH_RADIUS = 6371.0; // km

// Dictionary of localized UI strings

const translations = {
        en: {
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
        "topics.4": "Show Vis-Viva equation",
        "agent.status.online": "CORE ONLINE",
        "agent.status.listening": "LISTENING",
        "agent.status.thinking": "PROCESSING QUERY",
        "agent.status.speaking": "TRANSMITTING",
        "brain.routed": "ROUTED VIA",
        "jupyter.title": "Research Console",
        "jupyter.subtitle": "Interactive notebooks with the full Python astrodynamics engine.",
        "jupyter.status.checking": "SCANNING FOR LOCAL KERNEL…",
        "jupyter.status.online": "KERNEL ONLINE — PORT 8888",
        "jupyter.status.offline": "KERNEL OFFLINE — LAUNCH JUPYTERLAB TO EMBED",
        "jupyter.recheck": "RESCAN",
        "jupyter.copy": "COPY",
        "jupyter.copied": "COPIED ✓",
        "jupyter.offline_hint": "No JupyterLab server detected on port 8888. Launch it from the project root:",
        "jupyter.need_kernel": "⚠ KERNEL REQUIRED — RUN THE COMMAND BELOW. IF BLOCKED, CLICK 'OPEN IN TAB'",
        "jupyter.back": "CONSOLE",
        "jupyter.external": "OPEN IN TAB ↗",
        "jupyter.open": "OPEN NOTEBOOK",
        "nb.01.title": "Interactive Orbits",
        "nb.01.desc": "Visual study of the six classical orbital elements with live 3D Plotly widgets.",
        "nb.02.title": "Kepler's Equation",
        "nb.02.desc": "Newton-Raphson convergence analysis of M = E − e·sin E, step by step.",
        "nb.03.title": "IRIS² Constellation",
        "nb.03.desc": "Modeling the EU multi-orbital LEO/MEO hybrid constellation: latency and coverage.",
        "nb.badge.bronze": "BRONZE",
        "nb.badge.silver": "SILVER",
        "nb.badge.master": "MASTER"
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
        "topics.4": "Ecuación Vis-Viva",
        "agent.status.online": "NÚCLEO EN LÍNEA",
        "agent.status.listening": "ESCUCHANDO",
        "agent.status.thinking": "PROCESANDO CONSULTA",
        "agent.status.speaking": "TRANSMITIENDO",
        "brain.routed": "ENRUTADO VÍA",
        "jupyter.title": "Consola de Investigación",
        "jupyter.subtitle": "Cuadernos interactivos con el motor de astrodinámica Python completo.",
        "jupyter.status.checking": "BUSCANDO KERNEL LOCAL…",
        "jupyter.status.online": "KERNEL EN LÍNEA — PUERTO 8888",
        "jupyter.status.offline": "KERNEL APAGADO — INICIA JUPYTERLAB PARA INTEGRAR",
        "jupyter.recheck": "REESCANEAR",
        "jupyter.copy": "COPIAR",
        "jupyter.copied": "COPIADO ✓",
        "jupyter.offline_hint": "No se detectó servidor JupyterLab en el puerto 8888. Inícialo desde la raíz del proyecto:",
        "jupyter.need_kernel": "⚠ KERNEL REQUERIDO — EJECUTA EL COMANDO DE ABAJO. SI SE BLOQUEA, CLIC EN 'OPEN IN TAB'",
        "jupyter.back": "CONSOLA",
        "jupyter.external": "ABRIR EN PESTAÑA ↗",
        "jupyter.open": "ABRIR CUADERNO",
        "nb.01.title": "Órbitas Interactivas",
        "nb.01.desc": "Estudio visual de los seis elementos orbitales clásicos con widgets 3D de Plotly.",
        "nb.02.title": "Ecuación de Kepler",
        "nb.02.desc": "Análisis de convergencia Newton-Raphson de M = E − e·sin E, paso a paso.",
        "nb.03.title": "Constelación IRIS²",
        "nb.03.desc": "Modelado de la constelación híbrida LEO/MEO de la UE: latencia y cobertura.",
        "nb.badge.bronze": "BRONCE",
        "nb.badge.silver": "PLATA",
        "nb.badge.master": "MAESTRO"
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
        "topics.4": "显示活力方程 (Vis-Viva)",
        "agent.status.online": "核心在线",
        "agent.status.listening": "正在聆听",
        "agent.status.thinking": "正在处理查询",
        "agent.status.speaking": "正在传输",
        "brain.routed": "路由至",
        "jupyter.title": "研究控制台",
        "jupyter.subtitle": "交互式笔记本，内置完整的 Python 天体动力学引擎。",
        "jupyter.status.checking": "正在扫描本地内核…",
        "jupyter.status.online": "内核在线 — 端口 8888",
        "jupyter.status.offline": "内核离线 — 启动 JUPYTERLAB 以嵌入",
        "jupyter.recheck": "重新扫描",
        "jupyter.copy": "复制",
        "jupyter.copied": "已复制 ✓",
        "jupyter.offline_hint": "未在 8888 端口检测到 JupyterLab 服务器。请在项目根目录启动：",
        "jupyter.need_kernel": "⚠ 需要内核 — 请运行下方命令。如果被浏览器拦截，请点击 'OPEN IN TAB'",
        "jupyter.back": "控制台",
        "jupyter.external": "在新标签页打开 ↗",
        "jupyter.open": "打开笔记本",
        "nb.01.title": "交互式轨道",
        "nb.01.desc": "使用 Plotly 3D 实时控件可视化研究六个经典轨道根数。",
        "nb.02.title": "开普勒方程",
        "nb.02.desc": "逐步进行 M = E − e·sin E 的牛顿-拉夫森收敛分析。",
        "nb.03.title": "IRIS² 星座",
        "nb.03.desc": "建模欧盟 LEO/MEO 混合多轨道星座：延迟与覆盖范围。",
        "nb.badge.bronze": "铜级",
        "nb.badge.silver": "银级",
        "nb.badge.master": "大师级"
    }};


// Space Domain Keywords (Anti-troll Filter)
const spaceKeywords = [
    "orbit", "space", "satellite", "kepler", "gnss", "gps", "galileo", "beidou",
    "glonass", "iris2", "drag", "j2", "radiation", "propagate", "trajectory",
    "hohmann", "apogee", "perigee", "eccentricity", "inclination", "raan",
    "anomaly", "time", "clock", "precision", "relativity", "gravity", "transfer",
    "decommission", "srp", "constellation", "altitude",
    "vis-viva", "viva", "equation", "velocity", "energy", "period",
    "leo", "meo", "geo", "heo", "molniya", "iss", "starlink", "newton",
    "orbita", "órbita", "espacio", "satelite", "satélite", "arrastre", "radiacion", "propagar",
    "trayectoria", "apogeo", "perigeo", "excentricidad", "inclinacion",
    "anomalia", "tiempo", "reloj", "relatividad", "gravedad", "transferencia",
    "constelacion", "altitud", "despliegue",
    "ecuacion", "ecuación", "velocidad", "energia", "energía", "periodo", "leyes",
    "轨道", "空间", "太空", "卫星", "开普勒", "高度", "偏心率", "倾角",
    "升交点", "近地点", "远地点", "周期", "摄动", "大气阻力", "相对论",
    "方程", "活力", "速度", "能量", "定律", "霍曼"
];

// App State
let currentLang = "en";

// Three.js Global Objects for Simulator
let scene, camera, renderer, controls;
let earthMesh, earthWireframe, atmosphere, cloudMesh;
let orbitLine, commBeam;
let satelliteMesh;
let orbitalParams = { a: 7000, e: 0.01, i: 51.6, raan: 0, argp: 0 };
let satTime = 0;
let isConstellationMode = false;
let constellationGroup = [];
 // Simulated time tracker for orbits

// Raycaster & Moon Globals
let raycaster = new THREE.Raycaster();
let mouse = new THREE.Vector2();
let moonMesh;
let earthMat; // make earthMat accessible if needed


// Three.js Global Objects for Interactive 3D Background
let bgScene, bgCamera, bgRenderer, bgStars;
let mouseX = 0, mouseY = 0;

// --- 1. DIGITAL CLOCK STARDATE ---
function updateClock() {
    const clockEl = document.getElementById("digital-clock");
    if (!clockEl) return;
    
    const now = new Date();
    // Offset clock by +24 years to display the year 2050
    const year = now.getUTCFullYear() + 24;
    const month = String(now.getUTCMonth() + 1).padStart(2, '0');
    const day = String(now.getUTCDate()).padStart(2, '0');
    const hours = String(now.getUTCHours()).padStart(2, '0');
    const minutes = String(now.getUTCMinutes()).padStart(2, '0');
    const seconds = String(now.getUTCSeconds()).padStart(2, '0');
    
    clockEl.innerText = `${year}.${month}.${day} ${hours}:${minutes}:${seconds} UTC`;
}
setInterval(updateClock, 1000);


// --- 2. MATHEMATICAL SOLVERS ---

// Newton-Raphson Kepler Solver
function solveKepler(M, e, tol = 1e-10, maxIter = 100) {
    let E = M;
    for (let it = 0; it < maxIter; it++) {
        let f = E - e * Math.sin(E) - M;
        let df = 1.0 - e * Math.cos(E);
        let delta = f / df;
        E -= delta;
        if (Math.abs(delta) < tol) return E;
    }
    return E;
}

// Convert Eccentric Anomaly to True Anomaly
function trueAnomalyFromEccentric(E, e) {
    let factor = Math.sqrt((1 + e) / (1 - e));
    let nu = 2.0 * Math.atan2(factor * Math.sin(E / 2.0), Math.cos(E / 2.0));
    return nu < 0 ? nu + 2 * Math.PI : nu;
}

// Solve Cartesian ECI coordinates from Classical Elements and True Anomaly
function getCartesianPosition(a, e, i_deg, raan_deg, argp_deg, nu) {
    let i = i_deg * Math.PI / 180;
    let raan = raan_deg * Math.PI / 180;
    let argp = argp_deg * Math.PI / 180;
    
    let p = a * (1.0 - e * e);
    let r = p / (1.0 + e * Math.cos(nu));
    
    let x_pqw = r * Math.cos(nu);
    let y_pqw = r * Math.sin(nu);
    
    let cos_O = Math.cos(raan), sin_O = Math.sin(raan);
    let cos_i = Math.cos(i), sin_i = Math.sin(i);
    let cos_w = Math.cos(argp), sin_w = Math.sin(argp);
    
    let r11 = cos_O * cos_w - sin_O * sin_w * cos_i;
    let r21 = sin_O * cos_w + cos_O * sin_w * cos_i;
    let r31 = sin_w * sin_i;
    
    let r12 = -cos_O * sin_w - sin_O * cos_w * cos_i;
    let r22 = -sin_O * sin_w + cos_O * cos_w * cos_i;
    let r32 = cos_w * sin_i;
    
    return {
        x: r11 * x_pqw + r12 * y_pqw,
        y: r21 * x_pqw + r22 * y_pqw,
        z: r31 * x_pqw + r32 * y_pqw
    };
}


// --- 3. GLOBAL INTERACTIVE 3D DEEP-SPACE BACKGROUND ---
// Three parallax star layers + procedural nebulae + occasional shooting stars.

let bgStarLayers = [];
let bgNebulae = [];
let bgShootingStars = [];
let bgLastShootingStar = 0;
let bgPlexus = null;          // the living bio-digital tissue layer

// Soft radial-gradient sprite texture used for nebula clouds
function makeNebulaTexture(r, g, b) {
    const size = 256;
    const canvas = document.createElement("canvas");
    canvas.width = canvas.height = size;
    const ctx = canvas.getContext("2d");
    const grad = ctx.createRadialGradient(size / 2, size / 2, 0, size / 2, size / 2, size / 2);
    grad.addColorStop(0.0, `rgba(${r}, ${g}, ${b}, 0.55)`);
    grad.addColorStop(0.4, `rgba(${r}, ${g}, ${b}, 0.18)`);
    grad.addColorStop(1.0, "rgba(0, 0, 0, 0)");
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, size, size);
    return new THREE.CanvasTexture(canvas);
}

function initBackgroundThreeJS() {
    const canvas = document.getElementById("bg-canvas");
    if (!canvas) return;

    bgScene = new THREE.Scene();

    bgCamera = new THREE.PerspectiveCamera(60, window.innerWidth / window.innerHeight, 1, 10000);
    bgCamera.position.z = 1000;

    bgRenderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true });
    bgRenderer.setSize(window.innerWidth, window.innerHeight);
    bgRenderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));

    // Three star layers at different depths: far dust, mid field, near bright stars
    const layerSpecs = [
        { count: 700, spread: 3200, size: 1.6, color: 0x8fa8c0, opacity: 0.45, drift: 0.00012 },
        { count: 350, spread: 2400, size: 3.0, color: 0xbfd9e8, opacity: 0.55, drift: 0.00028 },
        { count: 120, spread: 1700, size: 5.0, color: 0xeaf6ff, opacity: 0.85, drift: 0.0005 }
    ];
    bgStarLayers = layerSpecs.map((spec) => {
        const geo = new THREE.BufferGeometry();
        const pos = new Float32Array(spec.count * 3);
        for (let k = 0; k < spec.count * 3; k++) pos[k] = (Math.random() - 0.5) * spec.spread;
        geo.setAttribute("position", new THREE.BufferAttribute(pos, 3));
        const mat = new THREE.PointsMaterial({
            color: spec.color,
            size: spec.size,
            transparent: true,
            opacity: spec.opacity,
            blending: THREE.AdditiveBlending,
            depthWrite: false
        });
        const points = new THREE.Points(geo, mat);
        points.userData = { drift: spec.drift, baseOpacity: spec.opacity, phase: Math.random() * Math.PI * 2 };
        bgScene.add(points);
        return points;
    });

    // Procedural nebula clouds drifting in the far field
    const nebulaPalette = [
        [40, 90, 140], [60, 140, 160], [90, 70, 150], [30, 110, 120]
    ];
    bgNebulae = [];
    for (let i = 0; i < 7; i++) {
        const c = nebulaPalette[i % nebulaPalette.length];
        const tex = makeNebulaTexture(c[0], c[1], c[2]);
        const mat = new THREE.SpriteMaterial({
            map: tex,
            transparent: true,
            opacity: 0.4 + Math.random() * 0.25,
            blending: THREE.AdditiveBlending,
            depthWrite: false
        });
        const sprite = new THREE.Sprite(mat);
        const scale = 900 + Math.random() * 1400;
        sprite.scale.set(scale, scale, 1);
        sprite.position.set(
            (Math.random() - 0.5) * 2600,
            (Math.random() - 0.5) * 1600,
            -800 - Math.random() * 1500
        );
        sprite.userData = {
            vx: (Math.random() - 0.5) * 0.12,
            vy: (Math.random() - 0.5) * 0.06,
            pulse: Math.random() * Math.PI * 2
        };
        bgScene.add(sprite);
        bgNebulae.push(sprite);
    }

    // Bio-digital plexus: a colony of wandering luminous cells that grow
    // and dissolve synaptic links — the universe itself feels alive
    initBgPlexus();

    // Track mouse movement for magnetic parallax effect
    window.addEventListener("mousemove", (e) => {
        mouseX = (e.clientX - window.innerWidth / 2) * 0.22;
        mouseY = (e.clientY - window.innerHeight / 2) * 0.22;
    });

    window.addEventListener("resize", () => {
        bgCamera.aspect = window.innerWidth / window.innerHeight;
        bgCamera.updateProjectionMatrix();
        bgRenderer.setSize(window.innerWidth, window.innerHeight);
    });

    animateBackground();
}

function initBgPlexus() {
    const N = 46;
    const BOUNDS = { x: 1500, y: 950, z: 350 };
    const nodes = [];
    for (let i = 0; i < N; i++) {
        nodes.push({
            pos: new THREE.Vector3(
                (Math.random() - 0.5) * 2 * BOUNDS.x,
                (Math.random() - 0.5) * 2 * BOUNDS.y,
                -150 - Math.random() * BOUNDS.z
            ),
            vel: new THREE.Vector3(
                (Math.random() - 0.5) * 0.5,
                (Math.random() - 0.5) * 0.35,
                (Math.random() - 0.5) * 0.1
            ),
            phase: Math.random() * Math.PI * 2
        });
    }

    // Cell bodies: soft bioluminescent points
    const cellGeo = new THREE.BufferGeometry();
    cellGeo.setAttribute("position", new THREE.BufferAttribute(new Float32Array(N * 3), 3));
    const cellMat = new THREE.PointsMaterial({
        color: 0x57e6c9,
        size: 7,
        transparent: true,
        opacity: 0.5,
        blending: THREE.AdditiveBlending,
        depthWrite: false
    });
    const cells = new THREE.Points(cellGeo, cellMat);
    bgScene.add(cells);

    // Synapses: preallocated line buffer with per-vertex fading colors
    const MAX_LINKS = 260;
    const lineGeo = new THREE.BufferGeometry();
    lineGeo.setAttribute("position", new THREE.BufferAttribute(new Float32Array(MAX_LINKS * 6), 3));
    lineGeo.setAttribute("color", new THREE.BufferAttribute(new Float32Array(MAX_LINKS * 6), 3));
    const lineMat = new THREE.LineBasicMaterial({
        vertexColors: true,
        transparent: true,
        opacity: 0.55,
        blending: THREE.AdditiveBlending,
        depthWrite: false
    });
    const links = new THREE.LineSegments(lineGeo, lineMat);
    bgScene.add(links);

    bgPlexus = { nodes, cells, links, BOUNDS, MAX_LINKS, LINK_DIST: 300 };
}

function updateBgPlexus(t) {
    if (!bgPlexus) return;
    const { nodes, cells, links, BOUNDS, MAX_LINKS, LINK_DIST } = bgPlexus;

    // Wander: organic drift with a heartbeat-like micro jitter
    const cellPos = cells.geometry.attributes.position.array;
    nodes.forEach((n, i) => {
        n.vel.x += Math.sin(t * 0.4 + n.phase) * 0.004;
        n.vel.y += Math.cos(t * 0.33 + n.phase * 1.7) * 0.003;
        n.pos.add(n.vel);
        if (Math.abs(n.pos.x) > BOUNDS.x) n.vel.x *= -1;
        if (Math.abs(n.pos.y) > BOUNDS.y) n.vel.y *= -1;
        if (n.pos.z > -100 || n.pos.z < -150 - BOUNDS.z) n.vel.z *= -1;
        cellPos[i * 3] = n.pos.x;
        cellPos[i * 3 + 1] = n.pos.y;
        cellPos[i * 3 + 2] = n.pos.z;
    });
    cells.geometry.attributes.position.needsUpdate = true;
    cells.material.opacity = 0.35 + 0.2 * Math.sin(t * 0.9);
    cells.material.size = 6 + 2.2 * Math.sin(t * 0.7);

    // Grow/dissolve synaptic links by proximity; brightness = closeness
    const lp = links.geometry.attributes.position.array;
    const lc = links.geometry.attributes.color.array;
    let li = 0;
    const heartbeat = 0.6 + 0.4 * Math.sin(t * 1.3);
    for (let i = 0; i < nodes.length && li < MAX_LINKS; i++) {
        for (let j = i + 1; j < nodes.length && li < MAX_LINKS; j++) {
            const d = nodes[i].pos.distanceTo(nodes[j].pos);
            if (d < LINK_DIST) {
                const w = (1 - d / LINK_DIST) * heartbeat;
                const o = li * 6;
                lp[o] = nodes[i].pos.x; lp[o + 1] = nodes[i].pos.y; lp[o + 2] = nodes[i].pos.z;
                lp[o + 3] = nodes[j].pos.x; lp[o + 4] = nodes[j].pos.y; lp[o + 5] = nodes[j].pos.z;
                lc[o] = 0.18 * w; lc[o + 1] = 0.85 * w; lc[o + 2] = 0.72 * w;
                lc[o + 3] = 0.25 * w; lc[o + 4] = 0.6 * w; lc[o + 5] = 0.85 * w;
                li++;
            }
        }
    }
    links.geometry.setDrawRange(0, li * 2);
    links.geometry.attributes.position.needsUpdate = true;
    links.geometry.attributes.color.needsUpdate = true;
}

function spawnShootingStar() {
    const points = [new THREE.Vector3(0, 0, 0), new THREE.Vector3(-90, 14, 0)];
    const geo = new THREE.BufferGeometry().setFromPoints(points);
    const mat = new THREE.LineBasicMaterial({
        color: 0xdef4ff,
        transparent: true,
        opacity: 0.9,
        blending: THREE.AdditiveBlending
    });
    const line = new THREE.Line(geo, mat);
    line.position.set(
        400 + Math.random() * 900,
        300 + Math.random() * 500,
        -200 - Math.random() * 400
    );
    line.userData = {
        vx: -(7 + Math.random() * 6),
        vy: -(1 + Math.random() * 2.5),
        life: 1.0
    };
    bgScene.add(line);
    bgShootingStars.push(line);
}

function animateBackground() {
    requestAnimationFrame(animateBackground);
    const now = performance.now();
    const t = now / 1000;

    // Star layers: slow counter-rotations + gentle twinkle per layer
    bgStarLayers.forEach((layer, idx) => {
        layer.rotation.y += layer.userData.drift * (idx % 2 === 0 ? 1 : -1);
        layer.rotation.x += layer.userData.drift * 0.3;
        layer.material.opacity = layer.userData.baseOpacity * (0.82 + 0.18 * Math.sin(t * 1.7 + layer.userData.phase));
    });

    // The living tissue layer
    updateBgPlexus(t);

    // Nebulae drift and breathe
    bgNebulae.forEach((n) => {
        n.position.x += n.userData.vx;
        n.position.y += n.userData.vy;
        if (Math.abs(n.position.x) > 1600) n.userData.vx *= -1;
        if (Math.abs(n.position.y) > 1000) n.userData.vy *= -1;
        n.material.opacity = 0.32 + 0.18 * Math.sin(t * 0.25 + n.userData.pulse);
    });

    // Occasional shooting star (every 4-9 seconds)
    if (now - bgLastShootingStar > 4000 + Math.random() * 5000) {
        bgLastShootingStar = now;
        spawnShootingStar();
    }
    for (let i = bgShootingStars.length - 1; i >= 0; i--) {
        const s = bgShootingStars[i];
        s.position.x += s.userData.vx;
        s.position.y += s.userData.vy;
        s.userData.life -= 0.012;
        s.material.opacity = Math.max(0, s.userData.life);
        if (s.userData.life <= 0) {
            bgScene.remove(s);
            s.geometry.dispose();
            s.material.dispose();
            bgShootingStars.splice(i, 1);
        }
    }

    // Interpolate camera to mouse position (Dampened Parallax)
    if (bgCamera) {
        bgCamera.position.x += (mouseX - bgCamera.position.x) * 0.05;
        bgCamera.position.y += (-mouseY - bgCamera.position.y) * 0.05;
        bgCamera.lookAt(bgScene.position);
    }

    if (bgRenderer && bgScene && bgCamera) {
        bgRenderer.render(bgScene, bgCamera);
    }
}


// --- 4. THREE.JS WEBGL SIMULATION (WITH REAL GLOBE TEXTURE) ---

// Solar-cell grid texture for the panels (procedural, no asset needed)
function makeSolarPanelTexture() {
    const canvas = document.createElement("canvas");
    canvas.width = 128; canvas.height = 64;
    const ctx = canvas.getContext("2d");
    ctx.fillStyle = "#0d2050";
    ctx.fillRect(0, 0, 128, 64);
    ctx.strokeStyle = "#2a4a9a";
    ctx.lineWidth = 1.5;
    for (let x = 0; x <= 128; x += 16) { ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, 64); ctx.stroke(); }
    for (let y = 0; y <= 64; y += 16) { ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(128, y); ctx.stroke(); }
    // Specular cell sheen
    const grad = ctx.createLinearGradient(0, 0, 128, 64);
    grad.addColorStop(0, "rgba(120, 170, 255, 0.20)");
    grad.addColorStop(0.5, "rgba(120, 170, 255, 0.02)");
    grad.addColorStop(1, "rgba(120, 170, 255, 0.15)");
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, 128, 64);
    return new THREE.CanvasTexture(canvas);
}

// NASA-style procedural satellite: gold-foil bus, gridded solar wings,
// Earth-pointing comm dish, and a blinking beacon.
function createSatelliteModel(scale) {
    const s = scale || 1.0;
    const group = new THREE.Group();

    // Gold multilayer-insulation bus
    const bus = new THREE.Mesh(
        new THREE.BoxGeometry(330 * s, 330 * s, 330 * s),
        new THREE.MeshStandardMaterial({
            color: 0xc9921e, metalness: 0.85, roughness: 0.38,
            emissive: 0x2a1d05, emissiveIntensity: 0.6
        })
    );
    group.add(bus);

    // Radiator plate (white) on one face
    const radiator = new THREE.Mesh(
        new THREE.BoxGeometry(300 * s, 300 * s, 8 * s),
        new THREE.MeshStandardMaterial({ color: 0xe8edf2, metalness: 0.1, roughness: 0.7 })
    );
    radiator.position.z = -172 * s;
    group.add(radiator);

    // Solar wings with cell-grid texture
    const panelTex = makeSolarPanelTexture();
    const panelMat = new THREE.MeshStandardMaterial({
        map: panelTex, color: 0xffffff, metalness: 0.35, roughness: 0.45,
        emissive: 0x0a1f4d, emissiveIntensity: 0.5, side: THREE.DoubleSide
    });
    const armMat = new THREE.MeshStandardMaterial({ color: 0x9aa4ae, metalness: 0.7, roughness: 0.4 });
    [-1, 1].forEach((dir) => {
        const arm = new THREE.Mesh(new THREE.CylinderGeometry(14 * s, 14 * s, 240 * s, 8), armMat);
        arm.rotation.z = Math.PI / 2;
        arm.position.x = dir * 280 * s;
        group.add(arm);

        const wing = new THREE.Mesh(new THREE.BoxGeometry(1050 * s, 8 * s, 330 * s), panelMat);
        wing.position.x = dir * (400 + 525) * s * 0.85;
        group.add(wing);
    });

    // Earth-pointing high-gain dish on +Z (group.lookAt(Earth) aims it)
    const dish = new THREE.Mesh(
        new THREE.SphereGeometry(130 * s, 24, 12, 0, Math.PI * 2, 0, Math.PI / 2),
        new THREE.MeshStandardMaterial({ color: 0xf2f5f8, metalness: 0.25, roughness: 0.5, side: THREE.DoubleSide })
    );
    dish.rotation.x = -Math.PI / 2;
    dish.position.z = 245 * s;
    group.add(dish);
    const boom = new THREE.Mesh(new THREE.CylinderGeometry(10 * s, 10 * s, 90 * s, 8), armMat);
    boom.rotation.x = Math.PI / 2;
    boom.position.z = 190 * s;
    group.add(boom);

    // Blinking navigation beacon
    const beaconMat = new THREE.MeshStandardMaterial({
        color: 0xff4444, emissive: 0xff2222, emissiveIntensity: 1.5
    });
    const beacon = new THREE.Mesh(new THREE.SphereGeometry(26 * s, 12, 12), beaconMat);
    beacon.position.y = 195 * s;
    group.add(beacon);
    group.userData.beaconMat = beaconMat;

    return group;
}

function initThreeJS() {
    const container = document.getElementById("canvas-container");
    if (!container) return;
    
    // Clear container
    container.innerHTML = "";
    
    const width = container.clientWidth;
    const height = container.clientHeight;
    
    // Create Scene
    scene = new THREE.Scene();
    
    // Setup Camera
    camera = new THREE.PerspectiveCamera(45, width / height, 100, 500000);
    camera.position.set(15000, 15000, 15000);
    
    // Setup WebGL Renderer
    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(width, height);
    renderer.setPixelRatio(window.devicePixelRatio || 1);
    container.appendChild(renderer.domElement);
    
    // Add OrbitControls
    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;
    controls.maxDistance = 280000;
    controls.minDistance = 8000;
    
    // Lighting: one warm Sun + faint cool space fill (cinema-standard
    // two-light rig for planets: day side warm, night side barely lifted)
    const ambientLight = new THREE.AmbientLight(0x223344, 0.55);
    scene.add(ambientLight);

    const dirLight = new THREE.DirectionalLight(0xfff2e0, 1.35);
    dirLight.position.set(1, 0.4, 0.8).normalize();
    scene.add(dirLight);
    
    // Deep Space Starfield Backdrop inside plot
    const starsGeo = new THREE.BufferGeometry();
    const starsCount = 1000;
    const starPositions = new Float32Array(starsCount * 3);
    for (let k = 0; k < starsCount * 3; k++) {
        starPositions[k] = (Math.random() - 0.5) * 600000;
    }
    starsGeo.setAttribute('position', new THREE.BufferAttribute(starPositions, 3));
    const starsMat = new THREE.PointsMaterial({
        color: 0xffffff,
        size: 900,
        sizeAttenuation: true,
        transparent: true,
        opacity: 0.85
    });
    const starfield = new THREE.Points(starsGeo, starsMat);
    scene.add(starfield);
    
    // Earth Solid Sphere — NASA blue-marble setup.
    // Best practice: the UI chrome stays muted (Palantir slate), but the
    // CONTENT — the planet — is rendered in full color: that contrast is
    // what makes mission displays read instantly.
    const earthGeo = new THREE.SphereGeometry(EARTH_RADIUS, 64, 64);
    const earthMat = new THREE.MeshPhongMaterial({
        color: 0x1b2a45,        // deep ocean fallback until textures stream in
        emissive: 0x060c18,
        shininess: 18,
        specular: new THREE.Color(0x333333)
    });
    
    // The Moon Setup
    const moonGeo = new THREE.SphereGeometry(1737 * 10, 32, 32); // 10x visual scale for visibility
    const moonMat = new THREE.MeshPhongMaterial({ color: 0x888888, emissive: 0x111111 });
    moonMesh = new THREE.Mesh(moonGeo, moonMat);
    // Earth-Moon distance is 384,400 km
    moonMesh.position.set(384400, 0, 0); 
    scene.add(moonMesh);

    // Stream NASA-derived planetary textures (color map, terrain relief,
    // ocean specular, rolling cloud deck) — full blue-marble treatment.
    const textureLoader = new THREE.TextureLoader();
    const PLANET_TEX = 'https://raw.githubusercontent.com/mrdoob/three.js/master/examples/textures/planets/';

    // Load Moon Texture
    textureLoader.load(PLANET_TEX + 'moon_1024.jpg', (texture) => {
        moonMat.map = texture;
        moonMat.color.setHex(0xffffff); // Reset base color so texture shines through
        moonMat.needsUpdate = true;
    });

    textureLoader.load(PLANET_TEX + 'earth_atmos_2048.jpg', (texture) => {
        earthMat.map = texture;
        earthMat.color.setHex(0xffffff);
        earthMat.emissive.setHex(0x0a0f1a);
        earthMat.needsUpdate = true;
    }, null, () => console.log("Earth texture failed to load, keeping fallback."));

    // Terrain relief so mountain ranges catch the sunlight
    textureLoader.load(PLANET_TEX + 'earth_normal_2048.jpg', (texture) => {
        earthMat.normalMap = texture;
        earthMat.normalScale = new THREE.Vector2(0.8, 0.8);
        earthMat.needsUpdate = true;
    });

    // Oceans glint, continents stay matte
    textureLoader.load(PLANET_TEX + 'earth_specular_2048.jpg', (texture) => {
        earthMat.specularMap = texture;
        earthMat.needsUpdate = true;
    });

    // Independent rolling cloud deck slightly above the surface
    textureLoader.load(PLANET_TEX + 'earth_clouds_1024.png', (texture) => {
        const cloudMat = new THREE.MeshLambertMaterial({
            map: texture,
            transparent: true,
            opacity: 0.55,
            depthWrite: false
        });
        cloudMesh = new THREE.Mesh(new THREE.SphereGeometry(EARTH_RADIUS * 1.012, 64, 64), cloudMat);
        scene.add(cloudMesh);
    });
    
    // Add Raycaster Click Event Listener
    container.addEventListener('pointerdown', (e) => {
        const rect = container.getBoundingClientRect();
        mouse.x = ((e.clientX - rect.left) / rect.width) * 2 - 1;
        mouse.y = -((e.clientY - rect.top) / rect.height) * 2 + 1;
        
        raycaster.setFromCamera(mouse, camera);
        if (satelliteMesh) {
            const intersects = raycaster.intersectObjects([satelliteMesh], true);
            if (intersects.length > 0) {
                const card = document.getElementById("satellite-telemetry-card");
                if (card) {
                    card.classList.toggle("hidden");
                }
            }
        }
    });
    
    earthMesh = new THREE.Mesh(earthGeo, earthMat);
    scene.add(earthMesh);
    
    // Faint tactical grid overlay (kept subtle so the blue marble leads)
    const gridMat = new THREE.MeshBasicMaterial({
        color: 0x4a708c,
        wireframe: true,
        transparent: true,
        opacity: 0.07
    });
    earthWireframe = new THREE.Mesh(earthGeo, gridMat);
    earthWireframe.scale.setScalar(1.002);
    scene.add(earthWireframe);

    // Atmospheric limb: fresnel rim scattering, the blue halo every
    // astronaut photo shows at the horizon
    const atmosMat = new THREE.ShaderMaterial({
        uniforms: {
            uColor: { value: new THREE.Color(0x4d9ce8) },
            uIntensity: { value: 1.1 }
        },
        vertexShader: `
            varying vec3 vNormalW;
            varying vec3 vPositionW;
            void main() {
                vNormalW = normalize(normalMatrix * normal);
                vec4 mvPosition = modelViewMatrix * vec4(position, 1.0);
                vPositionW = mvPosition.xyz;
                gl_Position = projectionMatrix * mvPosition;
            }`,
        fragmentShader: `
            uniform vec3 uColor;
            uniform float uIntensity;
            varying vec3 vNormalW;
            varying vec3 vPositionW;
            void main() {
                vec3 viewDir = normalize(-vPositionW);
                float rim = pow(1.0 - abs(dot(viewDir, normalize(vNormalW))), 3.5);
                gl_FragColor = vec4(uColor, rim * uIntensity);
            }`,
        side: THREE.BackSide,
        transparent: true,
        depthWrite: false,
        blending: THREE.AdditiveBlending
    });
    atmosphere = new THREE.Mesh(new THREE.SphereGeometry(EARTH_RADIUS * 1.045, 64, 64), atmosMat);
    scene.add(atmosphere);
    
    // Reference Equator Plane Ring
    const equatorGeo = new THREE.RingGeometry(EARTH_RADIUS + 20, EARTH_RADIUS + 180, 64);
    const equatorMat = new THREE.MeshBasicMaterial({
        color: 0xaaaaaa,
        side: THREE.DoubleSide,
        transparent: true,
        opacity: 0.18
    });
    const equator = new THREE.Mesh(equatorGeo, equatorMat);
    equator.rotation.x = Math.PI / 2;
    scene.add(equator);
    
    // Initial Orbit Line Setup (Cyan neon)
    const orbitMaterial = new THREE.LineBasicMaterial({
        color: 0x555555,
        transparent: true,
        opacity: 0.8
    });
    const orbitPoints = [];
    for (let i = 0; i <= 200; i++) {
        orbitPoints.push(new THREE.Vector3(0, 0, 0));
    }
    const orbitGeo = new THREE.BufferGeometry().setFromPoints(orbitPoints);
    orbitLine = new THREE.Line(orbitGeo, orbitMaterial);
    scene.add(orbitLine);
    
    // Transmission Communication Beam Line (Dotted style laser)
    const beamMat = new THREE.LineBasicMaterial({
        color: 0xaaaaaa,
        transparent: true,
        opacity: 0.35
    });
    const beamGeo = new THREE.BufferGeometry().setFromPoints([
        new THREE.Vector3(0, 0, 0),
        new THREE.Vector3(0, 0, 0)
    ]);
    commBeam = new THREE.Line(beamGeo, beamMat);
    scene.add(commBeam);
    
    satelliteMesh = createSatelliteModel(1.0);
    scene.add(satelliteMesh);
    
    // Setup window resize listener
    window.addEventListener("resize", onWindowResize);
    
    // Kick off animation loop
    animate();
}

function onWindowResize() {
    const container = document.getElementById("canvas-container");
    if (!container || !renderer || !camera) return;
    const width = container.clientWidth;
    const height = container.clientHeight;
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height);
}

function animate() {
    requestAnimationFrame(animate);
    
    if (controls) controls.update();
    
    // Slowly spin the Earth's cyber-grid
    if (earthWireframe) {
        earthWireframe.rotation.y += 0.0003;
    }
    if (earthMesh) {
        earthMesh.rotation.y += 0.0002;
    }
    // Clouds drift independently — the planet visibly *weathers*
    if (cloudMesh) {
        cloudMesh.rotation.y += 0.00031;
        cloudMesh.rotation.x = Math.sin(performance.now() / 90000) * 0.01;
    }
    
    // Propagate satellite along trajectory
    if (satelliteMesh && orbitalParams) {
        // Calculate orbital period
        const periodSec = 2 * Math.PI * Math.sqrt(Math.pow(orbitalParams.a, 3) / MU_EARTH);
        
        // Advance time factor (normalized speed to loop in ~18 seconds)
        satTime += 0.065 * (periodSec / 18);
        
        const M = (satTime % periodSec) * (2 * Math.PI / periodSec);
        const E = solveKepler(M, orbitalParams.e);
        const nu = trueAnomalyFromEccentric(E, orbitalParams.e);
        
        const pos = getCartesianPosition(orbitalParams.a, orbitalParams.e, orbitalParams.i, orbitalParams.raan, orbitalParams.argp, nu);
        satelliteMesh.position.set(pos.x, pos.y, pos.z);
        
        // Keep the high-gain dish locked on Earth, pulse the beacon
        satelliteMesh.lookAt(0, 0, 0);
        if (satelliteMesh.userData.beaconMat) {
            satelliteMesh.userData.beaconMat.emissiveIntensity = 1.0 + Math.sin(performance.now() / 280) * 0.9;
        }
        
        // Draw the communication beam connection from satellite to Earth
        if (commBeam) {
            const beamPoints = [
                new THREE.Vector3(0, 0, 0),
                satelliteMesh.position.clone()
            ];
            commBeam.geometry.dispose();
            commBeam.geometry = new THREE.BufferGeometry().setFromPoints(beamPoints);
        }
        
        // Update Tactical Telemetry Card
        const card = document.getElementById("satellite-telemetry-card");
        if (card && !card.classList.contains("hidden")) {
            const r_mag = Math.sqrt(pos.x*pos.x + pos.y*pos.y + pos.z*pos.z);
            const alt = r_mag - EARTH_RADIUS;
            const vel = Math.sqrt(MU_EARTH * (2/r_mag - 1/orbitalParams.a));
            
            document.getElementById("tele-alt").innerText = alt.toFixed(1) + " km";
            document.getElementById("tele-vel").innerText = vel.toFixed(3) + " km/s";
            document.getElementById("tele-x").innerText = pos.x.toFixed(1);
            document.getElementById("tele-y").innerText = pos.y.toFixed(1);
            document.getElementById("tele-z").innerText = pos.z.toFixed(1);
        }
    }
    
    // Propagate Tactical Constellation
    if (isConstellationMode && constellationGroup.length && renderer) {
        const timeFactor = 0.02; // Global constellation time speed

        // Project labels against the actual WebGL canvas position on screen
        const rect = renderer.domElement.getBoundingClientRect();

        constellationGroup.forEach(c => {
            const periodSec = 2 * Math.PI * Math.sqrt(Math.pow(c.data.a, 3) / MU_EARTH);
            c.nu += (timeFactor * 3600) / periodSec; // Advance true anomaly

            // Get Cartesian Position
            const pos = getCartesianPosition(c.data.a, c.data.e, c.data.i, c.data.raan, c.data.argp, c.nu);
            c.mesh.position.set(pos.x, pos.y, pos.z);

            // 2D Label Projection (canvas-rect aware)
            const vector = new THREE.Vector3(pos.x, pos.y, pos.z);
            vector.project(camera);

            if (vector.z < 1.0) {
                c.labelEl.style.display = 'block';
                const x = rect.left + (vector.x * 0.5 + 0.5) * rect.width;
                const y = rect.top + (-vector.y * 0.5 + 0.5) * rect.height;
                c.labelEl.style.left = `${x}px`;
                c.labelEl.style.top = `${y - 16}px`;
            } else {
                c.labelEl.style.display = 'none'; // Behind camera
            }
        });
    }

    if (renderer && scene && camera) {
        renderer.render(scene, camera);
    }
}

// Update the 3D orbit lines and adjust camera target
function updateThreeJSOrbit(a, e, i, raan, argp) {
    orbitalParams = { a, e, i, raan, argp };
    
    // Compute 200 points on the ellipse
    const points = [];
    const numPoints = 200;
    for (let k = 0; k <= numPoints; k++) {
        const nu = (k / numPoints) * 2 * Math.PI;
        const pos = getCartesianPosition(a, e, i, raan, argp, nu);
        points.push(new THREE.Vector3(pos.x, pos.y, pos.z));
    }
    
    // Swap line geometry
    if (orbitLine) {
        orbitLine.geometry.dispose();
        orbitLine.geometry = new THREE.BufferGeometry().setFromPoints(points);
    }
    
    // Scale camera view based on semi-major axis (a) to keep entire system framed
    if (camera && controls) {
        const currentDist = camera.position.length();
        if (currentDist < a * 1.4 || currentDist > a * 3.5) {
            const range = a * 2.2;
            camera.position.set(range * 0.7, range * 0.7, range * 0.7);
            controls.update();
        }
    }
}


// --- 5. CONVERSATIONAL AI AGENT SEARCH ENGINE ---

function querySecondBrainAgent(userInput) {
    const query = userInput.toLowerCase().trim();
    if (!query) return null;

    // Send the query directly to the APEX-1 Backend API
    return fetch("https://gnss-orbital.onrender.com/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
            message: query,
            language: currentLang
        })
    })
    .then(res => res.json())
    .then(data => {
        return {
            text: data.response,
            doc: "APEX-1 Database",
            agent: "Core Server"
        };
    })
    .catch(error => {
        console.error("Agent error:", error);
        return {
            text: translations[currentLang]["teacher.no_match"] || "SYSTEM ERROR: Backend connection failed.",
            doc: null,
            agent: null
        };
    });
}


// --- 6. CHAT INTERACTIVE INTERFACE ---

// Append a bubble to the chat logger
function appendChatBubble(sender, text, isMarkdown = false) {
    const messagesContainer = document.getElementById("chat-messages");
    if (!messagesContainer) return;
    
    const bubble = document.createElement("div");
    bubble.className = `chat-bubble ${sender}`;
    
    const avatar = document.createElement("div");
    avatar.className = "bubble-avatar";
    avatar.innerText = sender === "bot" ? "◈" : "⚇";
    
    const content = document.createElement("div");
    content.className = "bubble-content";
    
    if (isMarkdown) {
        content.innerHTML = marked.parse(text);
    } else {
        content.innerText = text;
    }
    
    bubble.appendChild(avatar);
    bubble.appendChild(content);
    messagesContainer.appendChild(bubble);
    
    // Auto-scroll
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
    
    return bubble;
}

// Show a glowing typing indicator while agent processes
function showTypingIndicator() {
    const messagesContainer = document.getElementById("chat-messages");
    if (!messagesContainer) return null;
    
    const bubble = document.createElement("div");
    bubble.className = "chat-bubble bot typing-indicator-bubble";
    
    const avatar = document.createElement("div");
    avatar.className = "bubble-avatar";
    avatar.innerText = "◈";
    
    const content = document.createElement("div");
    content.className = "bubble-content";
    content.innerHTML = `
        <div class="typing-indicator">
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
            <div class="typing-dot"></div>
        </div>
    `;
    
    bubble.appendChild(avatar);
    bubble.appendChild(content);
    messagesContainer.appendChild(bubble);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
    
    return bubble;
}

// Sync the living core, the status dot and the status text with one call
function setAgentState(state) {
    // state: idle | listening | thinking | speaking
    if (window.ApexOrb) ApexOrb.setState(state);

    const dict = translations[currentLang];
    const textKey = state === "idle" ? "agent.status.online" : `agent.status.${state}`;
    const textEl = document.getElementById("agent-status-text");
    if (textEl && dict[textKey]) textEl.innerText = dict[textKey];

    const dot = document.getElementById("agent-status-dot");
    if (dot) dot.setAttribute("data-state", state);
}

// Render markdown + LaTeX: math spans are shielded from the markdown parser,
// then typeset with KaTeX so $...$ and $$...$$ display as real equations
function renderRichContent(el, text) {
    const mathBlocks = [];
    const processed = text
        .replace(/\$\$([\s\S]+?)\$\$/g, (m, expr) => {
            mathBlocks.push({ expr: expr, display: true });
            return `%%MATH${mathBlocks.length - 1}%%`;
        })
        .replace(/\$([^$\n]+?)\$/g, (m, expr) => {
            mathBlocks.push({ expr: expr, display: false });
            return `%%MATH${mathBlocks.length - 1}%%`;
        });

    let html = marked.parse(processed);
    if (mathBlocks.length) {
        html = html.replace(/%%MATH(\d+)%%/g, (m, i) => {
            const b = mathBlocks[Number(i)];
            if (window.katex) {
                try {
                    return katex.renderToString(b.expr, { displayMode: b.display, throwOnError: false });
                } catch (e) { /* fall through to raw TeX */ }
            }
            return `<code>${b.expr}</code>`;
        });
    }
    el.innerHTML = html;
}

// Reveal a bot reply block-by-block while the core "transmits".
// When a sub-agent answered, a routing tag credits the specialist.
function revealBotMessage(text, isMarkdown, onDone, agent) {
    const bubble = appendChatBubble("bot", "");
    if (!bubble) { if (onDone) onDone(); return; }
    const content = bubble.querySelector(".bubble-content");
    const messagesContainer = document.getElementById("chat-messages");

    if (agent) {
        const tag = document.createElement("div");
        tag.className = "route-tag";
        tag.style.setProperty("--agent-color", agent.color || "#6fd3e7");
        const agentName = (agent.name && (agent.name[currentLang] || agent.name.en)) || agent.id;
        tag.innerHTML = `<span class="route-icon">${agent.icon || "◈"}</span>` +
            `<span>${translations[currentLang]["brain.routed"] || "ROUTED VIA"}</span>` +
            `<strong>${agent.id} · ${agentName}</strong>`;
        messagesContainer.insertBefore(tag, bubble);
    }

    if (isMarkdown) {
        renderRichContent(content, text);
        const blocks = Array.from(content.children);
        if (blocks.length === 0) { if (onDone) onDone(); return; }
        blocks.forEach(b => b.classList.add("reveal-pending"));

        let idx = 0;
        const timer = setInterval(() => {
            if (idx >= blocks.length) {
                clearInterval(timer);
                if (onDone) onDone();
                return;
            }
            blocks[idx].classList.remove("reveal-pending");
            blocks[idx].classList.add("reveal-in");
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
            idx++;
        }, 170);
    } else {
        // Plain text: character typewriter
        let pos = 0;
        const timer = setInterval(() => {
            pos = Math.min(pos + 2, text.length);
            content.innerText = text.slice(0, pos);
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
            if (pos >= text.length) {
                clearInterval(timer);
                if (onDone) onDone();
            }
        }, 18);
    }
}

function handleUserMessageSubmit() {
    const inputField = document.getElementById("chat-input");
    if (!inputField) return;

    const message = inputField.value.trim();
    if (!message) return;

    // 1. Log user message
    appendChatBubble("user", message);
    inputField.value = "";

    // 2. The core thinks: turbulent state + typing indicator
    setAgentState("thinking");
    const typingBubble = showTypingIndicator();

    // 3. Process search, then transmit the reply progressively
    setTimeout(async () => {
        if (typingBubble) typingBubble.remove();

        const response = await querySecondBrainAgent(message);
        if (!response) { setAgentState("idle"); return; }

        let fullReplyText;
        if (response.doc) {
            const intro = translations[currentLang]["teacher.reply_intro"].replace("{document}", response.doc);
            fullReplyText = `${intro}\n\n---\n\n${response.text}`;
            // A successful find makes the core visibly happy
            if (window.ApexOrb && ApexOrb.emote) ApexOrb.emote("happy");
        } else {
            fullReplyText = response.text;
        }

        setAgentState("speaking");
        revealBotMessage(fullReplyText, true, () => setAgentState("idle"), response.agent);
    }, 900);
}


// --- 7. INTERACTIVE WIDGETS & UI HANDLERS ---

function updatePlot() {
    const a = parseFloat(document.getElementById("slider-a").value);
    const e = parseFloat(document.getElementById("slider-e").value);
    const i = parseFloat(document.getElementById("slider-i").value);
    const raan = parseFloat(document.getElementById("slider-raan").value);
    const argp = parseFloat(document.getElementById("slider-argp").value);
    
    // Validate perigee intersection with Earth
    const perigee_alt = a * (1.0 - e) - EARTH_RADIUS;
    const apogee_alt = a * (1.0 + e) - EARTH_RADIUS;
    
    const warningBox = document.getElementById("subsurface-warning");
    if (perigee_alt < 0) {
        warningBox.classList.remove("hidden");
        document.getElementById("warning-text").innerText = translations[currentLang]["warning.subsurface"].replace("{radius}", EARTH_RADIUS.toFixed(0));
        
        // Hide satellite and communication laser from crashing
        if (satelliteMesh) satelliteMesh.visible = false;
        if (commBeam) commBeam.visible = false;
        return;
    } else {
        warningBox.classList.add("hidden");
        if (satelliteMesh) satelliteMesh.visible = true;
        if (commBeam) commBeam.visible = true;
    }
    
    // Update WebGL Scene
    updateThreeJSOrbit(a, e, i, raan, argp);
    
    // Update physical metrics
    const periodSec = 2 * Math.PI * Math.sqrt(Math.pow(a, 3) / MU_EARTH);
    document.getElementById("metric-period").innerText = `${(periodSec / 3600).toFixed(2)} hrs`;
    document.getElementById("metric-perigee").innerText = `${perigee_alt.toFixed(0)} km`;
    document.getElementById("metric-apogee").innerText = `${apogee_alt.toFixed(0)} km`;
}

// Localization Updater
function updateLocalization() {
    const dict = translations[currentLang];
    
    // Update simple translations
    document.querySelectorAll("[data-i18n]").forEach(elem => {
        const key = elem.getAttribute("data-i18n");
        if (dict[key]) {
            elem.innerText = dict[key];
        }
    });
    
    // Update dynamic placeholders
    const chatInput = document.getElementById("chat-input");
    if (chatInput && dict["brain.placeholder"]) {
        chatInput.placeholder = dict["brain.placeholder"];
    }
}

// Reset chat log with localized welcome message (typed out by the core)
function resetChatWelcome() {
    const messagesContainer = document.getElementById("chat-messages");
    if (!messagesContainer) return;

    messagesContainer.innerHTML = "";
    setAgentState("speaking");
    revealBotMessage(translations[currentLang]["brain.welcome"], false, () => setAgentState("idle"));
}

// Navigation Tabs Switcher
document.querySelectorAll(".nav-item").forEach(btn => {
    btn.addEventListener("click", () => {
        document.querySelectorAll(".nav-item").forEach(item => item.classList.remove("active"));
        document.querySelectorAll(".tab-pane").forEach(pane => pane.classList.remove("active"));
        
        btn.classList.add("active");
        const tab = btn.getAttribute("data-tab");
        document.getElementById(`tab-${tab}`).classList.add("active");
        
        const bgCanvas = document.getElementById("bg-canvas");
        const canvasContainer = document.getElementById("canvas-container");

        if (tab === "brain") {
            // Dim ambient layers so the living core owns the stage
            if (bgCanvas) bgCanvas.style.opacity = "0.35";
            if (canvasContainer) canvasContainer.style.opacity = "0";
            // The orb initialized while hidden (0x0): re-measure now that it is visible
            if (window.ApexOrb) setTimeout(() => ApexOrb.resize(), 60);
        } else {
            if (bgCanvas) bgCanvas.style.opacity = "1";
            if (canvasContainer) canvasContainer.style.opacity = "1";
        }

        // Trigger resize on WebGL canvas when Simulator becomes visible to avoid black areas
        if (tab === "simulator") {
            setTimeout(() => {
                onWindowResize();
                updatePlot();
            }, 60);
        }

        if (tab === "jupyter") {
            checkJupyterStatus();
            startJupyterPolling();
        }
    });
});

// Setup Slider Listeners
["slider-a", "slider-e", "slider-i", "slider-raan", "slider-argp"].forEach(id => {
    document.getElementById(id).addEventListener("input", (e) => {
        const shortId = id.replace("slider-", "");
        document.getElementById(`val-${shortId}`).innerText = e.target.value;
        
        // Deactivate active preset button
        document.querySelectorAll(".btn-preset").forEach(btn => btn.classList.remove("active"));
        document.getElementById("preset-custom").classList.add("active");
        
        updatePlot();
    });
});

// Setup Preset Button Listeners
document.querySelectorAll(".btn-preset").forEach(btn => {
    btn.addEventListener("click", () => {
        document.querySelectorAll(".btn-preset").forEach(item => item.classList.remove("active"));
        btn.classList.add("active");
        
        const type = btn.getAttribute("data-preset");
        if (type === "custom") return;
        
        const presets = {
            leo: { a: 6779, e: 0.0006, i: 51.6, raan: 0, argp: 0 },
            meo: { a: 26571, e: 0.01, i: 55.0, raan: 0, argp: 0 },
            geo: { a: 42164, e: 0.0001, i: 0.01, raan: 0, argp: 0 },
            heo: { a: 26560, e: 0.74, i: 63.4, raan: 0, argp: 270 }
        };
        
        const p = presets[type];
        Object.keys(p).forEach(key => {
            const slider = document.getElementById(`slider-${key}`);
            slider.value = p[key];
            document.getElementById(`val-${key}`).innerText = p[key];
        });
        
        updatePlot();
    });
});

// Language Select Change
function handleLanguageChange(e) {
    currentLang = e.target.value;
    updateLocalization();
    updatePlot();
    resetChatWelcome();
    renderSuggestionChips();
    renderNotebookGrid();
    setAgentState(window.ApexOrb ? ApexOrb.getState() : "idle");
    const btnConst = document.getElementById("btn-constellation");
    if(btnConst) btnConst.onclick = toggleConstellation;
    
    // Sync other select if present
    const otherId = e.target.id === 'lang-select' ? 'lang-select-mobile' : 'lang-select';
    const otherEl = document.getElementById(otherId);
    if (otherEl && otherEl.value !== e.target.value) {
        otherEl.value = e.target.value;
    }
}

const mainLangSelect = document.getElementById("lang-select");
if (mainLangSelect) mainLangSelect.addEventListener('change', handleLanguageChange);

const mobileLangSelect = document.getElementById("lang-select-mobile");
if (mobileLangSelect) mobileLangSelect.addEventListener('change', handleLanguageChange);

// Chatbot Event Listeners
document.getElementById("btn-chat-send").onclick = handleUserMessageSubmit;
document.getElementById("chat-input").onkeypress = (e) => {
    if (e.key === "Enter") {
        handleUserMessageSubmit();
    }
};

// The core listens while you type: focus drives the listening state
const chatInputEl = document.getElementById("chat-input");
if (chatInputEl) {
    chatInputEl.addEventListener("focus", () => {
        if (window.ApexOrb && ApexOrb.getState() === "idle") setAgentState("listening");
    });
    chatInputEl.addEventListener("blur", () => {
        if (window.ApexOrb && ApexOrb.getState() === "listening") setAgentState("idle");
    });
}


function renderSuggestionChips() {
    const container = document.getElementById("suggestion-chips");
    if (!container) return;
    container.innerHTML = "";
    for (let i = 1; i <= 4; i++) {
        const text = translations[currentLang][`topics.${i}`];
        if (text) {
            const chip = document.createElement("div");
            chip.className = "chip";
            chip.innerText = text;
            chip.onclick = () => {
                const input = document.getElementById("chat-input");
                if (input) {
                    input.value = text;
                    handleUserMessageSubmit();
                }
            };
            container.appendChild(chip);
        }
    }
}

// Window Initializer
window.onload = () => {
    updateLocalization();
    renderSuggestionChips();
    const btnConst = document.getElementById("btn-constellation");
    if(btnConst) btnConst.onclick = toggleConstellation;
    initBackgroundThreeJS();
    if (window.ApexOrb) ApexOrb.init("orb-container");
    if (window.AgentNetwork) AgentNetwork.init();
    initThreeJS();
    initJupyterConsole();
    updatePlot();
    resetChatWelcome();
};


function clearConstellation() {
    constellationGroup.forEach(c => {
        scene.remove(c.mesh);
        scene.remove(c.line);
        c.mesh.geometry.dispose();
        c.mesh.material.dispose();
        c.line.geometry.dispose();
        c.line.material.dispose();
    });
    constellationGroup = [];
}

function toggleConstellation() {
    isConstellationMode = !isConstellationMode;
    const labelsContainer = document.getElementById("labels-container");
    labelsContainer.innerHTML = "";

    const controlsCard = document.querySelector(".controls-card");
    const btn = document.getElementById("btn-constellation");

    if (isConstellationMode) {
        // Hide the single-orbit actors
        if (satelliteMesh) satelliteMesh.visible = false;
        if (orbitLine) orbitLine.visible = false;
        if (commBeam) commBeam.visible = false;
        if (controlsCard) controlsCard.style.opacity = "0.25";
        if (btn) btn.innerText = "◈ EXIT MULTI-ORBIT";

        // Reference constellation: one of each orbital regime, color-coded
        const sats = [
            { name: "ISS (LEO)",  a: EARTH_RADIUS + 420,   e: 0.0006, i: 51.6,  argp: 0,   raan: 0,   color: 0xeaf6ff },
            { name: "STARLINK-1", a: EARTH_RADIUS + 550,   e: 0.0001, i: 53.0,  argp: 0,   raan: 45,  color: 0x8fb8d8 },
            { name: "STARLINK-2", a: EARTH_RADIUS + 550,   e: 0.0001, i: 53.0,  argp: 0,   raan: 105, color: 0x8fb8d8 },
            { name: "GPS-III",    a: EARTH_RADIUS + 20200, e: 0.01,   i: 55.0,  argp: 0,   raan: 0,   color: 0x57c99b },
            { name: "GPS-III-B",  a: EARTH_RADIUS + 20200, e: 0.01,   i: 55.0,  argp: 0,   raan: 120, color: 0x57c99b },
            { name: "GALILEO",    a: EARTH_RADIUS + 23222, e: 0.0001, i: 56.0,  argp: 0,   raan: 200, color: 0xf0b429 },
            { name: "BEIDOU-3",   a: EARTH_RADIUS + 21528, e: 0.005,  i: 55.0,  argp: 0,   raan: 280, color: 0xd97f5a },
            { name: "GEO-COM",    a: 42164,                e: 0.0001, i: 0.01,  argp: 0,   raan: 0,   color: 0xff6b6b },
            { name: "MOLNIYA",    a: 26561,                e: 0.74,   i: 63.4,  argp: 270, raan: 45,  color: 0x8d87d8 }
        ];

        // Frame the whole system: pull the camera out past the largest apogee
        const maxApogee = Math.max(...sats.map(s => s.a * (1 + s.e)));
        if (camera && controls) {
            const d = maxApogee * 1.15;
            camera.position.set(d * 0.85, d * 0.5, d * 0.85);
            controls.update();
        }

        clearConstellation();

        sats.forEach(s => {
            // Glowing marker sphere (reads as a satellite at any zoom)
            const mesh = new THREE.Mesh(
                new THREE.SphereGeometry(520, 16, 16),
                new THREE.MeshBasicMaterial({ color: s.color })
            );
            scene.add(mesh);

            // Orbit line traced with the SAME transform as the satellite itself,
            // so line and marker can never disagree (the old rotation.set bug)
            const points = [];
            const N = 256;
            for (let k = 0; k <= N; k++) {
                const nu = (k / N) * Math.PI * 2;
                const p = getCartesianPosition(s.a, s.e, s.i, s.raan, s.argp, nu);
                points.push(new THREE.Vector3(p.x, p.y, p.z));
            }
            const line = new THREE.Line(
                new THREE.BufferGeometry().setFromPoints(points),
                new THREE.LineBasicMaterial({ color: s.color, transparent: true, opacity: 0.75 })
            );
            scene.add(line);

            // Floating name label, tinted like its orbit
            const label = document.createElement('div');
            label.className = 'satellite-label';
            label.innerText = s.name;
            const css = '#' + s.color.toString(16).padStart(6, '0');
            label.style.color = css;
            label.style.borderColor = css;
            labelsContainer.appendChild(label);

            constellationGroup.push({
                data: s,
                mesh: mesh,
                line: line,
                labelEl: label,
                nu: Math.random() * Math.PI * 2 // random starting anomaly
            });
        });

    } else {
        // Restore single mode
        if (satelliteMesh) satelliteMesh.visible = true;
        if (orbitLine) orbitLine.visible = true;
        if (commBeam) commBeam.visible = true;
        if (controlsCard) controlsCard.style.opacity = "1";
        if (btn) btn.innerText = translations[currentLang]["ctrl.constellation"] || "◈ MULTI-ORBIT VIEW";

        clearConstellation();
        updatePlot();
    }
}


// --- 8. JUPYTER RESEARCH CONSOLE ---

const JUPYTER_BASE = "http://localhost:8888";
const NOTEBOOKS = [
    { id: "01", file: "notebooks/01_interactive_orbits.ipynb", badge: "bronze" },
    { id: "02", file: "notebooks/02_kepler_equation.ipynb", badge: "silver" },
    { id: "03", file: "notebooks/03_iris2_constellation.ipynb", badge: "master" }
];
let jupyterOnline = false;

function renderNotebookGrid() {
    const grid = document.getElementById("notebook-grid");
    if (!grid) return;
    const dict = translations[currentLang];
    grid.innerHTML = "";

    NOTEBOOKS.forEach((nb, idx) => {
        const card = document.createElement("div");
        card.className = "glass-card notebook-card";
        card.style.animationDelay = `${idx * 0.08}s`;
        card.innerHTML = `
            <div class="nb-top-row">
                <span class="nb-index">${nb.id}</span>
                <span class="nb-badge nb-badge-${nb.badge}">${dict["nb.badge." + nb.badge] || nb.badge}</span>
            </div>
            <h3 class="nb-title">${dict["nb." + nb.id + ".title"] || nb.file}</h3>
            <p class="nb-desc">${dict["nb." + nb.id + ".desc"] || ""}</p>
            <div class="nb-footer">
                <code class="nb-file">${nb.file}</code>
                <button class="btn-open-nb">${dict["jupyter.open"] || "OPEN"} ▸</button>
            </div>`;
        card.querySelector(".btn-open-nb").onclick = () => openNotebook(nb);
        grid.appendChild(card);
    });
}

function updateJupyterStatusUI(state) {
    // state: checking | online | offline
    const dict = translations[currentLang];
    const dot = document.getElementById("jupyter-status-dot");
    const text = document.getElementById("jupyter-status-text");
    const help = document.getElementById("jupyter-offline-help");
    if (dot) dot.setAttribute("data-state", state);
    if (text) text.innerText = dict["jupyter.status." + state] || state.toUpperCase();
    if (help) help.classList.toggle("hidden", state !== "offline");
}

function checkJupyterStatus() {
    updateJupyterStatusUI("checking");
    const controller = new AbortController();
    const timeout = setTimeout(() => controller.abort(), 2500);

    // no-cors probe: resolves (opaque) if a server answers, rejects if the port is closed
    fetch(JUPYTER_BASE + "/api", { mode: "no-cors", signal: controller.signal })
        .then(() => {
            jupyterOnline = true;
            updateJupyterStatusUI("online");
        })
        .catch(() => {
            jupyterOnline = false;
            updateJupyterStatusUI("offline");
        })
        .finally(() => clearTimeout(timeout));
}

function openNotebook(nb) {
    const url = `${JUPYTER_BASE}/lab/tree/${nb.file}`;
    if (jupyterOnline) {
        const iframe = document.getElementById("jupyter-iframe");
        const title = document.getElementById("jupyter-embed-title");
        const external = document.getElementById("jupyter-external-link");
        if (iframe) iframe.src = url;
        if (title) title.innerText = nb.file.split("/").pop();
        if (external) external.href = url;
        document.getElementById("jupyter-launcher").classList.add("hidden");
        document.getElementById("jupyter-embed").classList.remove("hidden");
    } else {
        // No kernel: opening a dead tab helps nobody. Mission-control rule:
        // tell the operator exactly what to run, then auto-connect for them.
        const dict = translations[currentLang];
        const text = document.getElementById("jupyter-status-text");
        if (text) text.innerText = dict["jupyter.need_kernel"] || "KERNEL REQUIRED — RUN THE COMMAND BELOW";

        const help = document.getElementById("jupyter-offline-help");
        if (help) {
            help.classList.remove("hidden");
            help.classList.remove("flash-attention");
            void help.offsetWidth; // restart the CSS animation
            help.classList.add("flash-attention");
            help.scrollIntoView({ behavior: "smooth", block: "center" });
        }
        startJupyterPolling();
    }
}

// Ops-grade auto-connect: while the console tab is open and the kernel is
// down, probe every 4 s; the moment JupyterLab comes up the status flips
// green and OPEN NOTEBOOK embeds it — no manual rescan needed.
let jupyterPollTimer = null;
function startJupyterPolling() {
    if (jupyterPollTimer) return;
    jupyterPollTimer = setInterval(() => {
        const pane = document.getElementById("tab-jupyter");
        if (!pane || !pane.classList.contains("active") || jupyterOnline) {
            clearInterval(jupyterPollTimer);
            jupyterPollTimer = null;
            return;
        }
        checkJupyterStatus();
    }, 4000);
}

function initJupyterConsole() {
    renderNotebookGrid();

    const recheck = document.getElementById("btn-jupyter-recheck");
    if (recheck) recheck.onclick = checkJupyterStatus;

    const back = document.getElementById("btn-jupyter-back");
    if (back) back.onclick = () => {
        document.getElementById("jupyter-embed").classList.add("hidden");
        document.getElementById("jupyter-launcher").classList.remove("hidden");
        const iframe = document.getElementById("jupyter-iframe");
        if (iframe) iframe.src = "about:blank";
    };

    const copyBtn = document.getElementById("btn-copy-cmd");
    if (copyBtn) copyBtn.onclick = () => {
        const cmd = document.getElementById("jupyter-cmd");
        if (!cmd) return;
        navigator.clipboard.writeText(cmd.innerText).then(() => {
            copyBtn.innerText = translations[currentLang]["jupyter.copied"] || "COPIED";
            setTimeout(() => {
                copyBtn.innerText = translations[currentLang]["jupyter.copy"] || "COPY";
            }, 1600);
        });
    };
}

// Global initialization
document.addEventListener("DOMContentLoaded", () => {
    // Hide warning boxes initially if they shouldn't be visible
    document.querySelectorAll('.warning-box').forEach(box => {
        if (!box.classList.contains('hidden')) {
            box.classList.add('hidden');
        }
    });

    // Sidebar Toggle Logic
    const sidebarToggleBtn = document.getElementById("sidebar-toggle");
    const sidebar = document.querySelector(".sidebar");
    if (sidebarToggleBtn && sidebar) {
        sidebarToggleBtn.addEventListener("click", () => {
            sidebar.classList.toggle("collapsed");
        });
    }

    // Language selector setup
    const langSelect = document.getElementById("lang-select");
    if (langSelect) {
        langSelect.addEventListener("change", (e) => {
            setLanguage(e.target.value);
        });
    }
});
