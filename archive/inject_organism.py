import os

ROOT = r'c:\Users\invde\OneDrive\Documents\gnss-orbital-py\frontend'
index_file = os.path.join(ROOT, 'index.html')
app_file = os.path.join(ROOT, 'js', 'app.js')

# 1. Update index.html
with open(index_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Add the organism canvas behind the chat
organism_canvas = '<canvas id="organism-canvas" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; pointer-events: auto;"></canvas>\\n                <div class="chat-header"'

if 'id="organism-canvas"' not in html:
    html = html.replace('<div class="chat-header"', organism_canvas)
with open(index_file, 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Update app.js
with open(app_file, 'r', encoding='utf-8') as f:
    js = f.read()

# Fix the Tab switcher to hide the 3D Simulator (Radar) and Video
tab_switcher_new = '''    const bgVideo = document.getElementById('bg-video');
    const simCanvas = document.getElementById('canvas-container');
    const orgCanvas = document.getElementById('organism-canvas');
    
    if (tab === 'brain') {
        if (bgVideo) bgVideo.style.display = 'none';
        if (simCanvas) simCanvas.style.display = 'none';
        if (orgCanvas) {
            orgCanvas.style.display = 'block';
            if (!window.organismInitialized) {
                initOrganismCanvas();
                window.organismInitialized = true;
            }
        }
    } else {
        if (bgVideo) bgVideo.style.display = 'block';
        if (simCanvas) simCanvas.style.display = 'block';
        if (orgCanvas) orgCanvas.style.display = 'none';
    }'''

search_str = 'const tab = btn.getAttribute("data-tab");\\n        document.getElementById(`tab-${tab}`).classList.add("active");'
replace_str = f'const tab = btn.getAttribute("data-tab");\\n        document.getElementById(`tab-${{tab}}`).classList.add("active");\\n{tab_switcher_new}'

if "window.organismInitialized" not in js:
    js = js.replace(search_str, replace_str)

# Add the complex Organism Canvas logic
organism_js = '''

// --- THE LIVING DIGITAL ORGANISM (BIOLOGICAL PARTICLE SYSTEM) ---
function initOrganismCanvas() {
    const canvas = document.getElementById('organism-canvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    
    let width, height;
    function resize() {
        const rect = canvas.parentElement.getBoundingClientRect();
        width = rect.width;
        height = rect.height;
        canvas.width = width;
        canvas.height = height;
    }
    window.addEventListener('resize', resize);
    resize();

    const particles = [];
    const numParticles = 120;
    
    // Mouse interaction
    let mouse = { x: width/2, y: height/2, active: false };
    
    canvas.addEventListener('mousemove', (e) => {
        const rect = canvas.getBoundingClientRect();
        mouse.x = e.clientX - rect.left;
        mouse.y = e.clientY - rect.top;
        mouse.active = true;
    });
    canvas.addEventListener('mouseleave', () => { mouse.active = false; });
    
    // Click creates a pulse wave
    let pulses = [];
    canvas.addEventListener('mousedown', (e) => {
        const rect = canvas.getBoundingClientRect();
        pulses.push({
            x: e.clientX - rect.left,
            y: e.clientY - rect.top,
            radius: 0,
            maxRadius: 300,
            strength: 1.0
        });
    });

    for(let i=0; i<numParticles; i++) {
        particles.push({
            x: Math.random() * width,
            y: Math.random() * height,
            vx: (Math.random() - 0.5) * 1.5,
            vy: (Math.random() - 0.5) * 1.5,
            baseRadius: Math.random() * 3 + 1,
            phase: Math.random() * Math.PI * 2,
            speed: Math.random() * 0.02 + 0.01,
            connections: []
        });
    }

    let time = 0;

    function renderOrganism() {
        requestAnimationFrame(renderOrganism);
        time += 0.016;
        
        // Biological fluid background clear
        ctx.fillStyle = 'rgba(5, 8, 15, 0.3)'; // Trail effect
        ctx.fillRect(0, 0, width, height);
        
        const breathingGlobal = Math.sin(time * 0.5) * 0.5 + 0.5; // 0 to 1
        
        // Process Pulses (Click rings)
        for (let i = pulses.length - 1; i >= 0; i--) {
            let p = pulses[i];
            p.radius += 8;
            p.strength -= 0.02;
            
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
            ctx.strokeStyle = `rgba(0, 255, 200, ${p.strength * 0.5})`;
            ctx.lineWidth = 2;
            ctx.stroke();
            
            if (p.strength <= 0) pulses.splice(i, 1);
        }

        // Update & Draw Particles
        for(let i=0; i<numParticles; i++) {
            let p = particles[i];
            
            // Organic biological drift (Perlin-like wandering)
            p.vx += Math.sin(time + p.phase) * 0.05;
            p.vy += Math.cos(time + p.phase) * 0.05;
            
            // Mouse gravity/repulsion
            if (mouse.active) {
                let dx = mouse.x - p.x;
                let dy = mouse.y - p.y;
                let dist = Math.sqrt(dx*dx + dy*dy);
                if (dist < 150) {
                    // Repel softly, like biological membranes
                    p.vx -= (dx / dist) * 0.5;
                    p.vy -= (dy / dist) * 0.5;
                } else if (dist < 300) {
                    // Attract softly from medium distance
                    p.vx += (dx / dist) * 0.05;
                    p.vy += (dy / dist) * 0.05;
                }
            }
            
            // Apply pulses force
            pulses.forEach(pulse => {
                let dx = pulse.x - p.x;
                let dy = pulse.y - p.y;
                let dist = Math.sqrt(dx*dx + dy*dy);
                if (Math.abs(dist - pulse.radius) < 20) {
                    p.vx -= (dx / dist) * pulse.strength * 2;
                    p.vy -= (dy / dist) * pulse.strength * 2;
                }
            });

            // Friction
            p.vx *= 0.92;
            p.vy *= 0.92;
            
            p.x += p.vx;
            p.y += p.vy;
            
            // Wrap around edges like a continuous petri dish
            if (p.x < 0) p.x = width;
            if (p.x > width) p.x = 0;
            if (p.y < 0) p.y = height;
            if (p.y > height) p.y = 0;

            // Breathing pulsing radius
            let currentRadius = p.baseRadius + Math.sin(time * p.speed * 50 + p.phase) * 2 * breathingGlobal;
            if (currentRadius < 0.5) currentRadius = 0.5;
            
            // Draw node
            ctx.beginPath();
            ctx.arc(p.x, p.y, currentRadius, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(0, 255, 200, ${0.4 + breathingGlobal * 0.4})`;
            ctx.fill();
        }
        
        // Draw Neural Network / Membrane Connections
        ctx.lineWidth = 1;
        for(let i=0; i<numParticles; i++) {
            for(let j=i+1; j<numParticles; j++) {
                let dx = particles[i].x - particles[j].x;
                let dy = particles[i].y - particles[j].y;
                let distSq = dx*dx + dy*dy;
                
                if (distSq < 15000) {
                    let dist = Math.sqrt(distSq);
                    let opacity = 1 - (dist / 122);
                    
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    // Organic bezier curves instead of straight lines
                    let midX = (particles[i].x + particles[j].x) / 2 + Math.sin(time + particles[i].phase) * 20;
                    let midY = (particles[i].y + particles[j].y) / 2 + Math.cos(time + particles[j].phase) * 20;
                    
                    ctx.quadraticCurveTo(midX, midY, particles[j].x, particles[j].y);
                    
                    // Mix cyan and blue for neural pathways
                    ctx.strokeStyle = `rgba(0, 168, 255, ${opacity * 0.5})`;
                    ctx.stroke();
                }
            }
        }
    }
    
    renderOrganism();
}
'''
if "initOrganismCanvas" not in js:
    js = js + organism_js

with open(app_file, 'w', encoding='utf-8') as f:
    f.write(js)

print("Fixed f-string error. Living digital organism canvas injected successfully.")
