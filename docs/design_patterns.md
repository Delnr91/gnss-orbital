# Design Patterns Reference: gnss-orbital-py

This document provides a detailed overview of the software engineering design patterns implemented in the `gnss-orbital-py` package, including UML-like structural flows and code snippets.

---

## 1. Strategy Pattern (Orbit Propagation)

The Strategy pattern decouples the `OrbitalPropagator` class from the mathematical propagation algorithm. This structure allows us to swap the analytical Keplerian solver with numerical perturbation solvers (like J2 oblateness, atmospheric drag, or solar radiation pressure) dynamically at runtime.

### Structural Diagram

```
+-----------------------------------+
|         OrbitalPropagator         |
|-----------------------------------|
| - elements: OrbitalElements       |
| - strategy: PropagationStrategy   |
|-----------------------------------|
| + propagate(t_span): xyz          |
+-----------------------------------+
                  | (delegates to)
                  v
+-----------------------------------------------+
|         <<interface>> PropagationStrategy    |
|-----------------------------------------------|
| + propagate(elements, t_span, mu): Result     |
+-----------------------------------------------+
                  ^
                  | (implements)
         +--------+--------+
         |                 |
+------------------+ +------------------+
|KeplerianPropag.  | |J2PerturbPropag.  |
|                  | | (Future extension|
+------------------+ +------------------+
```

### Implementation Example

```python
from orbital import OrbitalPropagator, KeplerianPropagation

# Instantiate an orbit using the default Keplerian analytical strategy
propagator = OrbitalPropagator(a=7000, e=0.01, i=51.6, raan=0, argp=0, nu0=0,
                               strategy=KeplerianPropagation())

# To swap propagation algorithms, pass a different strategy instance
# propagator.strategy = NumericalJ2Propagation()
```

---

## 2. Template Method Pattern (3D Visualizations)

The Template Method pattern defines the algorithm skeleton for generating interactive 3D plots in the base `OrbitPlotter` class. It defers specific styling or decoration details to subclass hooks or configuration parameters.

### Structural Flow

1. **Calculate Trajectory**: Compute propagation steps.
2. **Add Earth Surface (Hook)**: Draw Earth sphere if enabled.
3. **Add Orbit Line (Hook)**: Draw line trace.
4. **Add Satellite Position (Hook)**: Draw marker at epoch position.
5. **Configure Layout (Hook)**: Set colors, axes labels, title, and initial camera viewport.

By overriding hooks like `create_earth_sphere` or `configure_layout`, developers can create stylized plots (e.g., stylized GNSS constellations) while retaining the core plot-building algorithm.

---

## 3. Observer Pattern (Gamification Challenges)

The Observer pattern is used to implement achievement tracking. When notebooks or CLI example scripts execute educational challenges, they record completion flags via the `ProgressTracker` subject. The tracker automatically notifies and unlocks badges based on requirements.

### Data Flow

```
[Challenge Cell in Notebook]
           |
           | 1. user completes challenge
           v
[ProgressTracker.record_action("solve_kepler")]
           |
           | 2. checks achievement registry
           v
[Unlock "kepler_solver" Badge]
           |
           | 3. save to progress.json
           v
[Display notification & update console progress]
```

---

## 4. Registry Pattern (Internationalization)

The `Locale` class acts as a global registry for translations. It loads local language files (`locales/*.json`) once and registers them in a class-level dictionary.

### Fallback Chain

If a translation key is missing in the requested language (e.g., Chinese), the registry automatically falls back:

$$\text{Requested Language (zh)} \longrightarrow \text{Default Language (en)} \longrightarrow \text{Raw Key String}$$

This structure guarantees that the library will not crash if a translator has not completed translations for newly added exceptions or messages.
