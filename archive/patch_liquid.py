import re

app_file = r'c:\Users\invde\OneDrive\Documents\gnss-orbital-py\frontend\js\app.js'
html_file = r'c:\Users\invde\OneDrive\Documents\gnss-orbital-py\frontend\index.html'
css_file = r'c:\Users\invde\OneDrive\Documents\gnss-orbital-py\frontend\css\style.css'

# 1. Update index.html
with open(html_file, 'r', encoding='utf-8') as f:
    html = f.read()

old_tab_brain = '''            <!-- TAB 2: SPACE AGENT (Jarvis Core Layout) -->
            <section id="tab-brain" class="tab-pane">
                <div class="jarvis-layout">
                    <!-- Top: Jarvis Animation & Name -->
                    <div class="jarvis-header">
                        <div class="jarvis-core">
                            <div class="jarvis-ring ring-1"></div>
                            <div class="jarvis-ring ring-2"></div>
                            <div class="jarvis-ring ring-3"></div>
                            <div class="jarvis-center"></div>
                        </div>
                        <h2 class="jarvis-name" data-i18n="brain.agent_title" id="chat-agent-title">APEX-1 Space Agent</h2>
                        <div class="jarvis-status" data-i18n="brain.agent_subtitle" id="chat-agent-subtitle">ONLINE | KNOWLEDGE BASE SYNCED</div>
                    </div>

                    <!-- Bottom: Professional Chat Room -->
                    <div class="chat-agent-layout jarvis-chat">'''

new_tab_brain = '''            <!-- TAB 2: SPACE AGENT (Liquid Frequencies) -->
            <section id="tab-brain" class="tab-pane">
                <!-- Liquid Frequency Visualizer -->
                <div class="liquid-visualizer-container">
                    <canvas id="liquid-canvas"></canvas>
                </div>
                
                <div class="jarvis-layout">
                    <div class="jarvis-header">
                        <h2 class="jarvis-name" data-i18n="brain.agent_title" id="chat-agent-title">APEX-1 Space Agent</h2>
                        <div class="jarvis-status" data-i18n="brain.agent_subtitle" id="chat-agent-subtitle">ONLINE | KNOWLEDGE BASE SYNCED</div>
                    </div>

                    <!-- Bottom: Professional Chat Room -->
                    <div class="chat-agent-layout jarvis-chat">'''

if old_tab_brain in html:
    html = html.replace(old_tab_brain, new_tab_brain)
else:
    print("Warning: old_tab_brain not found in html")

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update app.js
with open(app_file, 'r', encoding='utf-8') as f:
    js = f.read()

liquid_js = '''
// --- LIQUID FREQUENCY VISUALIZER ---
let liquidCanvas, liquidCtx;
let liquidTime = 0;
let isSpeaking = false;
let targetAmplitude = 20;
let currentAmplitude = 20;

function initLiquidVisualizer() {
    liquidCanvas = document.getElementById('liquid-canvas');
    if (!liquidCanvas) return;
    liquidCtx = liquidCanvas.getContext('2d');
    
    function resizeCanvas() {
        liquidCanvas.width = window.innerWidth;
        liquidCanvas.height = window.innerHeight;
    }
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();
    
    requestAnimationFrame(renderLiquid);
}

function renderLiquid() {
    if (!liquidCtx || !liquidCanvas) return;
    requestAnimationFrame(renderLiquid);
    
    // Smoothly interpolate amplitude
    currentAmplitude += (targetAmplitude - currentAmplitude) * 0.1;
    
    const w = liquidCanvas.width;
    const h = liquidCanvas.height;
    const centerY = h / 2 - 100; // Centered slightly above the chat
    
    liquidCtx.clearRect(0, 0, w, h);
    
    // Draw 4 overlapping liquid frequency waves
    const waves = [
        { color: 'rgba(0, 243, 255, 0.4)', freq: 0.005, speed: 0.02, heightFactor: 1.0 },
        { color: 'rgba(0, 150, 255, 0.6)', freq: 0.008, speed: 0.03, heightFactor: 0.8 },
        { color: 'rgba(0, 255, 200, 0.3)', freq: 0.003, speed: 0.015, heightFactor: 1.2 },
        { color: 'rgba(255, 255, 255, 0.8)', freq: 0.01, speed: 0.04, heightFactor: 0.5 }
    ];
    
    for (let i = 0; i < waves.length; i++) {
        const wave = waves[i];
        liquidCtx.beginPath();
        liquidCtx.moveTo(0, centerY);
        
        for (let x = 0; x <= w; x += 5) {
            // Envelope function to taper edges
            const envelope = Math.sin((x / w) * Math.PI); 
            // Wave calculation
            const y = centerY + Math.sin(x * wave.freq + liquidTime * wave.speed) * (currentAmplitude * wave.heightFactor * envelope);
            liquidCtx.lineTo(x, y);
        }
        
        // Connect to bottom to fill
        liquidCtx.lineTo(w, h);
        liquidCtx.lineTo(0, h);
        liquidCtx.closePath();
        
        liquidCtx.fillStyle = wave.color;
        liquidCtx.fill();
    }
    
    // Add glowing core in the center
    const gradient = liquidCtx.createRadialGradient(w/2, centerY, 0, w/2, centerY, currentAmplitude * 3);
    gradient.addColorStop(0, 'rgba(0, 243, 255, 0.8)');
    gradient.addColorStop(1, 'rgba(0, 243, 255, 0)');
    
    liquidCtx.beginPath();
    liquidCtx.arc(w/2, centerY, currentAmplitude * 3, 0, Math.PI * 2);
    liquidCtx.fillStyle = gradient;
    liquidCtx.fill();
    
    liquidTime++;
}

// Trigger speaking animation when bot types
function botSpeakStart() {
    isSpeaking = true;
    targetAmplitude = 120; // High amplitude for speaking
}
function botSpeakEnd() {
    isSpeaking = false;
    targetAmplitude = 20; // Low amplitude for idle
}

'''

if 'initLiquidVisualizer' not in js:
    js = js + '\n' + liquid_js

# Hook botSpeakStart and botSpeakEnd into querySecondBrainAgent
if 'setTimeout(() => {' in js and 'const response = querySecondBrainAgent(message);' in js:
    # Find the logic that appends the user message and gets the bot response
    chat_logic_search = '''    appendChatBubble("user", message);
    chatInput.value = "";
    
    // Bot response
    setTimeout(() => {
        const response = querySecondBrainAgent(message);
        appendChatBubble("bot", response);
    }, 500);'''
    
    chat_logic_replace = '''    appendChatBubble("user", message);
    chatInput.value = "";
    
    // Bot response
    if (typeof botSpeakStart === 'function') botSpeakStart();
    setTimeout(() => {
        const response = querySecondBrainAgent(message);
        appendChatBubble("bot", response);
        if (typeof botSpeakEnd === 'function') botSpeakEnd();
    }, 1200);'''
    
    js = js.replace(chat_logic_search, chat_logic_replace)

if 'initBackgroundThreeJS();' in js and 'initLiquidVisualizer();' not in js:
    js = js.replace('initBackgroundThreeJS();', 'initBackgroundThreeJS();\n    initLiquidVisualizer();')

with open(app_file, 'w', encoding='utf-8') as f:
    f.write(js)

# 3. Update style.css
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

liquid_css = '''
/* --- LIQUID VISUALIZER --- */
.liquid-visualizer-container {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 1; /* Behind chat but above background */
    pointer-events: none;
}

#liquid-canvas {
    width: 100%;
    height: 100%;
}

.jarvis-layout {
    position: relative;
    z-index: 10;
    display: flex;
    flex-direction: column;
    justify-content: flex-end; /* Push chat to bottom */
    height: 100%;
    padding: 40px;
    background: transparent;
}

.jarvis-header {
    text-align: center;
    margin-bottom: 20px;
    /* Hide the old CSS circles */
    display: flex;
    flex-direction: column;
    align-items: center;
}

.jarvis-core {
    display: none !important; /* Hide old circles */
}

.jarvis-name {
    font-size: 24px;
    letter-spacing: 4px;
    color: #00f3ff;
    text-shadow: 0 0 10px #00f3ff;
    margin: 0;
}

.jarvis-status {
    font-size: 12px;
    color: #a0c0d0;
    letter-spacing: 2px;
    margin-top: 5px;
}

.jarvis-chat {
    width: 100%;
    max-width: 800px;
    margin: 0 auto;
    background: rgba(0, 20, 30, 0.4);
    backdrop-filter: blur(10px);
    -webkit-backdrop-filter: blur(10px);
    border: 1px solid rgba(0, 243, 255, 0.2);
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
    height: 40vh; /* Takes lower portion of screen */
}
'''

if 'LIQUID VISUALIZER' not in css:
    with open(css_file, 'a', encoding='utf-8') as f:
        f.write('\n' + liquid_css)
