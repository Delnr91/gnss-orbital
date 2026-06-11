import os
import re

app_file = r'c:\Users\invde\OneDrive\Documents\gnss-orbital-py\frontend\js\app.js'

with open(app_file, 'r', encoding='utf-8') as f:
    js = f.read()

# 1. Remove ⚡ emoji from translations and index.html
js = js.replace('"ctrl.constellation": "⚡ MULTI-ORBIT VIEW"', '"ctrl.constellation": "◈ MULTI-ORBIT VIEW"')
js = js.replace('"ctrl.constellation": "⚡ VISTA MULTI-ÓRBITA"', '"ctrl.constellation": "◈ VISTA MULTI-ÓRBITA"')
js = js.replace('"ctrl.constellation": "⚡ 多轨道星座视图"', '"ctrl.constellation": "◈ 多轨道星座视图"')
js = js.replace('document.getElementById("btn-constellation").innerText = "⚡ TACTICAL CONSTELLATION";', 'document.getElementById("btn-constellation").innerText = "◈ TACTICAL CONSTELLATION";')

# Also fix index.html
index_file = r'c:\Users\invde\OneDrive\Documents\gnss-orbital-py\frontend\index.html'
with open(index_file, 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('⚡ MULTI-ORBIT VIEW', '◈ MULTI-ORBIT VIEW')
with open(index_file, 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Fix the animate() function to propagate constellations and project 2D labels
animate_code_original = '''    if (renderer && scene && camera) {
        renderer.render(scene, camera);
    }
}'''

animate_code_new = '''    // Propagate Tactical Constellation
    if (isConstellationMode && constellationGroup) {
        const timeFactor = 0.02; // Global constellation time speed
        
        const canvasContainer = document.getElementById("canvas-container");
        const hw = canvasContainer.clientWidth / 2;
        const hh = canvasContainer.clientHeight / 2;
        
        constellationGroup.forEach(c => {
            const periodSec = 2 * Math.PI * Math.sqrt(Math.pow(c.data.a, 3) / MU_EARTH);
            c.nu += (timeFactor * 3600) / periodSec; // Advance true anomaly
            
            // Get Cartesian Position
            const pos = getCartesianPosition(c.data.a, c.data.e, c.data.i, c.data.raan, c.data.argp, c.nu);
            c.mesh.position.set(pos.x, pos.y, pos.z);
            
            // 2D Label Projection
            const vector = new THREE.Vector3(pos.x, pos.y, pos.z);
            vector.project(camera);
            
            if (vector.z < 1.0) { // If in front of camera
                c.labelEl.style.display = 'block';
                const x = (vector.x * hw) + hw;
                const y = -(vector.y * hh) + hh;
                c.labelEl.style.left = `${x}px`;
                c.labelEl.style.top = `${y - 15}px`; // Slightly above satellite
            } else {
                c.labelEl.style.display = 'none'; // Behind camera
            }
        });
    }

    if (renderer && scene && camera) {
        renderer.render(scene, camera);
    }
}'''

js = js.replace(animate_code_original, animate_code_new)

# 3. Add camera zoom to toggleConstellation()
toggle_const_code = '''        // Build Constellation Data
        const sats = ['''

toggle_const_new = '''        // Zoom out camera to see GEO orbits (42,000 km)
        if (camera && controls) {
            camera.position.set(80000, 50000, 80000);
            controls.update();
        }

        // Build Constellation Data
        const sats = ['''

js = js.replace(toggle_const_code, toggle_const_new)

with open(app_file, 'w', encoding='utf-8') as f:
    f.write(js)

print("Constellation physics, camera zoom, and emoji removals patched successfully!")
