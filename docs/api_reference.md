# API Reference: gnss-orbital-py

This document provides documentation for the public classes, functions, and interfaces exposed by the `orbital` package.

---

## 1. Package Entry Point: `orbital`

Clients should import all primary classes and functions directly from the package facade:

```python
from orbital import solve_kepler_equation, OrbitalPropagator, OrbitPlotter
```

---

## 2. Kepler Mathematical Solvers

### `solve_kepler_equation`

```python
def solve_kepler_equation(
    M: numpy.typing.ArrayLike,
    e: float,
    tol: float = 1e-10,
    max_iter: int = 100
) -> numpy.ndarray:
```
Solves Kepler's equation $M = E - e \sin E$ using the Newton-Raphson numerical method.
- **Parameters**:
  - `M`: Mean anomaly (in radians). Can be a scalar or a NumPy array.
  - `e`: Eccentricity of the orbit ($0 \le e < 1$).
  - `tol`: Absolute convergence tolerance.
  - `max_iter`: Maximum number of iterations.
- **Returns**: Eccentric anomaly $E$ in radians.
- **Raises**:
  - `ValueError`: If eccentricity or numerical parameters are invalid.
  - `ConvergenceError`: If Newton-Raphson fails to converge.

### `true_anomaly_from_eccentric`

```python
def true_anomaly_from_eccentric(
    E: numpy.typing.ArrayLike,
    e: float
) -> numpy.ndarray:
```
Converts eccentric anomaly $E$ to true anomaly $\nu$.
- **Returns**: True anomaly in radians in the range $[0, 2\pi)$.

---

## 3. Orbit Propagation

### `OrbitalPropagator`

```python
class OrbitalPropagator:
    def __init__(
        self,
        a: float,
        e: float,
        i: float,
        raan: float,
        argp: float,
        nu0: float,
        mu: float = MU_EARTH,
        strategy: Optional[PropagationStrategy] = None
    ) -> None:
```
Manages classical orbital elements and propagates them using a pluggable strategy.
- **Properties**:
  - `a`: Semi-major axis (km).
  - `e`: Eccentricity.
  - `i`: Inclination (degrees).
  - `elements`: Underlying `OrbitalElements` data structure.
- **Methods**:
  - `period() -> float`: Returns the orbital period (seconds).
  - `orbital_velocity(r: float) -> float`: Returns the velocity (km/s) at distance $r$ (km).
  - `propagate(t_span: float, num_points: int = 500) -> Tuple[np.ndarray, np.ndarray, np.ndarray]`: Propagates the orbit over a duration `t_span` (seconds) and returns $X, Y, Z$ positions in ECI frame.
  - `summary(lang: str = None) -> str`: Returns a localized string summary of orbital parameters.

---

## 4. Visualization Engine

### `OrbitPlotter`

```python
class OrbitPlotter:
    def __init__(self, locale: Optional[Locale] = None) -> None:
```
Plots 3D interactive visualizations of trajectories using Plotly.
- **Methods**:
  - `create_earth_sphere(radius: float = EARTH_RADIUS, num_points: int = 50) -> go.Surface`: Returns a single surface trace representing Earth.
  - `plot_orbit(propagator: OrbitalPropagator, title: Optional[str] = None, show_earth: bool = True, color: str = "red", num_points: int = 500) -> go.Figure`: Plots a single orbit path and satellite position.
  - `plot_comparison(propagators: Sequence[OrbitalPropagator], names: Optional[List[str]] = None, colors: Optional[List[str]] = None, title: Optional[str] = None, show_earth: bool = True, num_points: int = 500) -> go.Figure`: Plots multiple orbits side-by-side.

---

## 5. Backward Compatibility (Spanish Interface)

The following Spanish aliases are exposed directly from `orbital` and correspond to their English counterparts:

- `resolver_ecuacion_kepler` $\to$ `solve_kepler_equation`
- `anomalia_verdadera_desde_excentrica` $\to$ `true_anomaly_from_eccentric`
- `anomalia_media` $\to$ `mean_anomaly`
- `movimiento_medio` $\to$ `mean_motion`
- `PropagadorOrbital` $\to$ `OrbitalPropagator`
- `crear_orbita_leo` $\to$ `create_leo_orbit`
- `crear_orbita_meo` $\to$ `create_meo_orbit`
- `crear_orbita_geo` $\to$ `create_geo_orbit`
- `crear_orbita_heo` $\to$ `create_heo_orbit`
- `crear_esfera_tierra` $\to$ `create_earth_sphere`
- `graficar_orbita_3d` $\to$ `plot_orbit_3d`
- `graficar_multiples_orbitas` $\to$ `plot_multiple_orbits`
