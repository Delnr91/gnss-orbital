# Keplerian Orbital Dynamics & 3D Interactive Laboratory
# Laboratorio Interactivo 3D y Dinámica Orbital Kepleriana

An open-source educational repository demonstrating Keplerian orbital mechanics, astrodynamics, design patterns, and internationalization (i18n) standards. Used for satellite systems modeling, including the European IRIS² constellation.

Una biblioteca educativa de código abierto que demuestra la mecánica orbital kepleriana, la astrodinámica, los patrones de diseño y las prácticas de internacionalización. Diseñado para el modelado de sistemas satelitales, incluyendo la constelación europea IRIS².

---

## 🚀 Key Features / Características Clave

### English
- **Kepler Solver**: High-precision numerical Kepler equation solver ($M = E - e \sin E$) using the Newton-Raphson method.
- **APEX-1 Living Core**: A GPU liquid-shader agent orb that listens, thinks and speaks — with a reactive frequency ring, live status protocol, and progressive "transmission" replies rendered with Markdown + KaTeX math.
- **3D Mission Deck**: Three.js WebGL simulator with orbit presets (LEO/MEO/GEO/HEO), live classical-element sliders, tactical telemetry, and a multi-orbit constellation view.
- **Research Console**: Jupyter launcher with notebook mission cards, automatic local-kernel detection, and embedded JupyterLab.
- **Multilingual Support**: Real-time localization registry supporting English, Spanish, and Chinese (Simplified) — across both the Python library and the web deck.
- **Interactive 3D Visualizations**: Interactive orbit plots utilizing Plotly and ipywidgets with a dark background theme and a semi-transparent Earth.
- **IRIS² Multi-Orbital Modeling**: Study of LEO/MEO hybrid constellations to analyze latency, coverage, and modern New Space architectures.
- **Software Design Patterns**: Clean implementation of Strategy, Template Method, Observer, Facade, and Registry design patterns.
- **Gamified Progression**: Local achievement system to track student progress through notebook challenges.

### Español
- **Solucionador de Kepler**: Solucionador numérico de alta precisión para la ecuación de Kepler ($M = E - e \sin E$) mediante Newton-Raphson.
- **Núcleo Viviente APEX-1**: Un orbe-agente líquido renderizado por shaders en GPU que escucha, piensa y habla — con anillo de frecuencias reactivo, protocolo de estado en vivo y respuestas en "transmisión" progresiva con Markdown + matemáticas KaTeX.
- **Cubierta de Misión 3D**: Simulador WebGL con Three.js, órbitas predefinidas (LEO/MEO/GEO/HEO), deslizadores de elementos clásicos, telemetría táctica y vista de constelación multi-órbita.
- **Consola de Investigación**: Lanzador de Jupyter con tarjetas de misión por cuaderno, detección automática del kernel local y JupyterLab integrado.
- **Soporte Multilingüe**: Registro de localización en tiempo real con soporte para inglés, español y chino (simplificado) — tanto en la librería Python como en la web.
- **Visualización 3D Interactiva**: Gráficas orbitales interactivas con Plotly e ipywidgets sobre fondo oscuro y una Tierra semitransparente.
- **Modelado Multi-Orbital IRIS²**: Estudio de constelaciones híbridas LEO/MEO para analizar latencia, cobertura y arquitecturas modernas de New Space.
- **Patrones de Diseño de Software**: Implementación clara de los patrones Strategy, Template Method, Observer, Facade y Registry.
- **Gamificación Progresiva**: Sistema local de logros para realizar un seguimiento del progreso del estudiante en los cuadernos.

---

## 🛠️ Technology Stack & Architecture / Stack Tecnológico y Arquitectura

### Technology Stack
- **Core**: Python 3.9+
- **Math & Numeric**: NumPy
- **Visuals & 3D**: Plotly
- **Widgets & Interactivity**: ipywidgets, JupyterLab
- **Testing**: pytest

### Architecture Layers / Capas de la Arquitectura
The library follows a layered design to separate core physics, presentation, and infrastructure:

1. **Domain Layer**: `kepler.py`, `orbits.py`, `constants.py`, `types.py`. Mathematical algorithms and physics rules.
2. **Application Layer**: `i18n.py` (Registry pattern), `gamification.py` (Observer pattern).
3. **Presentation Layer**: Jupyter Notebooks (`notebooks/`) and example CLI scripts (`examples/`).
4. **Infrastructure Layer**: Translation files (`locales/*.json`) and achievements schema (`assets/badges/*.json`).

For full details on design patterns, see [ARCHITECTURE.md](ARCHITECTURE.md) and [docs/design_patterns.md](docs/design_patterns.md).

---

## 📦 Installation / Instalación

```bash
# Clone the repository
git clone https://github.com/your-username/gnss-orbital-py.git
cd gnss-orbital-py

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install package in editable mode with development dependencies
pip install -e .
```

---

## 🎮 Quick Start / Inicio Rápido

### Run CLI Examples
You can run the examples from the command line. Use the `--lang` flag to specify your language (`en`, `es`, `zh`):

```bash
# LEO Orbit propagation
python examples/leo_orbit.py --lang es

# Orbit Comparison (LEO, MEO, GEO, HEO)
python examples/orbit_comparison.py --lang en
```

### Launch the APEX-1 Web Mission Deck
The full experience — liquid agent core, 3D simulator, and embedded JupyterLab:

```powershell
pip install -r requirements.txt
./scripts/start.ps1   # Windows: JupyterLab on :8888 + deck served at http://localhost:8000
```

Or serve the static deck alone (agent and simulator run fully in-browser):

```bash
python -m http.server 8000 --directory frontend
```

### Launch Jupyter Notebooks
Open the interactive notebooks to study the orbits visually:

```bash
jupyter lab
```

Then navigate to:
1. `notebooks/01_interactive_orbits.ipynb`: Visual study of classical orbital elements.
2. `notebooks/02_kepler_equation.ipynb`: In-depth solver convergence analysis.
3. `notebooks/03_iris2_constellation.ipynb`: Modeling the EU IRIS² multi-orbital constellation.

---

## 🏆 Achievements / Sistema de Logros

This project includes a local gamification engine. When you complete challenges in the notebooks, achievements are unlocked and stored in `~/.gnss-orbital/progress.json`.

- **Bronze: Orbit Explorer** - Successfully simulate a Low Earth Orbit.
- **Bronze: Keplerian Apprentice** - Solve Kepler's equation numerically for the first time.
- **Silver: Orbital Navigator** - Modify all 6 orbital elements and propagate the trajectory.
- **Silver: Trajectory Analyst** - Compare LEO, MEO, GEO, and HEO orbits side-by-side.
- **Gold: Space Pilot** - Design a Hohmann transfer orbit from LEO to GEO.
- **Master: IRIS2 Constellation Designer** - Model the complete IRIS² hybrid constellation.

---

## 📚 References & Resources / Referencias y Recursos

1. David A. Vallado, *Fundamentals of Astrodynamics and Applications*, 4th Edition.
2. Howard D. Curtis, *Orbital Mechanics for Engineering Students*, Elsevier.
3. European Commission, *IRIS²: Infrastructure for Resilience, Interconnection and Security by Satellite*.
4. CDIO Initiative: *Standards 2.0* for engineering education training.

---

## 📜 License / Licencia

Distributed under the MIT License. See `LICENSE` for details.
