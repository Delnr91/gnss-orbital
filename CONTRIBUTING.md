# Contributing to APEX-1

First off — thank you. APEX-1 is open source (MIT) and built to be **taken, learned from, and improved**. Whether you fix a typo, translate a string, or implement a real J2-perturbed ground track, you're welcome here.

> 🌍 Contributions in **English, Español, or 中文** are all welcome — in issues, PRs, and docs.

---

## 🧭 Read this first

The project keeps a living memory file: [`docs/ENGRAM.md`](docs/ENGRAM.md). It records **what was built, why, in what order, and what's next**. Read it before starting — it's the fastest way to understand the project's intent and conventions. The runtime agent network is documented in [`docs/agent_architecture.md`](docs/agent_architecture.md).

## ⚙️ Local setup

**Frontend (zero install)** — the web deck is fully static:

```bash
git clone https://github.com/Delnr91/gnss-orbital.git
cd gnss-orbital
python -m http.server 3000 --directory frontend
# open http://localhost:3000
```

**Python library + tests:**

```bash
pip install -e ".[dev]"     # numpy, plotly, ipywidgets + pytest, mypy
pytest                      # 16 tests should pass
```

**Optional backend / Jupyter:** `./scripts/start.ps1` (Windows) launches JupyterLab + the FastAPI backend together.

## 📐 Principles (please keep these)

1. **The chat agent does not use an LLM.** APEX-1 answers only from curated Markdown in `frontend/kb/` + `frontend/documents.js`, routed by the declarative sub-agent registry in `frontend/agents/manifest.json`. Keep context small, coherent, and auditable.
2. **The frontend must run 100% static** (GitHub Pages / Vercel). The Python physics is intentionally mirrored in JS — if you change the math, change **both** sides.
3. **Everything user-facing is trilingual** (en / es / zh). New strings go in all three: JS `translations`, Python `Locale` (`locales/*.json`).
4. **Pattern before patch.** A second implementation should fit the existing pattern (Strategy for propagators, Registry for agents) — if it doesn't, refactor the pattern rather than adding a special case.

## 🌱 Good first contributions

The prioritized backlog lives in [`docs/ENGRAM.md`](docs/ENGRAM.md#próximas-fases-backlog-priorizado). Highlights, roughly easiest → deepest:

- **Add a translation** — extend `frontend/kb/<lang>/` or `locales/*.json`.
- **Add a sub-agent** — write a Markdown shard + one entry in `frontend/agents/manifest.json` (see `docs/agent_architecture.md`, "Adding a new sub-agent").
- **Ground tracks** — project the orbit onto a 2D rotating Earth map (`EARTH_ROTATION_RATE` already exists).
- **Visualize J2 in the deck** — port the existing `J2Propagation` secular rates to JS and add a toggle to see RAAN precession.
- **Real TLEs** from CelesTrak in the Multi-Orbit View.
- **GNSS visibility / GDOP** from a user's lat-lon.
- **PyPI packaging** + Binder/Colab badges on the notebooks.

## 🔀 Pull requests

- Branch off `main`; keep PRs focused on one thing.
- Run `pytest` before opening — CI runs the suite on Python 3.10 and 3.12.
- Match the surrounding code style (comment density, naming, idiom).
- Describe the *why* in the PR body. Screenshots/GIFs help for UI changes.
- New physics? Add a test. New user-facing string? Add all three languages.

## 🐛 Issues

Found a bug or have an idea? Open an issue with steps to reproduce (and your browser / device for frontend issues — the WebGL deck is tested on desktop, mobile, and iPad). "Good first issue" candidates are drawn from the ENGRAM backlog.

---

Built with ☕ by [Lattice Startup](https://lattices.cl). Be kind, ship things, and aim for the stars. 🚀
