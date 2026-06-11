import re

app_file = r'c:\Users\invde\OneDrive\Documents\gnss-orbital-py\frontend\js\app.js'

with open(app_file, 'r', encoding='utf-8') as f:
    js = f.read()

# Replace the mock querySecondBrainAgent function with a real fetch call
search_str = '''function querySecondBrainAgent(userInput) {
    const input = userInput.toLowerCase();
    
    const docs = documents.filter(doc => input.includes(doc.tags[0]) || input.includes(doc.title.toLowerCase()));
    
    if (docs.length > 0) {
        return translations[currentLang]["teacher.reply_intro"].replace('{document}', docs[0].title) + `<br><br><i>${docs[0].content}</i>`;
    }
    
    // Check for off-topic
    const offTopic = ["hello", "hi", "how are you", "weather"];
    if (offTopic.some(word => input.includes(word))) {
        return translations[currentLang]["teacher.offtopic"];
    }
    
    return translations[currentLang]["teacher.no_match"];
}'''

replace_str = '''async function querySecondBrainAgent(userInput) {
    try {
        // Change this URL to your Oracle Cloud IP when deploying:
        // const API_URL = "http://YOUR_ORACLE_IP:8000/api/chat";
        const API_URL = "http://localhost:8000/api/chat";
        
        const response = await fetch(API_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message: userInput })
        });
        
        const data = await response.json();
        return data.response;
    } catch (error) {
        console.error("Backend connection failed:", error);
        return "ERROR: Connection to APEX-1 Backend failed. Is the server running?";
    }
}'''

# Need to also update the caller inside the setTimeout to use async/await
search_caller = '''    if (typeof botSpeakStart === 'function') botSpeakStart();
    setTimeout(() => {
        const response = querySecondBrainAgent(message);
        appendChatBubble("bot", response);
        if (typeof botSpeakEnd === 'function') botSpeakEnd();
    }, 1200);'''

replace_caller = '''    if (typeof botSpeakStart === 'function') botSpeakStart();
    setTimeout(async () => {
        const response = await querySecondBrainAgent(message);
        appendChatBubble("bot", response);
        if (typeof botSpeakEnd === 'function') botSpeakEnd();
    }, 1200);'''

js = js.replace(search_str, replace_str)
js = js.replace(search_caller, replace_caller)

with open(app_file, 'w', encoding='utf-8') as f:
    f.write(js)
