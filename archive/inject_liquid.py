import os

file_path = r'c:\Users\invde\OneDrive\Documents\gnss-orbital-py\frontend\css\style.css'

with open(file_path, 'r', encoding='utf-8') as f:
    code = f.read()

liquid_css = '''
/* --- LIQUID JARVIS AGENT --- */
.jarvis-core {
    position: relative;
    width: 150px;
    height: 150px;
    margin-bottom: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    /* Remove old ring code, replace with blob */
}

/* Hide old rings */
.jarvis-ring { display: none !important; }
.jarvis-center { display: none !important; }

/* The Liquid Blob */
.jarvis-core::before {
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    background: linear-gradient(45deg, var(--text-primary), #555, var(--text-secondary));
    background-size: 200% 200%;
    border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%;
    animation: liquidMorph 8s ease-in-out infinite, gradientShift 5s ease infinite;
    box-shadow: 0 0 40px rgba(255, 255, 255, 0.2);
    filter: blur(2px) contrast(1.2);
}

@keyframes liquidMorph {
    0%, 100% { border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%; transform: scale(1) rotate(0deg); }
    34% { border-radius: 70% 30% 50% 50% / 30% 30% 70% 70%; transform: scale(1.05) rotate(45deg); }
    67% { border-radius: 100% 60% 60% 100% / 100% 100% 60% 60%; transform: scale(0.95) rotate(90deg); }
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* --- NASA CHAT UI --- */
.jarvis-chat {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    position: relative;
    overflow: hidden;
}

/* Agent Name Watermark in Background */
.jarvis-chat::before {
    content: 'APEX-1';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-family: var(--font-title);
    font-size: 180px;
    color: rgba(255, 255, 255, 0.02);
    z-index: 0;
    pointer-events: none;
    letter-spacing: 20px;
}

.jarvis-chat .chat-history {
    flex-grow: 1;
    background: transparent !important;
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 0; /* NASA stark corners */
    position: relative;
    z-index: 1;
    padding: 20px;
    overflow-y: auto;
}

.jarvis-chat .chat-input-bar {
    position: relative;
    z-index: 1;
    border-radius: 0;
    border: 1px solid rgba(255,255,255,0.1);
    border-top: none;
    background: rgba(0,0,0,0.5) !important;
}

.jarvis-chat .chat-input-bar input {
    font-family: var(--font-mono);
    color: var(--text-primary);
    background: transparent;
    border: none;
}

.jarvis-chat .chat-input-bar button {
    background: transparent;
    border-left: 1px solid rgba(255,255,255,0.1);
    color: var(--text-primary);
    font-family: var(--font-mono);
    text-transform: uppercase;
}

.jarvis-chat .chat-input-bar button:hover {
    background: rgba(255,255,255,0.1);
}

/* Chat bubble styling for NASA contrast */
.chat-bubble.bot {
    background: rgba(255, 255, 255, 0.05);
    border-left: 2px solid var(--text-primary);
    border-radius: 0;
    font-family: var(--font-mono);
}

.chat-bubble.user {
    background: rgba(0, 0, 0, 0.3);
    border-right: 2px solid var(--text-secondary);
    border-radius: 0;
    font-family: var(--font-mono);
    text-align: right;
}
'''

with open(file_path, 'a', encoding='utf-8') as f:
    f.write(liquid_css)

print("Liquid CSS applied.")
