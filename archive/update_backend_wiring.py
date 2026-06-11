import os

file_path = r'c:\Users\invde\OneDrive\Documents\gnss-orbital-py\frontend\app.js'

with open(file_path, 'r', encoding='utf-8') as f:
    code = f.read()

# 1. Update the Moon scaling
moon_old = 'const moonGeo = new THREE.SphereGeometry(1737, 32, 32);'
moon_new = 'const moonGeo = new THREE.SphereGeometry(1737 * 10, 32, 32); // 10x visual scale for visibility'
code = code.replace(moon_old, moon_new)

# 2. Refactor updatePlot to call /api/orbit/propagate
update_plot_old = '''function updatePlot() {
    const a = parseFloat(document.getElementById("input-a").value);
    const e = parseFloat(document.getElementById("input-e").value);
    
    // Safety check for surface intersection
    const perigee = a * (1 - e);
    const warnEl = document.getElementById("orbit-warning");
    if (perigee < EARTH_RADIUS) {
        warnEl.innerText = translations[currentLang]["warning.subsurface"].replace("{radius}", EARTH_RADIUS);
        warnEl.style.display = "block";
    } else {
        warnEl.style.display = "none";
    }
    
    // Re-propagate the visual path
    const points = [];
    for (let theta = 0; theta <= Math.PI * 2; theta += 0.05) {
        const r = (a * (1 - e*e)) / (1 + e * Math.cos(theta));
        const x = r * Math.cos(theta);
        const y = r * Math.sin(theta);
        points.push(new THREE.Vector3(x, y, 0));
    }
    
    orbitLine.geometry.dispose();
    orbitLine.geometry = new THREE.BufferGeometry().setFromPoints(points);
    
    orbitalParams = { a: a, e: e, i: parseFloat(document.getElementById("input-i").value) };
    
    // Update metric cards
    const T_hrs = (2 * Math.PI * Math.sqrt(Math.pow(a, 3) / MU_EARTH)) / 3600;
    document.getElementById("metric-period").innerText = T_hrs.toFixed(2) + " hrs";
    document.getElementById("metric-perigee").innerText = (perigee - EARTH_RADIUS).toFixed(0) + " km";
    document.getElementById("metric-apogee").innerText = (a * (1 + e) - EARTH_RADIUS).toFixed(0) + " km";
}'''

update_plot_new = '''async function updatePlot() {
    const a = parseFloat(document.getElementById("input-a").value);
    const e = parseFloat(document.getElementById("input-e").value);
    const i_inc = parseFloat(document.getElementById("input-i").value);
    const argp = parseFloat(document.getElementById("input-argp").value);
    
    orbitalParams = { a: a, e: e, i: i_inc, argp: argp, raan: 0 };
    
    // Safety check for surface intersection
    const perigee = a * (1 - e);
    const warnEl = document.getElementById("orbit-warning");
    if (perigee < EARTH_RADIUS) {
        warnEl.innerText = translations[currentLang]["warning.subsurface"].replace("{radius}", EARTH_RADIUS);
        warnEl.style.display = "block";
    } else {
        warnEl.style.display = "none";
    }
    
    // Update metric cards
    const T_hrs = (2 * Math.PI * Math.sqrt(Math.pow(a, 3) / MU_EARTH)) / 3600;
    document.getElementById("metric-period").innerText = T_hrs.toFixed(2) + " hrs";
    document.getElementById("metric-perigee").innerText = (perigee - EARTH_RADIUS).toFixed(0) + " km";
    document.getElementById("metric-apogee").innerText = (a * (1 + e) - EARTH_RADIUS).toFixed(0) + " km";
    
    // API Call to Python Backend for precise orbital propagation
    try {
        const payload = {
            a: a, e: e, i: i_inc, raan: 0.0, argp: argp, nu0: 0.0
        };
        const response = await fetch('/api/orbit/propagate', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(payload)
        });
        const data = await response.json();
        if (data.points) {
            const points = data.points.map(p => new THREE.Vector3(p.x, p.y, p.z));
            orbitLine.geometry.dispose();
            orbitLine.geometry = new THREE.BufferGeometry().setFromPoints(points);
        }
    } catch(err) {
        console.error("Failed to propagate orbit via API:", err);
        // Fallback to basic 2D
        const points = [];
        for (let theta = 0; theta <= Math.PI * 2; theta += 0.05) {
            const r = (a * (1 - e*e)) / (1 + e * Math.cos(theta));
            points.push(new THREE.Vector3(r * Math.cos(theta), r * Math.sin(theta), 0));
        }
        orbitLine.geometry.dispose();
        orbitLine.geometry = new THREE.BufferGeometry().setFromPoints(points);
    }
}'''
code = code.replace(update_plot_old, update_plot_new)


# 3. Refactor querySecondBrainAgent and handleUserMessageSubmit
query_agent_old = '''function querySecondBrainAgent(query) {
    const q = query.toLowerCase();
    
    // Domain Check
    const tokens = q.split(/[\\s,\\.\\?\\!\\-\\/\\(\\)]+/).filter(t => t.length > 2);
    const isSpaceRelated = tokens.some(token => spaceKeywords.includes(token));
    
    if (!isSpaceRelated) {
        return {
            text: translations[currentLang]["teacher.offtopic"],
            doc: null
        };
    }
    
    let bestMatch = null;
    let highestScore = 0;
    
    // Search the KB
    for (const [filename, content] of Object.entries(markdownKB)) {
        let score = 0;
        
        // Boost for Title/Header matches
        const lines = content.split('\\n');
        const headers = lines.filter(l => l.startsWith('#')).map(l => l.toLowerCase());
        
        tokens.forEach(token => {
            headers.forEach(h => {
                if (h.includes(token)) score += 5.0; // Huge boost for header matches
            });
            
            const bodyText = content.toLowerCase();
            // Standard weight for matching tokens in body text
            if (bodyText.includes(token)) {
                const matchesCount = (bodyText.match(new RegExp(token.replace(/[-\\/\\\\^$*+?.()|[\\]{}]/g, '\\\\$&'), 'g')) || []).length;
                let tokenScore = Math.min(matchesCount, 3) * 1.0; // cap term frequency influence
                
                score += tokenScore;
            }
        });
        
        if (score > highestScore) {
            highestScore = score;
            bestMatch = filename;
        }
    }
    
    if (highestScore < 1.0) {
        return {
            text: translations[currentLang]["teacher.no_match"],
            doc: null
        };
    }
    
    // Extract a relevant section to simulate "learning"
    const content = markdownKB[bestMatch];
    const sections = content.split(/\\n##\\s/);
    let bestSection = sections[0];
    let maxSScore = 0;
    
    sections.forEach(sec => {
        let sScore = 0;
        tokens.forEach(token => {
            if (sec.toLowerCase().includes(token)) sScore++;
        });
        if (sScore > maxSScore) {
            maxSScore = sScore;
            bestSection = sec;
        }
    });
    
    // If it was split, re-add the ## 
    if (bestSection !== sections[0]) {
        bestSection = "## " + bestSection;
    }
    
    return {
        text: translations[currentLang]["teacher.reply_intro"].replace("{document}", bestMatch) + "\\n\\n" + bestSection,
        doc: bestMatch
    };
}'''

handle_submit_old = '''function handleUserMessageSubmit() {
    const input = document.getElementById("chat-input");
    const message = input.value.trim();
    if (!message) return;
    
    // 1. Post user message
    appendChatBubble(message, "user");
    input.value = "";
    
    // 2. Post agent typing indicator
    const typingBubble = appendChatBubble(translations[currentLang]["teacher.searching"], "bot", false);
    
    // Update Karmaloop Stat
    // ... wait, karmaloop logic was modified here by previous script. I will just rewrite the whole function.
'''

# Instead of relying on exact match for the whole function, we'll replace the click handlers and functions.
# Let's use regex.
import re

handle_submit_regex = re.compile(r'function handleUserMessageSubmit\(\) \{[\s\S]*?\}\s*(?=function appendChatBubble)', re.MULTILINE)
new_handle_submit = '''async function handleUserMessageSubmit() {
    const input = document.getElementById("chat-input");
    const message = input.value.trim();
    if (!message) return;
    
    appendChatBubble(message, "user");
    input.value = "";
    
    const typingBubble = appendChatBubble("Consulting Python Backend (TF-IDF)...", "bot", false);
    
    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ message: message })
        });
        const data = await response.json();
        
        typingBubble.remove();
        
        if (data.doc) {
            const intro = translations[currentLang]["teacher.reply_intro"] 
                ? translations[currentLang]["teacher.reply_intro"].replace("{document}", data.doc)
                : `Found in ${data.doc}:`;
            appendChatBubble(intro + "\\n\\n" + data.response, "bot", true);
        } else {
            appendChatBubble(data.response, "bot", false);
        }
    } catch (err) {
        typingBubble.remove();
        appendChatBubble("Error: Backend offline.", "bot", false);
    }
}
'''
code = handle_submit_regex.sub(new_handle_submit, code)

# We can safely just delete querySecondBrainAgent
query_regex = re.compile(r'function querySecondBrainAgent\(query\) \{[\s\S]*?return \{\s*text:.*?\s*doc:.*?\s*\};\s*\}', re.MULTILINE)
code = query_regex.sub('', code)


# 4. Remove `documents.js` from index.html
# Need to do this separately, but I'll write the script logic to modify index.html too.

# Write back app.js
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(code)

print("Wiring complete.")
