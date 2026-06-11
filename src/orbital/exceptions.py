"""Custom exception classes for the orbital dynamics package.

This module defines a clear exception hierarchy to handle mathematical, physical,
and configuration errors gracefully.
"""


class OrbitalError(Exception):
    """Base exception class for all errors in the orbital library."""
    pass


class ConvergenceError(OrbitalError):
    """Exception raised when numerical methods (e.g., Newton-Raphson) fail to converge."""
    pass


class InvalidElementsError(OrbitalError):
    """Exception raised when orbital elements violate physical boundaries."""
    pass


class SubsurfaceOrbitError(InvalidElementsError):
    """Exception raised when orbital parameters result in a trajectory that intersects Earth."""
    pass
