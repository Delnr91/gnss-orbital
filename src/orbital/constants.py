"""Fundamental physical and astronomical constants for orbital mechanics.

This module defines planetary parameters for Earth and universal constants
in standard units (km, kg, s).
"""

# Earth standard gravitational parameter [km^3/s^2]
# Product of universal gravitational constant G and Earth mass M. (EGM2008 / WGS-84)
MU_EARTH: float = 398600.4418

# Earth mean equatorial radius [km] (WGS-84)
EARTH_RADIUS: float = 6371.0

# Earth J2 zonal geopotential coefficient [dimensionless]
# Describes planetary oblateness causing secular perturbations.
J2_EARTH: float = 1.08263e-3

# Earth angular rotation rate [rad/s] (sidereal rotation)
EARTH_ROTATION_RATE: float = 7.2921159e-5

# Universal gravitational constant [km^3/(kg*s^2)]
G: float = 6.674e-20

# Earth mass [kg]
EARTH_MASS: float = 5.972e24


# ====================================================================
# Backward-Compatible Spanish Aliases
# ====================================================================
MU_TIERRA = MU_EARTH
RADIO_TIERRA = EARTH_RADIUS
J2_TIERRA = J2_EARTH
OMEGA_TIERRA = EARTH_ROTATION_RATE
MASA_TIERRA = EARTH_MASS
