# 🧠 ENGRAM — Memoria Viva del Proyecto APEX-1

> Un *engram* es la huella física que deja un recuerdo. Este archivo es la huella del
> proyecto: qué se construyó, por qué, en qué orden, y qué sigue. **Toda sesión de
> trabajo (humana o de agente IA) debe leer este archivo primero y actualizarlo al
> terminar.** Es la fuente de verdad del hilo narrativo del proyecto.

---

## Identidad

| | |
|---|---|
| **Nombre** | APEX-1 — Plataforma educativa de mecánica orbital y GNSS |
| **Misión** | Aprender mecánica orbital *mirando e interactuando*: librería Python rigurosa + cubierta web inmersiva |
| **Audiencia** | Estudiantes de ingeniería espacial, autodidactas, público de divulgación |
| **Idiomas** | en / es / zh — en TODO (librería, web, docs, errores) |
| **Estética** | Palantir/NASA: slate casi monocromo, un acento cian disciplinado, ámbar solo para warnings |

## Principios de diseño (no negociables)

1. **El chat NO usa LLM.** APEX-1 responde exclusivamente desde la base de conocimiento
   markdown curada del proyecto, enrutada por agentes y sub-agentes declarados en
   `frontend/agents/manifest.json`. Contexto pequeño y coherente, estilo scikit-learn docs.
2. **El frontend funciona 100% estático** (GitHub Pages): la física del simulador está
   duplicada en JS a propósito. El backend FastAPI es opcional, no requisito.
3. **La sección del agente es un organismo vivo digital**: líquido, respira, emite
   frecuencias, reacciona, expresa emoción. Nunca degradarla a un chatbot con avatar.
4. **Cada error de validación se traduce** (claves en `locales/*.json`), porque los
   errores también enseñan.
5. **Patrón antes que parche**: si una segunda implementación no encaja en el patrón
   existente (Strategy, Registry…), se rediseña el patrón, no se mete un `if`.

---

## Fases construidas (el hilo)

### Fase 0 — Génesis (pre-2026-06)
Librería Python (`src/orbital`): solver de Kepler Newton-Raphson vectorizado, elementos
clásicos, propagador kepleriano (patrón Strategy), visualización Plotly, i18n Registry,
gamificación local, notebooks 01-03, docs trilingües en `docs/`. Frontend "Academy Deck
2050" con Three.js. Sin commits, sin tests corriendo, varios bugs latentes.

### Fase 1 — Cimientos (2026-06-11) · commit `5366c80`
- **Fix i18n**: `_locales_dir` apuntaba a `src/locales` (inexistente) → búsqueda ascendente.
- **Fix backend**: llamadas a métodos extintos `periodo()/propagar()` → `period()/propagate()`.
- **Fix packaging/tests**: mapeo src-layout en `pyproject.toml` + `pythonpath` pytest → 10/10 verdes.
- Limpieza: scripts one-off → `archive/`, notebooks vacíos eliminados, `.gitignore` ampliado.
- **Commit inicial** del repo (y se descubrió/neutralizó un repo git accidental en el HOME
  del usuario, creado por Git GUI; protección `GIT_CEILING_DIRECTORIES` instalada).

### Fase 2 — El Núcleo Viviente (2026-06-11)
- `frontend/js/orb.js`: orbe líquido por **shader GPU** (ruido simplex 3D desplazando
  vértices), halo fresnel, anillo de 96 barras de frecuencia, máquina de estados
  idle/listening/thinking/speaking, parallax al cursor, ondas al click.
- Chat con revelado progresivo por bloques + **KaTeX** (se arregló corrupción de TeX en
  `documents.js`: template literals → `String.raw`).
- Paleta Palantir en `:root`, Research Console de Jupyter con detección de kernel.
- Vocabulario del filtro anti-troll ampliado (el chip Vis-Viva era auto-rechazado).

### Fase 3 — Red de Agentes + Organismo Pleno (2026-06-11, esta fase)
- **J2Propagation** (`src/orbital/orbits.py`): segunda estrategia real del patrón Strategy.
  Tasas seculares analíticas (regresión nodal, rotación apsidal, deriva de M) + 6 tests
  (sun-synchronous ≈ 0.9856°/día, inclinación crítica 63.43°, divergencia vs kepleriano).
- **Red de agentes** (`frontend/agents/manifest.json` + `frontend/js/agents.js`):
  6 sub-agentes (KEPLER, GNSS, PERTURB, IRIS2, MISSION, SPACECRAFT) con dominios de
  keywords y shards de documentos. Cadena: guard → router → especialista → fallback plano.
  El chat muestra "ROUTED VIA <agente>" con el color del especialista.
- **KB ampliada**: 12 documentos nuevos en `frontend/kb/{en,es,zh}/` — maniobras y
  transferencias, sistemas de satélite, entorno espacial, operaciones de misión.
- **Emociones del orbe**: `ApexOrb.emote('happy')` — rebote líquido amortiguado
  (squash & stretch), bloom dorado, ráfaga triple de ondas; bobbing flotante permanente.
  Se dispara cuando el agente encuentra respuesta.
- **Chat a pantalla completa**: el organismo + nombre quedan como capa ambiental detrás
  del chat translúcido.
- **Fondo nuevo sin video**: se eliminó `background.mp4` (tenía watermark de Veo) →
  fondo 3D procedural: 3 capas de estrellas con parallax y twinkle, nebulosas
  procedurales, estrellas fugaces ocasionales.
- **Fix Multi-Orbit View**: causa raíz = `getElementById("orbital-controls")` sobre un
  elemento inexistente (TypeError abortaba el modo) + líneas de órbita rotadas con
  `rotation.set` incorrecto. Ahora las líneas se trazan con la MISMA transformación que
  los satélites (`getCartesianPosition`), cámara auto-encuadra al apogeo máximo,
  etiquetas con nombre/color por satélite proyectadas contra el rect real del canvas.
- **Satélite procedural estilo NASA**: bus dorado MLI metálico, alas solares con textura
  de celdas, antena de alta ganancia que apunta a la Tierra (`lookAt`), radiador, beacon
  parpadeante.
- **CI**: `.github/workflows/ci.yml` (pytest matrix 3.10/3.12 + lint advisory) y
  `pages.yml` (deploy automático de `frontend/` a GitHub Pages). Badges en README.
- Bug sutil cazado: `const AgentNetwork` no crea `window.AgentNetwork` → binding
  explícito al final de `agents.js`.

### Fase 4 — El Universo Vivo (2026-06-11)
- **Tierra blue-marble**: se retiró el filtro grayscale. Decisión de diseño documentada:
  *el chrome de la UI se queda muted (Palantir slate), el CONTENIDO — el planeta — va a
  todo color*; ese contraste es la mejor práctica de los mission displays. Texturas NASA
  (color + relieve normal + especular oceánico + capa de nubes independiente rotando),
  limbo atmosférico con shader fresnel azul, rig de luz de dos fuentes (sol cálido +
  relleno frío espacial).
- **Universo bio-IA de fondo**: capa "plexo" — 46 células bioluminiscentes errantes que
  crean y disuelven enlaces sinápticos por proximidad, con latido (heartbeat) global.
  Conviven con estrellas parallax, nebulosas y fugaces. El proyecto *se siente vivo*.
- **Organismo más presente**: bug encontrado — el `backdrop-filter: blur(18px)` de la
  regla base seguía difuminando al orbe tras el chat; anulado con `backdrop-filter: none`
  (la legibilidad ahora viene del fondo sólido de cada burbuja). Estado idle más
  enérgico, micro-pulsos espontáneos cada 2.6-6.4 s, deriva bacteriana lissajous,
  brillo/saturación del canvas subidos.
- **Lógica Jupyter ops-grade**: click en OPEN NOTEBOOK sin kernel ya no abre pestañas
  muertas → status "KERNEL REQUIRED", panel del comando parpadea en ámbar, y un
  auto-poll de 4 s conecta y embebe JupyterLab en cuanto el operador lo lanza.
- Nota operativa: si `preview_screenshot` se cuelga con la página viva, reiniciar el
  servidor de preview (es el pipeline de captura, no la app).

---

## Arquitectura y patrones (mapa rápido)

```
src/orbital/          ← librería Python (la verdad física)
  kepler.py             solver Newton-Raphson vectorizado
  orbits.py             OrbitalPropagator + Strategy: KeplerianPropagation | J2Propagation
  i18n.py               Locale (Registry + Singleton-por-idioma, fallback en)
  types.py              dataclasses congeladas (OrbitalElements, PropagationResult)
  visualization.py      Plotly (Facade + Template Method)
  gamification.py       logros locales (Observer-ish)
src/backend/main.py   ← FastAPI opcional (TF-IDF chat + API de propagación)
frontend/
  agents/manifest.json  Registry declarativo de sub-agentes
  js/agents.js          Router (Chain of Responsibility: guard→router→especialista→fallback)
  js/orb.js             organismo shader (máquina de estados + capa de emociones)
  js/app.js             controlador del deck (simulador, chat, jupyter console, i18n UI)
  kb/{en,es,zh}/        shards markdown de la red de agentes
docs/                 ← teoría trilingüe (fuente del vault del backend TF-IDF)
tests/                ← pytest (16 tests: kepler, orbits, i18n, j2)
```

Patrones: **Strategy** (propagadores), **Registry** (Locale, manifest de agentes),
**Chain of Responsibility** (pipeline del chat), **Facade** (visualization),
**Template Method** (plots), **State Machine** (orbe).

## Convenciones

- Commits con mensaje en inglés, cuerpo explicando el porqué.
- Ángulos en la API pública: **grados**; internamente: radianes.
- Unidades: km, s, rad/s. Nada de unidades mezcladas sin sufijo.
- Todo string visible al usuario pasa por i18n (JS: `translations`, Py: `Locale.t`).
- Los docs KB usan secciones `## ` — el scoring del router depende de ello.

---

## Próximas fases (backlog priorizado)

1. **Ground tracks**: proyección de la órbita sobre mapa 2D con rotación terrestre
   (`EARTH_ROTATION_RATE` ya existe). EL gráfico pedagógico que falta.
2. **Visualizar J2 en el deck**: toggle "J2 ON/OFF" en el simulador mostrando la
   precesión de RAAN (la librería ya lo calcula; falta portar las tasas a JS).
3. **TLEs reales** (CelesTrak) en el Multi-Orbit View: de juguete a herramienta.
4. **Visibilidad/DOP por ciudad**: lat/lon del usuario → satélites GNSS visibles + GDOP.
5. **PyPI** (`pip install gnss-orbital-py`) + badges Binder/Colab en notebooks.
6. **Validación contra Skyfield/poliastro** en tests de regresión (<1 km).
7. **Gamificación en el deck web**: logros visibles en la UI.

## Deudas conocidas

- `src/backend/main.py` (TF-IDF) y la red de agentes JS son dos cerebros paralelos;
  unificar criterios de scoring cuando el backend se use en serio.
- `mypy` está en modo advisory en CI; endurecer cuando se tipen los módulos UI.
- El simulador JS duplica fórmulas de `kepler.py` (decisión consciente, ver Principio 2)
  — si se toca la física, tocar AMBOS lados.

> **Última actualización**: 2026-06-11 · Fase 4 completada.
