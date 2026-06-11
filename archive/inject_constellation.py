import os

ROOT = r'c:\Users\invde\OneDrive\Documents\gnss-orbital-py\frontend'
index_file = os.path.join(ROOT, 'index.html')
app_file = os.path.join(ROOT, 'js', 'app.js')
css_file = os.path.join(ROOT, 'css', 'style.css')

# 1. Update index.html
with open(index_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Inject Labels Container and Button
labels_container = '<div id="labels-container" style="position: absolute; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:10;"></div>'
if 'id="labels-container"' not in html:
    html = html.replace('<!-- Cybernetic Scanline Overlay for 2050 Hologram Feel -->', f'{labels_container}\n    <!-- Cybernetic Scanline Overlay for 2050 Hologram Feel -->')

btn_html = '<button id="btn-constellation" class="preset-btn" style="width:100%; margin-top: 15px; border-color: var(--text-primary); color: var(--text-primary);">⚡ TACTICAL CONSTELLATION</button>'
if 'id="btn-constellation"' not in html:
    html = html.replace('<button id="btn-propagate" class="btn-primary"', f'{btn_html}\n                            <button id="btn-propagate" class="btn-primary"')

with open(index_file, 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update style.css
css_injection = '''
/* Holographic Satellite Label */
.satellite-label {
    position: absolute;
    color: var(--text-primary);
    font-family: var(--font-mono);
    font-size: 10px;
    letter-spacing: 1px;
    transform: translate(-50%, -100%);
    padding-bottom: 8px;
    text-shadow: 0 0 4px rgba(0,0,0,1);
    pointer-events: none;
    text-transform: uppercase;
}
.satellite-label::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    width: 1px;
    height: 8px;
    background: var(--text-primary);
    transform: translateX(-50%);
}
'''
with open(css_file, 'a', encoding='utf-8') as f:
    f.write(css_injection)

# 3. Update app.js
with open(app_file, 'r', encoding='utf-8') as f:
    app_js = f.read()

# Add Globals
if 'let isConstellationMode = false;' not in app_js:
    app_js = app_js.replace('let satTime = 0;', 'let satTime = 0;\nlet isConstellationMode = false;\nlet constellationGroup = [];\n')

# Toggle Constellation Function
constellation_fn = '''
function toggleConstellation() {
    isConstellationMode = !isConstellationMode;
    const container = document.getElementById("labels-container");
    container.innerHTML = "";
    
    if (isConstellationMode) {
        // Hide single orbit controls & mesh
        satelliteMesh.visible = false;
        orbitLine.visible = false;
        if(commBeam) commBeam.visible = false;
        document.getElementById("orbital-controls").style.opacity = "0.2";
        document.getElementById("btn-constellation").innerText = "❌ DISABLE CONSTELLATION";
        
        // Build Constellation Data
        const sats = [
            { name: "ISS (LEO)", a: EARTH_RADIUS + 400, e: 0.0006, i: 51.6, argp: 0, raan: 0, color: 0xffffff },
            { name: "STARLINK-1", a: EARTH_RADIUS + 550, e: 0.0001, i: 53.0, argp: 0, raan: 45, color: 0xaaaaaa },
            { name: "STARLINK-2", a: EARTH_RADIUS + 550, e: 0.0001, i: 53.0, argp: 0, raan: 90, color: 0xaaaaaa },
            { name: "GPS-IIR-1", a: EARTH_RADIUS + 20200, e: 0.01, i: 55.0, argp: 0, raan: 0, color: 0x00ffcc },
            { name: "GPS-IIR-2", a: EARTH_RADIUS + 20200, e: 0.01, i: 55.0, argp: 120, raan: 0, color: 0x00ffcc },
            { name: "GPS-IIR-3", a: EARTH_RADIUS + 20200, e: 0.01, i: 55.0, argp: 240, raan: 0, color: 0x00ffcc },
            { name: "GALILEO-1", a: EARTH_RADIUS + 23222, e: 0.0001, i: 56.0, argp: 0, raan: 120, color: 0xffaa00 },
            { name: "GEO-SAT-1", a: 42164, e: 0.0001, i: 0.01, argp: 0, raan: 0, color: 0xff5555 },
            { name: "MOLNIYA-1", a: 26561, e: 0.74, i: 63.4, argp: 270, raan: 45, color: 0x5555ff }
        ];
        
        constellationGroup.forEach(c => {
            scene.remove(c.mesh);
            scene.remove(c.line);
        });
        constellationGroup = [];
        
        sats.forEach(s => {
            // Mesh
            const satGeo = new THREE.BoxGeometry(100, 100, 100); // slightly bigger for visibility
            const satMat = new THREE.MeshPhongMaterial({ color: s.color, emissive: 0x222222 });
            const mesh = new THREE.Mesh(satGeo, satMat);
            scene.add(mesh);
            
            // Orbit Line
            const points = [];
            for (let theta = 0; theta <= Math.PI * 2; theta += 0.05) {
                const r = (s.a * (1 - s.e*s.e)) / (1 + s.e * Math.cos(theta));
                const x = r * Math.cos(theta);
                const y = r * Math.sin(theta);
                points.push(new THREE.Vector3(x, y, 0));
            }
            const lineGeo = new THREE.BufferGeometry().setFromPoints(points);
            const lineMat = new THREE.LineBasicMaterial({ color: s.color, transparent: true, opacity: 0.3 });
            const line = new THREE.Line(lineGeo, lineMat);
            
            // Rotate orbit line by i, raan, argp
            const i_rad = s.i * Math.PI / 180;
            const raan_rad = s.raan * Math.PI / 180;
            const argp_rad = s.argp * Math.PI / 180;
            line.rotation.set(i_rad, raan_rad, argp_rad, 'ZYX');
            scene.add(line);
            
            // HTML Label
            const label = document.createElement('div');
            label.className = 'satellite-label';
            label.innerText = s.name;
            container.appendChild(label);
            
            // Save state
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
        satelliteMesh.visible = true;
        orbitLine.visible = true;
        if(commBeam) commBeam.visible = true;
        document.getElementById("orbital-controls").style.opacity = "1";
        document.getElementById("btn-constellation").innerText = "⚡ TACTICAL CONSTELLATION";
        
        constellationGroup.forEach(c => {
            scene.remove(c.mesh);
            scene.remove(c.line);
        });
        constellationGroup = [];
    }
}
'''
if 'function toggleConstellation' not in app_js:
    app_js += '\n' + constellation_fn

# Hook up event listener
hook = '''    const btnConst = document.getElementById("btn-constellation");
    if(btnConst) btnConst.onclick = toggleConstellation;'''
if 'btnConst.onclick' not in app_js:
    app_js = app_js.replace('renderSuggestionChips();', f'renderSuggestionChips();\n{hook}')

# Update animate function to move constellation and labels
anim_injection = '''        
        if (isConstellationMode) {
            const timeStep = 50; // accelerated time
            const canvasRect = renderer.domElement.getBoundingClientRect();
            
            constellationGroup.forEach(c => {
                // Update true anomaly
                const n = Math.sqrt(MU_EARTH / Math.pow(c.data.a, 3));
                c.nu += n * timeStep; // Simplified circular/elliptic update for visual
                
                // Radius
                const e = c.data.e;
                const a = c.data.a;
                const r = (a * (1 - e*e)) / (1 + e * Math.cos(c.nu));
                
                // Position in orbital plane
                const x_orb = r * Math.cos(c.nu);
                const y_orb = r * Math.sin(c.nu);
                
                // Rotation
                const i_rad = c.data.i * Math.PI / 180;
                const raan_rad = c.data.raan * Math.PI / 180;
                const argp_rad = c.data.argp * Math.PI / 180;
                
                // Apply rotation matrices (simplified ZYX)
                const cos_O = Math.cos(raan_rad), sin_O = Math.sin(raan_rad);
                const cos_i = Math.cos(i_rad), sin_i = Math.sin(i_rad);
                const cos_w = Math.cos(argp_rad), sin_w = Math.sin(argp_rad);

                const r11 = cos_O * cos_w - sin_O * sin_w * cos_i;
                const r21 = sin_O * cos_w + cos_O * sin_w * cos_i;
                const r31 = sin_w * sin_i;

                const r12 = -cos_O * sin_w - sin_O * cos_w * cos_i;
                const r22 = -sin_O * sin_w + cos_O * cos_w * cos_i;
                const r32 = cos_w * sin_i;

                c.mesh.position.x = r11 * x_orb + r12 * y_orb;
                c.mesh.position.y = r21 * x_orb + r22 * y_orb;
                c.mesh.position.z = r31 * x_orb + r32 * y_orb;
                
                // Project to 2D Screen for Label
                const pos = c.mesh.position.clone();
                pos.project(camera);
                
                // Only show if in front of camera
                if (pos.z < 1) {
                    c.labelEl.style.display = "block";
                    const x = (pos.x * .5 + .5) * canvasRect.width;
                    const y = (pos.y * -.5 + .5) * canvasRect.height;
                    c.labelEl.style.left = `${x}px`;
                    c.labelEl.style.top = `${y}px`;
                } else {
                    c.labelEl.style.display = "none";
                }
            });
        }
'''
if 'if (isConstellationMode)' not in app_js:
    # insert inside animate
    app_js = app_js.replace('if (commBeam) {', f'{anim_injection}\n        if (commBeam) {{')

with open(app_file, 'w', encoding='utf-8') as f:
    f.write(app_js)

print("Constellation logic injected.")
