"""Type definitions and data structures for orbital dynamics.

This module defines the primary data structures, enums, and type hints
used across the orbital dynamics library.
"""

from dataclasses import dataclass
from enum import Enum
import numpy as np


class OrbitType(Enum):
    """Supported earth orbit classifications."""
    LEO = "leo"
    MEO = "meo"
    GEO = "geo"
    HEO = "heo"



@dataclass(frozen=True)
class OrbitalElements:
    """Classical Keplerian orbital elements.

    Attributes:
        semi_major_axis: Semi-major axis of the orbit in kilometers.
        eccentricity: Eccentricity of the orbit (dimensionless, 0 <= e < 1).
        inclination: Inclination in degrees (0 <= i <= 180).
        raan: Right Ascension of the Ascending Node in degrees (0 <= raan < 360).
        argument_of_periapsis: Argument of periapsis in degrees (0 <= argp < 360).
        true_anomaly: True anomaly in degrees (0 <= nu < 360).
    """
    semi_major_axis: float
    eccentricity: float
    inclination: float
    raan: float
    argument_of_periapsis: float
    true_anomaly: float

    def __post_init__(self) -> None:
        if self.semi_major_axis <= 0:
            raise ValueError(f"Semi-major axis must be positive. Received: {self.semi_major_axis}")
        if not (0.0 <= self.eccentricity < 1.0):
            raise ValueError(f"Eccentricity must satisfy 0 <= e < 1. Received: {self.eccentricity}")
        if not (0.0 <= self.inclination <= 180.0):
            raise ValueError(f"Inclination must be between 0 and 180 degrees. Received: {self.inclination}")


@dataclass(frozen=True)
class PropagationResult:
    """Result of orbital propagation over a time series.

    Attributes:
        x: Array of X coordinates in the ECI frame (km).
        y: Array of Y coordinates in the ECI frame (km).
        z: Array of Z coordinates in the ECI frame (km).
        time: Array of time steps since reference epoch (s).
        elements: Reference orbital elements at the starting epoch.
    """
    x: np.ndarray
    y: np.ndarray
    z: np.ndarray
    time: np.ndarray
    elements: OrbitalElements
