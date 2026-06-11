import re

css_file = r'c:\Users\invde\OneDrive\Documents\gnss-orbital-py\frontend\css\index.css'

css_organism = '''
/* --- LIVING DIGITAL AI ORGANISM --- */
#ai-organism-container {
    display: flex;
    justify-content: center;
    align-items: center;
    background: radial-gradient(circle at center, rgba(0, 30, 40, 0.9) 0%, rgba(0, 5, 10, 1) 100%);
}

#ai-organism-container.active {
    opacity: 1 !important;
}

.organism-core {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    background: radial-gradient(circle, #00f3ff 0%, #0066ff 50%, transparent 80%);
    box-shadow: 0 0 50px #00f3ff, 0 0 100px #0066ff, inset 0 0 20px #ffffff;
    animation: pulseCore 4s ease-in-out infinite alternate, morphShape 8s ease-in-out infinite;
    position: relative;
    z-index: 2;
    filter: blur(2px) contrast(1.2);
}

.organism-ring {
    position: absolute;
    border-radius: 50%;
    border: 2px solid rgba(0, 243, 255, 0.3);
    border-top-color: #00f3ff;
    border-bottom-color: #0066ff;
    z-index: 1;
}

.ring-1 {
    width: 250px;
    height: 250px;
    animation: rotateRing 12s linear infinite;
    box-shadow: inset 0 0 20px rgba(0, 243, 255, 0.1);
}

.ring-2 {
    width: 350px;
    height: 350px;
    border-width: 1px;
    border-style: dashed;
    animation: rotateRing 20s linear infinite reverse;
    opacity: 0.5;
}

@keyframes pulseCore {
    0% { transform: scale(0.9); opacity: 0.8; filter: blur(2px) hue-rotate(0deg); }
    50% { filter: blur(4px) hue-rotate(15deg); }
    100% { transform: scale(1.1); opacity: 1; box-shadow: 0 0 80px #00f3ff, 0 0 150px #0066ff; filter: blur(1px) hue-rotate(-15deg); }
}

@keyframes morphShape {
    0% { border-radius: 50%; }
    25% { border-radius: 40% 60% 70% 30% / 40% 50% 60% 50%; }
    50% { border-radius: 60% 40% 30% 70% / 60% 30% 70% 40%; }
    75% { border-radius: 30% 70% 50% 50% / 50% 60% 40% 60%; }
    100% { border-radius: 50%; }
}

@keyframes rotateRing {
    0% { transform: rotate(0deg) scale(1); }
    50% { transform: rotate(180deg) scale(1.05); }
    100% { transform: rotate(360deg) scale(1); }
}

.organism-particles {
    position: absolute;
    width: 400px;
    height: 400px;
    background-image: radial-gradient(circle, #00f3ff 1px, transparent 1px);
    background-size: 20px 20px;
    animation: floatParticles 20s linear infinite;
    opacity: 0.1;
    z-index: 0;
    mask-image: radial-gradient(circle at center, black 0%, transparent 70%);
    -webkit-mask-image: radial-gradient(circle at center, black 0%, transparent 70%);
}

@keyframes floatParticles {
    0% { transform: translateY(0) rotate(0deg); }
    100% { transform: translateY(-100px) rotate(45deg); }
}
'''

with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

if 'LIVING DIGITAL AI ORGANISM' not in css:
    with open(css_file, 'a', encoding='utf-8') as f:
        f.write('\n' + css_organism)
