// APEX-1 Living Core — liquid shader orb + frequency ring
// A GPU-displaced sphere that breathes, listens, thinks and speaks.
// Exposed API: window.ApexOrb = { init, setState, getState, pulse }

(function () {
    "use strict";

    // ------------------------------------------------------------------
    // GLSL: Ashima 3D simplex noise (public domain) + displacement shader
    // ------------------------------------------------------------------
    const NOISE_GLSL = `
    vec3 mod289(vec3 x){return x - floor(x * (1.0/289.0)) * 289.0;}
    vec4 mod289(vec4 x){return x - floor(x * (1.0/289.0)) * 289.0;}
    vec4 permute(vec4 x){return mod289(((x*34.0)+1.0)*x);}
    vec4 taylorInvSqrt(vec4 r){return 1.79284291400159 - 0.85373472095314 * r;}
    float snoise(vec3 v){
        const vec2 C = vec2(1.0/6.0, 1.0/3.0);
        const vec4 D = vec4(0.0, 0.5, 1.0, 2.0);
        vec3 i  = floor(v + dot(v, C.yyy));
        vec3 x0 = v - i + dot(i, C.xxx);
        vec3 g = step(x0.yzx, x0.xyz);
        vec3 l = 1.0 - g;
        vec3 i1 = min(g.xyz, l.zxy);
        vec3 i2 = max(g.xyz, l.zxy);
        vec3 x1 = x0 - i1 + C.xxx;
        vec3 x2 = x0 - i2 + C.yyy;
        vec3 x3 = x0 - D.yyy;
        i = mod289(i);
        vec4 p = permute(permute(permute(
                 i.z + vec4(0.0, i1.z, i2.z, 1.0))
               + i.y + vec4(0.0, i1.y, i2.y, 1.0))
               + i.x + vec4(0.0, i1.x, i2.x, 1.0));
        float n_ = 0.142857142857;
        vec3 ns = n_ * D.wyz - D.xzx;
        vec4 j = p - 49.0 * floor(p * ns.z * ns.z);
        vec4 x_ = floor(j * ns.z);
        vec4 y_ = floor(j - 7.0 * x_);
        vec4 x = x_ * ns.x + ns.yyyy;
        vec4 y = y_ * ns.x + ns.yyyy;
        vec4 h = 1.0 - abs(x) - abs(y);
        vec4 b0 = vec4(x.xy, y.xy);
        vec4 b1 = vec4(x.zw, y.zw);
        vec4 s0 = floor(b0)*2.0 + 1.0;
        vec4 s1 = floor(b1)*2.0 + 1.0;
        vec4 sh = -step(h, vec4(0.0));
        vec4 a0 = b0.xzyw + s0.xzyw*sh.xxyy;
        vec4 a1 = b1.xzyw + s1.xzyw*sh.zzww;
        vec3 p0 = vec3(a0.xy, h.x);
        vec3 p1 = vec3(a0.zw, h.y);
        vec3 p2 = vec3(a1.xy, h.z);
        vec3 p3 = vec3(a1.zw, h.w);
        vec4 norm = taylorInvSqrt(vec4(dot(p0,p0), dot(p1,p1), dot(p2,p2), dot(p3,p3)));
        p0 *= norm.x; p1 *= norm.y; p2 *= norm.z; p3 *= norm.w;
        vec4 m = max(0.6 - vec4(dot(x0,x0), dot(x1,x1), dot(x2,x2), dot(x3,x3)), 0.0);
        m = m * m;
        return 42.0 * dot(m*m, vec4(dot(p0,x0), dot(p1,x1), dot(p2,x2), dot(p3,x3)));
    }`;

    const VERTEX_SHADER = NOISE_GLSL + `
    uniform float uTime;
    uniform float uAmplitude;
    uniform float uFrequency;
    varying float vDisplacement;
    varying vec3 vNormalW;
    varying vec3 vPositionW;
    void main() {
        // Two octaves of flowing noise: large slow swells + fine ripples
        float n1 = snoise(normal * uFrequency + vec3(uTime * 0.45, uTime * 0.3, 0.0));
        float n2 = snoise(normal * uFrequency * 2.7 + vec3(0.0, uTime * 0.9, uTime * 0.6)) * 0.35;
        float d = (n1 + n2) * uAmplitude;
        vDisplacement = d;
        vec3 displaced = position + normal * d;
        vNormalW = normalize(normalMatrix * normal);
        vec4 mvPosition = modelViewMatrix * vec4(displaced, 1.0);
        vPositionW = mvPosition.xyz;
        gl_Position = projectionMatrix * mvPosition;
    }`;

    const FRAGMENT_SHADER = `
    uniform vec3 uColorA;
    uniform vec3 uColorB;
    uniform float uGlow;
    varying float vDisplacement;
    varying vec3 vNormalW;
    varying vec3 vPositionW;
    void main() {
        vec3 viewDir = normalize(-vPositionW);
        float fresnel = pow(1.0 - max(dot(viewDir, normalize(vNormalW)), 0.0), 2.2);
        // Crest highlights: peaks of the liquid glow brighter
        float crest = smoothstep(0.0, 0.35, vDisplacement);
        vec3 base = mix(uColorA, uColorB, crest);
        vec3 color = base * (0.35 + crest * 0.65) + uColorB * fresnel * uGlow;
        float alpha = 0.92;
        gl_FragColor = vec4(color, alpha);
    }`;

    // Atmosphere halo (backside fresnel shell)
    const HALO_VERTEX = `
    varying vec3 vNormalW;
    varying vec3 vPositionW;
    void main() {
        vNormalW = normalize(normalMatrix * normal);
        vec4 mvPosition = modelViewMatrix * vec4(position, 1.0);
        vPositionW = mvPosition.xyz;
        gl_Position = projectionMatrix * mvPosition;
    }`;
    const HALO_FRAGMENT = `
    uniform vec3 uColor;
    uniform float uIntensity;
    varying vec3 vNormalW;
    varying vec3 vPositionW;
    void main() {
        vec3 viewDir = normalize(-vPositionW);
        float rim = pow(1.0 - abs(dot(viewDir, normalize(vNormalW))), 3.0);
        gl_FragColor = vec4(uColor, rim * uIntensity);
    }`;

    // ------------------------------------------------------------------
    // State machine targets
    // ------------------------------------------------------------------
    const STATES = {
        idle: {
            amplitude: 0.10, frequency: 1.6, speed: 0.35, glow: 0.9,
            colorA: [0.08, 0.16, 0.24], colorB: [0.35, 0.78, 0.88],
            ringEnergy: 0.10, rotation: 0.0015
        },
        listening: {
            amplitude: 0.16, frequency: 2.1, speed: 0.7, glow: 1.25,
            colorA: [0.07, 0.20, 0.28], colorB: [0.42, 0.88, 0.96],
            ringEnergy: 0.28, rotation: 0.003
        },
        thinking: {
            amplitude: 0.30, frequency: 3.4, speed: 2.3, glow: 1.5,
            colorA: [0.10, 0.12, 0.32], colorB: [0.55, 0.62, 1.0],
            ringEnergy: 0.45, rotation: 0.011
        },
        speaking: {
            amplitude: 0.34, frequency: 2.4, speed: 1.5, glow: 1.7,
            colorA: [0.05, 0.22, 0.30], colorB: [0.45, 0.95, 1.0],
            ringEnergy: 1.0, rotation: 0.005
        }
    };

    // Live (interpolated) parameters
    const live = {
        amplitude: 0.10, frequency: 1.6, speed: 0.35, glow: 0.9,
        colorA: [0.08, 0.16, 0.24], colorB: [0.35, 0.78, 0.88],
        ringEnergy: 0.10, rotation: 0.0015
    };

    let currentState = "idle";
    let emotion = null;          // active emotion overlay (e.g. "happy")
    let emotionStart = 0;
    let scene, camera, renderer, orbMesh, haloMesh, uniforms, haloUniforms;
    let freqCanvas, freqCtx;
    let container;
    let shaderTime = 0;
    let lastFrameTs = 0;
    let pulses = [];           // click ripples on the ring canvas
    let pointer = { x: 0, y: 0 };
    let barLevels = [];        // smoothed per-bar spectrum
    const NUM_BARS = 96;
    let initialized = false;

    function lerp(a, b, t) { return a + (b - a) * t; }

    // Pseudo-voice envelope: layered sines gated by state, looks like speech cadence
    function voiceEnvelope(t) {
        const raw =
            Math.sin(t * 7.1) * 0.55 +
            Math.sin(t * 13.7 + 1.3) * 0.30 +
            Math.sin(t * 3.3 + 0.7) * 0.45 +
            Math.sin(t * 23.0) * 0.12;
        // Syllable gating: occasionally near-silent gaps
        const gate = Math.max(0, Math.sin(t * 1.9) + 0.55);
        return Math.max(0, raw * gate) / 1.4;
    }

    function init(containerId) {
        container = document.getElementById(containerId);
        if (!container || typeof THREE === "undefined") return;

        const orbCanvas = container.querySelector("#orb-canvas");
        freqCanvas = container.querySelector("#freq-canvas");
        if (!orbCanvas || !freqCanvas) return;
        freqCtx = freqCanvas.getContext("2d");

        for (let i = 0; i < NUM_BARS; i++) barLevels.push(0);

        scene = new THREE.Scene();
        camera = new THREE.PerspectiveCamera(40, 1, 0.1, 100);
        camera.position.z = 4.2;

        renderer = new THREE.WebGLRenderer({ canvas: orbCanvas, antialias: true, alpha: true });
        renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));

        uniforms = {
            uTime: { value: 0 },
            uAmplitude: { value: live.amplitude },
            uFrequency: { value: live.frequency },
            uColorA: { value: new THREE.Color(...live.colorA) },
            uColorB: { value: new THREE.Color(...live.colorB) },
            uGlow: { value: live.glow }
        };

        const geometry = new THREE.IcosahedronGeometry(1.0, 64);
        const material = new THREE.ShaderMaterial({
            uniforms: uniforms,
            vertexShader: VERTEX_SHADER,
            fragmentShader: FRAGMENT_SHADER,
            transparent: true
        });
        orbMesh = new THREE.Mesh(geometry, material);
        scene.add(orbMesh);

        haloUniforms = {
            uColor: { value: new THREE.Color(...live.colorB) },
            uIntensity: { value: 0.55 }
        };
        const haloGeo = new THREE.SphereGeometry(1.35, 48, 48);
        const haloMat = new THREE.ShaderMaterial({
            uniforms: haloUniforms,
            vertexShader: HALO_VERTEX,
            fragmentShader: HALO_FRAGMENT,
            transparent: true,
            side: THREE.BackSide,
            depthWrite: false,
            blending: THREE.AdditiveBlending
        });
        haloMesh = new THREE.Mesh(haloGeo, haloMat);
        scene.add(haloMesh);

        // Subtle parallax: the core leans toward the cursor — it notices you
        window.addEventListener("pointermove", (e) => {
            pointer.x = (e.clientX / window.innerWidth - 0.5) * 2;
            pointer.y = (e.clientY / window.innerHeight - 0.5) * 2;
        });

        // Touching the core sends a ripple through the ring
        container.addEventListener("pointerdown", () => pulse());

        window.addEventListener("resize", resize);
        resize();

        initialized = true;
        lastFrameTs = performance.now();
        requestAnimationFrame(loop);
    }

    function resize() {
        if (!container || !renderer) return;
        const size = Math.min(container.clientWidth, container.clientHeight);
        renderer.setSize(size, size, false);
        const orbCanvas = renderer.domElement;
        orbCanvas.style.width = size + "px";
        orbCanvas.style.height = size + "px";
        camera.aspect = 1;
        camera.updateProjectionMatrix();

        const dpr = Math.min(window.devicePixelRatio || 1, 2);
        freqCanvas.width = container.clientWidth * dpr;
        freqCanvas.height = container.clientHeight * dpr;
        freqCanvas.style.width = container.clientWidth + "px";
        freqCanvas.style.height = container.clientHeight + "px";
        freqCtx.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    function setState(name) {
        if (STATES[name]) currentState = name;
    }
    function getState() { return currentState; }

    function pulse() {
        pulses.push({ r: 0, alpha: 0.8 });
        // Physical flinch: brief amplitude kick
        live.amplitude = Math.min(live.amplitude + 0.18, 0.65);
    }

    // Emotion overlay: a short, expressive performance on top of the current state.
    // "happy" = damped joy-bounce (squash & stretch), golden bloom, triple ripple burst.
    function emote(name) {
        if (name !== "happy") return;
        emotion = "happy";
        emotionStart = performance.now();
        pulses.push({ r: 0, alpha: 0.9 });
        setTimeout(() => pulses.push({ r: 0, alpha: 0.75 }), 160);
        setTimeout(() => pulses.push({ r: 0, alpha: 0.6 }), 340);
    }

    function loop(ts) {
        if (!initialized) return;
        requestAnimationFrame(loop);
        const dt = Math.min((ts - lastFrameTs) / 1000, 0.05);
        lastFrameTs = ts;

        const target = STATES[currentState];
        const k = 1 - Math.pow(0.001, dt); // framerate-independent smoothing

        live.amplitude = lerp(live.amplitude, target.amplitude, k);
        live.frequency = lerp(live.frequency, target.frequency, k);
        live.speed = lerp(live.speed, target.speed, k);
        live.glow = lerp(live.glow, target.glow, k);
        live.ringEnergy = lerp(live.ringEnergy, target.ringEnergy, k);
        live.rotation = lerp(live.rotation, target.rotation, k);
        for (let c = 0; c < 3; c++) {
            live.colorA[c] = lerp(live.colorA[c], target.colorA[c], k);
            live.colorB[c] = lerp(live.colorB[c], target.colorB[c], k);
        }

        shaderTime += dt * live.speed;

        // Voice modulation while speaking: the surface trembles with the words
        let speakBoost = 0;
        if (currentState === "speaking") {
            speakBoost = voiceEnvelope(ts / 1000) * 0.22;
        }

        // Emotion overlay: damped joy-bounce with golden bloom
        let emotionGlow = 0;
        let colorB = live.colorB;
        let scaleX = 1, scaleY = 1, scaleZ = 1;
        if (emotion === "happy") {
            const elapsed = (ts - emotionStart) / 1000;
            if (elapsed > 2.4) {
                emotion = null;
            } else {
                // Damped spring: big joyful hops that settle naturally
                const spring = Math.sin(elapsed * 13.0) * Math.exp(-elapsed * 2.0);
                scaleY = 1 + spring * 0.26;            // stretch up...
                scaleX = scaleZ = 1 - spring * 0.13;   // ...squash sideways (liquid!)
                const env = Math.exp(-elapsed * 1.1);
                emotionGlow = env * 0.8;
                // Blend the rim color toward warm gold while the joy lasts
                colorB = [
                    live.colorB[0] + (1.0 - live.colorB[0]) * env * 0.7,
                    live.colorB[1] + (0.86 - live.colorB[1]) * env * 0.7,
                    live.colorB[2] + (0.45 - live.colorB[2]) * env * 0.7
                ];
            }
        }

        uniforms.uTime.value = shaderTime;
        uniforms.uAmplitude.value = live.amplitude + speakBoost + emotionGlow * 0.12;
        uniforms.uFrequency.value = live.frequency;
        uniforms.uGlow.value = live.glow + emotionGlow;
        uniforms.uColorA.value.setRGB(live.colorA[0], live.colorA[1], live.colorA[2]);
        uniforms.uColorB.value.setRGB(colorB[0], colorB[1], colorB[2]);
        haloUniforms.uColor.value.setRGB(colorB[0], colorB[1], colorB[2]);
        haloUniforms.uIntensity.value = 0.35 + live.glow * 0.25 + speakBoost + emotionGlow * 0.5;

        orbMesh.rotation.y += live.rotation;
        orbMesh.rotation.z += live.rotation * 0.4;

        // Always alive: gentle buoyant bobbing + squash & stretch from emotions
        const bob = Math.sin(ts / 1000 * 0.9) * 0.045;
        orbMesh.position.y = bob;
        haloMesh.position.y = bob;
        orbMesh.scale.set(scaleX, scaleY, scaleZ);
        haloMesh.scale.set(scaleX, scaleY, scaleZ);

        // Lean toward the cursor
        const targetRotX = pointer.y * 0.25;
        const targetRotXOffset = targetRotX - orbMesh.rotation.x;
        orbMesh.rotation.x += targetRotXOffset * 0.04;
        scene.position.x = lerp(scene.position.x, pointer.x * 0.12, 0.04);
        scene.position.y = lerp(scene.position.y, -pointer.y * 0.12, 0.04);

        renderer.render(scene, camera);
        drawFrequencyRing(ts / 1000, speakBoost);
    }

    function drawFrequencyRing(t, speakBoost) {
        const w = freqCanvas.clientWidth || container.clientWidth;
        const h = freqCanvas.clientHeight || container.clientHeight;
        const orbPx = Math.min(w, h);
        if (orbPx < 24) return; // container hidden or collapsed: nothing to draw
        const cx = w / 2, cy = h / 2;
        const baseRadius = orbPx * 0.36;

        freqCtx.clearRect(0, 0, w, h);

        const energy = live.ringEnergy;
        const colB = live.colorB;
        const rgb = `${Math.round(colB[0] * 255)}, ${Math.round(colB[1] * 255)}, ${Math.round(colB[2] * 255)}`;

        // Spectrum bars radiating from the core
        for (let i = 0; i < NUM_BARS; i++) {
            const angle = (i / NUM_BARS) * Math.PI * 2 - Math.PI / 2;
            // Layered pseudo-spectrum: low bins move slow/high, high bins flicker
            const bin =
                Math.abs(Math.sin(t * 2.1 + i * 0.55)) * 0.45 +
                Math.abs(Math.sin(t * 4.7 + i * 1.31)) * 0.35 +
                Math.abs(Math.sin(t * 9.3 + i * 2.17)) * 0.20;
            const targetLevel = bin * energy * (0.5 + speakBoost * 3.2);
            barLevels[i] += (targetLevel - barLevels[i]) * 0.25;

            const len = 2 + barLevels[i] * orbPx * 0.13;
            const x1 = cx + Math.cos(angle) * baseRadius;
            const y1 = cy + Math.sin(angle) * baseRadius;
            const x2 = cx + Math.cos(angle) * (baseRadius + len);
            const y2 = cy + Math.sin(angle) * (baseRadius + len);

            freqCtx.beginPath();
            freqCtx.moveTo(x1, y1);
            freqCtx.lineTo(x2, y2);
            freqCtx.strokeStyle = `rgba(${rgb}, ${0.12 + barLevels[i] * 0.85})`;
            freqCtx.lineWidth = 1.6;
            freqCtx.stroke();
        }

        // Hairline orbit ring
        freqCtx.beginPath();
        freqCtx.arc(cx, cy, baseRadius - 4, 0, Math.PI * 2);
        freqCtx.strokeStyle = `rgba(${rgb}, 0.18)`;
        freqCtx.lineWidth = 1;
        freqCtx.stroke();

        // Click ripples expanding outward
        for (let i = pulses.length - 1; i >= 0; i--) {
            const p = pulses[i];
            p.r += orbPx * 0.012;
            p.alpha -= 0.016;
            if (p.alpha <= 0) { pulses.splice(i, 1); continue; }
            freqCtx.beginPath();
            freqCtx.arc(cx, cy, baseRadius + p.r, 0, Math.PI * 2);
            freqCtx.strokeStyle = `rgba(${rgb}, ${p.alpha})`;
            freqCtx.lineWidth = 1.5;
            freqCtx.stroke();
        }
    }

    window.ApexOrb = { init, setState, getState, pulse, resize, emote };
})();
