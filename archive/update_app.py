import os

file_path = r'c:\Users\invde\OneDrive\Documents\gnss-orbital-py\frontend\app.js'

with open(file_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update Translations
code = code.replace(
    '"brain.send": "Send",',
    '''"brain.send": "Send",
        "brain.welcome": "Greetings. I am APEX-1. Orbital database synced.",
        "topics.1": "How does Hohmann Transfer work?",
        "topics.2": "What is J2 perturbation?",
        "topics.3": "Explain GPS vs Galileo",
        "topics.4": "Difference between ECI and ECEF",'''
)
code = code.replace(
    '"brain.send": "Enviar",',
    '''"brain.send": "Enviar",
        "brain.welcome": "Saludos. Soy APEX-1. Base de datos orbital sincronizada.",
        "topics.1": "¿Cómo funciona la transferencia de Hohmann?",
        "topics.2": "¿Qué es la perturbación J2?",
        "topics.3": "Explicar GPS vs Galileo",
        "topics.4": "Diferencia entre marcos ECI y ECEF",'''
)
code = code.replace(
    '"brain.send": "发送",',
    '''"brain.send": "发送",
        "brain.welcome": "您好。我是 APEX-1。轨道数据库已同步。",
        "topics.1": "霍曼转移是如何工作的？",
        "topics.2": "什么是J2摄动？",
        "topics.3": "解释 GPS 与 伽利略",
        "topics.4": "地心惯性系 (ECI) 与地固系 (ECEF) 的区别",'''
)

# 2. Add Raycaster and Moon Globals
ray_globals = '''let satTime = 0; // Simulated time tracker for orbits

// Raycaster & Moon Globals
let raycaster = new THREE.Raycaster();
let mouse = new THREE.Vector2();
let moonMesh;
let earthMat; // make earthMat accessible if needed
'''
code = code.replace('let satTime = 0; // Simulated time tracker for orbits', ray_globals)

# 3. Add Moon and adjust camera in initThreeJS
init_scene = '''    // Scene Setup
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 1000000); // Increased FAR to see Moon
    camera.position.set(20000, 15000, 20000);
    
    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(container.clientWidth, container.clientHeight);
    container.appendChild(renderer.domElement);
    
    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;
    controls.maxDistance = 800000; // Increased to allow zooming to the Moon'''
    
code = code.replace(
'''    // Scene Setup
    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(45, container.clientWidth / container.clientHeight, 0.1, 100000);
    camera.position.set(20000, 15000, 20000);
    
    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(container.clientWidth, container.clientHeight);
    container.appendChild(renderer.domElement);
    
    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.dampingFactor = 0.05;
    controls.maxDistance = 80000;''',
init_scene
)

# 4. Earth Grayscale Texture and Moon Mesh
texture_loading_code_old = '''    // Load NASA photorealistic Earth texture map
    const textureLoader = new THREE.TextureLoader();
    textureLoader.load(
        'https://raw.githubusercontent.com/mrdoob/three.js/master/examples/textures/planets/earth_atmos_2048.jpg',
        (texture) => {
            earthMat.map = texture;
            earthMat.color.setHex(0xffffff); // resetting to show texture maps
            earthMat.emissive.setHex(0x000000);
            earthMat.needsUpdate = true;
        },
        null,
        (error) => {
            console.log("Earth texture failed to load, keeping cybernetic fallback.");
        }
    );'''

texture_loading_code_new = '''    // The Moon Setup
    const moonGeo = new THREE.SphereGeometry(1737, 32, 32);
    const moonMat = new THREE.MeshPhongMaterial({ color: 0x888888, emissive: 0x111111 });
    moonMesh = new THREE.Mesh(moonGeo, moonMat);
    // Earth-Moon distance is 384,400 km
    moonMesh.position.set(384400, 0, 0); 
    scene.add(moonMesh);

    // Load NASA photorealistic Earth texture map and apply Palantir Grayscale filter
    const textureLoader = new THREE.TextureLoader();
    textureLoader.load(
        'https://raw.githubusercontent.com/mrdoob/three.js/master/examples/textures/planets/earth_atmos_2048.jpg',
        (texture) => {
            const img = texture.image;
            const canvas = document.createElement('canvas');
            canvas.width = img.width;
            canvas.height = img.height;
            const ctx = canvas.getContext('2d');
            ctx.drawImage(img, 0, 0);
            
            const imgData = ctx.getImageData(0, 0, canvas.width, canvas.height);
            const data = imgData.data;
            for (let i = 0; i < data.length; i += 4) {
                const avg = 0.2126 * data[i] + 0.7152 * data[i+1] + 0.0722 * data[i+2];
                const contrast = (avg > 128) ? avg * 1.1 : avg * 0.9;
                data[i] = contrast;
                data[i+1] = contrast;
                data[i+2] = contrast;
            }
            ctx.putImageData(imgData, 0, 0);
            
            const bwTexture = new THREE.CanvasTexture(canvas);
            earthMat.map = bwTexture;
            earthMat.color.setHex(0xffffff);
            earthMat.emissive.setHex(0x111111);
            earthMat.needsUpdate = true;
        },
        null,
        (error) => {
            console.log("Earth texture failed to load, keeping fallback.");
        }
    );
    
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
    });'''
code = code.replace(texture_loading_code_old, texture_loading_code_new)

# 5. Make cyber elements Palantir stark
code = code.replace('color: 0x00ffcc,', 'color: 0x555555,')
code = code.replace('color: 0x00ccff,', 'color: 0x222222,')
code = code.replace('color: 0x00a8ff,', 'color: 0xaaaaaa,')

# NASA Gold -> Silver/Grey
code = code.replace('color: 0xffd700,', 'color: 0xdddddd,')
code = code.replace('emissive: 0x221a00,', 'emissive: 0x222222,')
# Solar Panels -> Dark
code = code.replace('color: 0x0088ff,', 'color: 0x444444,')
code = code.replace('emissive: 0x001133,', 'emissive: 0x111111,')


# 6. Update Telemetry data in animate loop
animate_old = '''        // Draw the communication beam connection from satellite to Earth
        if (commBeam) {
            const beamPoints = [
                new THREE.Vector3(0, 0, 0),
                satelliteMesh.position.clone()
            ];
            commBeam.geometry.dispose();
            commBeam.geometry = new THREE.BufferGeometry().setFromPoints(beamPoints);
        }'''
animate_new = animate_old + '''
        
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
        }'''
code = code.replace(animate_old, animate_new)

# 7. Add Suggestion Chips rendering to window.onload
load_old = '''// Window Initializer
window.onload = () => {
    updateLocalization();'''
load_new = '''
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
    renderSuggestionChips();'''
code = code.replace(load_old, load_new)

lang_change_old = '''// Language Select Change
document.getElementById("lang-select").onchange = (e) => {
    currentLang = e.target.value;
    updateLocalization();
    updatePlot();
    resetChatWelcome();
};'''

lang_change_new = '''// Language Select Change
document.getElementById("lang-select").onchange = (e) => {
    currentLang = e.target.value;
    updateLocalization();
    updatePlot();
    resetChatWelcome();
    renderSuggestionChips();
};'''
code = code.replace(lang_change_old, lang_change_new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Rewrite complete.")
