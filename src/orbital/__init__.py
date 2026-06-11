"""Keplerian Orbital Dynamics Educational Package.

Exposes a clean API for solving Kepler's equation, defining orbits,
and producing 3D interactive visualizations. Supports English, Spanish,
and Chinese locales.
"""

from .i18n import Locale
from .exceptions import (
    OrbitalError,
    ConvergenceError,
    InvalidElementsError,
    SubsurfaceOrbitError,
)
from .types import OrbitType, OrbitalElements, PropagationResult
from .gamification import Achievement, ProgressTracker
from .constants import (
    MU_EARTH,
    EARTH_RADIUS,
    J2_EARTH,
    EARTH_ROTATION_RATE,
    G,
    EARTH_MASS,
    MU_TIERRA,
    RADIO_TIERRA,
    J2_TIERRA,
    OMEGA_TIERRA,
    MASA_TIERRA,
)
from .kepler import (
    solve_kepler_equation,
    true_anomaly_from_eccentric,
    mean_anomaly,
    mean_motion,
    resolver_ecuacion_kepler,
    anomalia_verdadera_desde_excentrica,
    anomalia_media,
    movimiento_medio,
)
from .orbits import (
    PropagationStrategy,
    KeplerianPropagation,
    OrbitalPropagator,
    create_leo_orbit,
    create_meo_orbit,
    create_geo_orbit,
    create_heo_orbit,
    PropagadorOrbital,
    crear_orbita_leo,
    crear_orbita_meo,
    crear_orbita_geo,
    crear_orbita_heo,
)
from .visualization import (
    OrbitPlotter,
    create_earth_sphere,
    plot_orbit_3d,
    plot_multiple_orbits,
    crear_esfera_tierra,
    graficar_orbita_3d,
    graficar_multiples_orbitas,
)
from .teacher import SpaceTeacher, create_teacher_workspace

__all__ = [
    # Internationalization & Exceptions
    "Locale",
    "OrbitalError",
    "ConvergenceError",
    "InvalidElementsError",
    "SubsurfaceOrbitError",
    
    # Types & Dataclasses
    "OrbitType",
    "OrbitalElements",
    "PropagationResult",
    "Achievement",
    "ProgressTracker",
    
    # Constants
    "MU_EARTH",
    "EARTH_RADIUS",
    "J2_EARTH",
    "EARTH_ROTATION_RATE",
    "G",
    "EARTH_MASS",
    "MU_TIERRA",
    "RADIO_TIERRA",
    "J2_TIERRA",
    "OMEGA_TIERRA",
    "MASA_TIERRA",
    
    # Kepler Mathematical Solvers
    "solve_kepler_equation",
    "true_anomaly_from_eccentric",
    "mean_anomaly",
    "mean_motion",
    "resolver_ecuacion_kepler",
    "anomalia_verdadera_desde_excentrica",
    "anomalia_media",
    "movimiento_medio",
    
    # Orbits Definition & Propagation
    "PropagationStrategy",
    "KeplerianPropagation",
    "OrbitalPropagator",
    "create_leo_orbit",
    "create_meo_orbit",
    "create_geo_orbit",
    "create_heo_orbit",
    "PropagadorOrbital",
    "crear_orbita_leo",
    "crear_orbita_meo",
    "crear_orbita_geo",
    "crear_orbita_heo",
    
    # Visualization Engines
    "OrbitPlotter",
    "create_earth_sphere",
    "plot_orbit_3d",
    "plot_multiple_orbits",
    "crear_esfera_tierra",
    "graficar_orbita_3d",
    "graficar_multiples_orbitas",
    
    # Teacher & Obsidian Companion
    "SpaceTeacher",
    "create_teacher_workspace",
]
