# APEX-1 Agent Network Architecture

APEX-1's chat does **not** use an LLM. It answers exclusively from the project's curated
markdown knowledge base, dispatched through a declarative network of sub-agents. The goal
is scikit-learn-style documentation answers with a small, coherent context — served like a
bot, auditable like a library.

## The pipeline (Chain of Responsibility)

```
 user query
     │
     ▼
 ┌─────────────┐   off-domain    ┌──────────────────────┐
 │ 1. GUARD    │ ──────────────▶ │ rejection message    │
 │ keyword     │                 └──────────────────────┘
 │ gate        │
 └─────┬───────┘
       │ on-domain
       ▼
 ┌─────────────┐   no agent      ┌──────────────────────┐
 │ 2. ROUTER   │ ──────────────▶ │ 4. FLAT FALLBACK     │
 │ scores each │                 │ search whole vault   │
 │ sub-agent's │                 └──────────────────────┘
 │ keyword     │                          ▲
 │ domain      │                          │ weak shard (escalate)
 └─────┬───────┘                          │
       │ best specialist                  │
       ▼                                  │
 ┌─────────────┐                          │
 │ 3. SPECIALIST│ ────────────────────────┘
 │ searches ONLY│
 │ its own docs │──▶ answer + "ROUTED VIA <agent>" tag
 └─────────────┘
```

Every stage can pass the query down the chain; the user always gets an answer or an
honest "no match".

## The Registry: `frontend/agents/manifest.json`

Each sub-agent is pure data — no code changes needed to add one:

```json
{
  "id": "PERTURB",
  "icon": "≋",
  "color": "#8d87d8",
  "name": { "en": "Perturbations", "es": "Perturbaciones", "zh": "轨道摄动" },
  "keywords": ["j2", "drag", "precession", "sun-synchronous", "..."],
  "docs": ["orbital_perturbations.md", "space_environment.md"]
}
```

- **keywords** define the agent's routing domain (trilingual, substring-matched).
- **docs** is the agent's *shard*: the only documents it searches. Small shard = coherent
  answers, no context bleed between domains.
- `kb_files` lists markdown shards fetched at runtime from `frontend/kb/<lang>/` and
  merged into the inline vault (`documents.js`), so the deck still works from `file://`
  (without the extra shards) and fully on GitHub Pages.

## Scoring (the "backend of answers")

1. **Router score** per agent: +2 per matched keyword (>3 chars), +1 otherwise.
2. **Section score** inside the shard: documents are split on `##` headers; header hits
   weigh 4.5, body term frequency is capped at 3 per token. The best section wins.
3. Below `offtopic_threshold` (manifest, default 1.2) the specialist *escalates* to the
   flat vault search, keeping its routing tag for transparency.

The reply is rendered as Markdown + KaTeX, revealed block-by-block while the living core
is in its `speaking` state; a successful match triggers the core's `happy` emotion.

## Design patterns in the network

| Pattern | Where | Why |
|---|---|---|
| Registry | `manifest.json` | add/retire agents without touching code |
| Strategy | each sub-agent = a search strategy over its shard | swap scoring per domain later |
| Chain of Responsibility | guard → router → specialist → fallback | graceful degradation, always answers |
| State Machine | `orb.js` (idle/listening/thinking/speaking + emotion overlay) | the UI *is* the agent's body |
| Facade | `AgentNetwork` public API (`init`, `route`) | app.js never sees scoring internals |

## Mirror in Python

`src/backend/main.py` offers the same idea server-side (TF-IDF over `docs/*.md` with
scikit-learn). The JS network is the canonical implementation because the deck must run
fully static; keep their thresholds aligned if the backend goes live (see ENGRAM —
known debts).

## Adding a new sub-agent (checklist)

1. Write the markdown shard(s) in `frontend/kb/en|es|zh/<topic>.md` using `##` sections.
2. Add the filename to `kb_files` in the manifest.
3. Declare the agent: id, icon, color, trilingual name, keywords (include es/zh terms!),
   and its `docs` list.
4. If the topic introduces new vocabulary, extend `spaceKeywords` in `app.js` so the
   guard lets the queries through.
5. Update ENGRAM.md.
