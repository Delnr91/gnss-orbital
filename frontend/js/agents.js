// APEX-1 Agent Network — declarative sub-agent registry over markdown shards.
//
// Patterns at play:
//   Registry      — agents/manifest.json declares every sub-agent and its domain
//   Strategy      — each sub-agent searches only its own document shard
//   Chain of Resp.— guard -> router -> specialist -> flat-vault fallback
//
// No LLM involved: answers come exclusively from the project's curated
// markdown knowledge base, scored with keyword/section heuristics.

const AgentNetwork = (function () {
    "use strict";

    let manifest = null;
    let ready = false;

    const STOP_WORDS = [
        "the", "a", "an", "and", "or", "but", "to", "of", "in", "on", "at", "for", "with", "is", "are", "what", "how", "show", "explain",
        "el", "la", "los", "las", "un", "una", "y", "o", "de", "en", "para", "con", "es", "son", "que", "qué", "como", "cómo", "muestra", "explica",
        "的", "了", "和", "是", "在", "什么", "如何"
    ];

    async function init() {
        try {
            const res = await fetch("agents/manifest.json");
            if (!res.ok) throw new Error("manifest fetch failed");
            manifest = await res.json();
        } catch (e) {
            // Offline / file:// — network degrades to the inline vault search
            manifest = null;
            return;
        }

        // Pull the markdown shards for every language and merge them into the vault
        const langs = Object.keys(typeof vaultDocuments === "object" ? vaultDocuments : {});
        const jobs = [];
        langs.forEach((lang) => {
            (manifest.kb_files || []).forEach((file) => {
                jobs.push(
                    fetch(`kb/${lang}/${file}`)
                        .then((r) => (r.ok ? r.text() : null))
                        .then((text) => { if (text) vaultDocuments[lang][file] = text; })
                        .catch(() => { /* shard unavailable — skip silently */ })
                );
            });
        });
        await Promise.all(jobs);
        ready = true;
    }

    function tokenize(query) {
        const tokens = query
            .toLowerCase()
            .split(/[\s,\.\?\!\-\/\(\)（），。？！]+/)
            .filter((t) => t.length > 1 && !STOP_WORDS.includes(t));
        return tokens.length ? tokens : [query.toLowerCase()];
    }

    // Scores one document's sections (split on '## ' headers) against tokens
    function scoreSections(content, tokens) {
        let bestSection = null;
        let bestScore = 0;

        content.split(/(?=## )/g).forEach((section) => {
            const headerMatch = section.match(/##\s*(.*)/);
            const headerText = headerMatch ? headerMatch[1].toLowerCase() : "";
            const bodyText = section.toLowerCase();

            let score = 0;
            tokens.forEach((token) => {
                if (headerText.includes(token)) score += 4.5;
                if (bodyText.includes(token)) {
                    const safe = token.replace(/[-\/\\^$*+?.()|[\]{}]/g, "\\$&");
                    const count = (bodyText.match(new RegExp(safe, "g")) || []).length;
                    score += Math.min(count, 3);
                }
            });

            if (score > bestScore) {
                bestScore = score;
                bestSection = section;
            }
        });

        return { section: bestSection, score: bestScore };
    }

    // Router: pick the specialist whose keyword domain best matches the query
    function pickAgent(query) {
        const q = query.toLowerCase();
        let best = null;
        let bestScore = 0;

        (manifest.agents || []).forEach((agent) => {
            let s = 0;
            agent.keywords.forEach((k) => {
                if (q.includes(k)) s += k.length > 3 ? 2 : 1;
            });
            if (s > bestScore) { bestScore = s; best = agent; }
        });

        return bestScore > 0 ? best : null;
    }

    // Full dispatch. Returns:
    //   { agent, doc, section, score }  — specialist answered from its shard
    //   { agent, escalate: true }       — specialist matched but shard was weak
    //   null                            — network unavailable or no agent matched
    function route(query, lang) {
        if (!manifest || !ready) return null;

        const agent = pickAgent(query);
        if (!agent) return null;

        const docs = (typeof vaultDocuments === "object" && vaultDocuments[lang]) || {};
        const tokens = tokenize(query);

        let best = { section: null, score: 0, doc: "" };
        agent.docs.forEach((name) => {
            const content = docs[name];
            if (!content) return;
            const r = scoreSections(content, tokens);
            if (r.score > best.score) best = { section: r.section, score: r.score, doc: name };
        });

        const threshold = manifest.offtopic_threshold || 1.2;
        if (best.score < threshold) return { agent: agent, escalate: true };

        return { agent: agent, doc: best.doc, section: best.section, score: best.score };
    }

    return {
        init: init,
        route: route,
        tokenize: tokenize,
        scoreSections: scoreSections,
        isReady: function () { return ready; },
        getManifest: function () { return manifest; }
    };
})();

// Explicit window binding: `const` does not create a window property,
// and app.js feature-detects via `window.AgentNetwork`.
window.AgentNetwork = AgentNetwork;
