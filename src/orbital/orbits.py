"""Orbits definition, propagation strategies, and orbit factory methods.

This module implements the core Keplerian orbit representation and uses the
Strategy design pattern to allow different propagation algorithms.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Tuple, Optional

import numpy as np
import numpy.typing as npt

from .constants import MU_EARTH, EARTH_RADIUS
from .exceptions import SubsurfaceOrbitError
from .i18n import Locale
from .kepler import (
    anomalia_media,
    anomalia_verdadera_desde_excentrica,
    movimiento_medio,
    resolver_ecuacion_kepler,
)
from .types import OrbitalElements, PropagationResult

_DOS_PI = 2.0 * np.pi


class PropagationStrategy(ABC):
    """Abstract base class for orbit propagation strategies."""

    @abstractmethod
    def propagate(
        self,
        elements: OrbitalElements,
        t_span: float,
        num_points: int,
        mu: float,
    ) -> PropagationResult:
        """Propagates an orbit over a time duration.

        Args:
            elements: Initial Keplerian elements.
            t_span: Propagation duration in seconds.
            num_points: Number of steps to compute.
            mu: Planet gravitational parameter.

        Returns:
            A PropagationResult containing coordinates and time steps.
        """
        pass


class KeplerianPropagation(PropagationStrategy):
    """Two-body Keplerian analytical orbit propagation."""

    def propagate(
        self,
        elements: OrbitalElements,
        t_span: float,
        num_points: int,
        mu: float,
    ) -> PropagationResult:
        locale = Locale()

        if t_span <= 0:
            raise ValueError(locale.t("errors.t_span_positive", t_span=t_span))

        n = movimiento_medio(elements.semi_major_axis, mu)

        # Initial eccentric anomaly from initial true anomaly
        nu0_rad = np.radians(elements.true_anomaly)
        e = elements.eccentricity
        
        # Safe tangent evaluation for quadrant mapping
        E0 = 2.0 * np.arctan2(
            np.sqrt(1.0 - e) * np.sin(nu0_rad / 2.0),
            np.sqrt(1.0 + e) * np.cos(nu0_rad / 2.0),
        )
        M0 = E0 - e * np.sin(E0)

        # Time vector
        t = np.linspace(0.0, t_span, num_points)

        # Propagate anomalies
        M = anomalia_media(n, t) + M0
        E = resolver_ecuacion_kepler(M, e)
        nu_rad = anomalia_verdadera_desde_excentrica(E, e)

        # Compute position vectors
        x, y, z = self._positions_from_nu(elements, nu_rad)

        return PropagationResult(
            x=x,
            y=y,
            z=z,
            time=t,
            elements=elements,
        )

    def _positions_from_nu(
        self,
        elements: OrbitalElements,
        nu_rad: np.ndarray,
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Calculates cartesian coordinates in ECI frame for a vector of true anomalies."""
        a = elements.semi_major_axis
        e = elements.eccentricity
        i_rad = np.radians(elements.inclination)
        raan_rad = np.radians(elements.raan)
        argp_rad = np.radians(elements.argument_of_periapsis)

        p = a * (1.0 - e**2)
        r = p / (1.0 + e * np.cos(nu_rad))

        x_pqw = r * np.cos(nu_rad)
        y_pqw = r * np.sin(nu_rad)

        cos_O, sin_O = np.cos(raan_rad), np.sin(raan_rad)
        cos_i, sin_i = np.cos(i_rad), np.sin(i_rad)
        cos_w, sin_w = np.cos(argp_rad), np.sin(argp_rad)

        r11 = cos_O * cos_w - sin_O * sin_w * cos_i
        r21 = sin_O * cos_w + cos_O * sin_w * cos_i
        r31 = sin_w * sin_i

        r12 = -cos_O * sin_w - sin_O * cos_w * cos_i
        r22 = -sin_O * sin_w + cos_O * cos_w * cos_i
        r32 = cos_w * sin_i

        x = r11 * x_pqw + r12 * y_pqw
        y = r21 * x_pqw + r22 * y_pqw
        z = r31 * x_pqw + r32 * y_pqw

        return x, y, z


class OrbitalPropagator:
    """Propagator for satellite orbits.

    Allows definining classical orbital elements and propagates them using
    an interchangeable propagation strategy.
    """

    def __init__(
        self,
        a: float,
        e: float,
        i: float,
        raan: float,
        argp: float,
        nu0: float,
        mu: float = MU_EARTH,
        strategy: Optional[PropagationStrategy] = None,
    ) -> None:
        locale = Locale()

        # Check for subsurface orbit
        perigee = a * (1.0 - e)
        if perigee < EARTH_RADIUS:
            raise SubsurfaceOrbitError(
                locale.t("errors.subsurface_orbit", perigee=perigee - EARTH_RADIUS, radius=EARTH_RADIUS)
            )

        self._elements = OrbitalElements(
            semi_major_axis=a,
            eccentricity=e,
            inclination=i,
            raan=raan,
            argument_of_periapsis=argp,
            true_anomaly=nu0,
        )
        self.mu = mu
        self.strategy = strategy or KeplerianPropagation()

    @property
    def a(self) -> float:
        """Semi-major axis in km."""
        return self._elements.semi_major_axis

    @property
    def e(self) -> float:
        """Eccentricity."""
        return self._elements.eccentricity

    @property
    def i(self) -> float:
        """Inclination in degrees."""
        return self._elements.inclination

    @property
    def i_rad(self) -> float:
        """Inclination in radians (backward compatibility attribute)."""
        return np.radians(self._elements.inclination)

    @property
    def raan_rad(self) -> float:
        """RAAN in radians (backward compatibility attribute)."""
        return np.radians(self._elements.raan)

    @property
    def argp_rad(self) -> float:
        """Argument of periapsis in radians (backward compatibility attribute)."""
        return np.radians(self._elements.argument_of_periapsis)

    @property
    def nu0_rad(self) -> float:
        """Initial true anomaly in radians (backward compatibility attribute)."""
        return np.radians(self._elements.true_anomaly)

    @property
    def elements(self) -> OrbitalElements:
        """The underlying OrbitalElements dataclass."""
        return self._elements

    def period(self) -> float:
        """Calculates orbital period in seconds."""
        return _DOS_PI * np.sqrt(self.a**3 / self.mu)

    def orbital_velocity(self, r: float) -> float:
        """Calculates the orbital velocity at a distance r using the vis-viva equation."""
        locale = Locale()
        if r <= 0:
            raise ValueError(locale.t("errors.radius_positive", r=r))
        val = self.mu * (2.0 / r - 1.0 / self.a)
        if val < 0:
            raise ValueError("Radial distance yields imaginary velocity.")
        return float(np.sqrt(val))

    def get_position(self, nu: npt.ArrayLike) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Calculates ECI Cartesian position for a given true anomaly (in radians)."""
        nu_arr = np.atleast_1d(np.asarray(nu, dtype=np.float64))
        
        # Instantiate a temporary KeplerianPropagation to calculate PQW rotation
        temp_strat = KeplerianPropagation()
        x, y, z = temp_strat._positions_from_nu(self._elements, nu_arr)
        
        if np.asarray(nu).ndim == 0:
            return x[0], y[0], z[0]
        return x, y, z

    def propagate(self, t_span: float, num_points: int = 500) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """Propagates orbit over time using the configured strategy."""
        res = self.strategy.propagate(self._elements, t_span, num_points, self.mu)
        return res.x, res.y, res.z

    def summary(self, lang: Optional[str] = None) -> str:
        """Generates a multilingual text summary of the orbit."""
        locale = Locale(lang)
        T = self.period()
        rp = self.a * (1.0 - self.e)
        ra = self.a * (1.0 + self.e)
        alt_p = rp - EARTH_RADIUS
        alt_a = ra - EARTH_RADIUS
        vp = self.orbital_velocity(rp)
        va = self.orbital_velocity(ra)

        lines = [
            "================================================",
            f"  {locale.t('ui.title_orbit_simulation').upper()}",
            "------------------------------------------------",
            f"  {locale.t('orbit.semi_major_axis')} (a)      : {self.a:>12.3f} km",
            f"  {locale.t('orbit.eccentricity')} (e)      : {self.e:>12.6f}",
            f"  {locale.t('orbit.inclination')} (i)        : {self.i:>12.4f}°",
            f"  RAAN (Ω)              : {self._elements.raan:>12.4f}°",
            f"  {locale.t('orbit.argument_of_periapsis')} (ω)  : {self._elements.argument_of_periapsis:>12.4f}°",
            f"  {locale.t('orbit.true_anomaly')} (ν₀)  : {self._elements.true_anomaly:>12.4f}°",
            "------------------------------------------------",
            f"  {locale.t('orbit.period')}        : {T:>12.2f} s",
            f"                         : {T / 60:>12.2f} min",
            f"  {locale.t('orbit.perigee_altitude')}     : {alt_p:>12.3f} km",
            f"  {locale.t('orbit.apogee_altitude')}      : {alt_a:>12.3f} km",
            f"  {locale.t('orbit.velocity_at_perigee')}   : {vp:>12.4f} km/s",
            f"  {locale.t('orbit.velocity_at_apogee')}    : {va:>12.4f} km/s",
            "================================================",
        ]
        return "\n".join(lines)

    def info(self) -> str:
        """Prints and returns orbit summary (for backwards compatibility)."""
        res = self.summary()
        print(res)
        return res

    def __repr__(self) -> str:
        return (
            f"OrbitalPropagator(a={self.a}, e={self.e}, i={self.i}°, "
            f"raan={self._elements.raan}°, argp={self._elements.argument_of_periapsis}°, "
            f"nu0={self._elements.true_anomaly}°)"
        )


# ======================================================================
# Factory functions for typical earth orbits
# ======================================================================

def create_leo_orbit(
    altitude: float = 400.0,
    inclination: float = 51.6,
    raan: float = 0.0,
    argument_of_periapsis: float = 0.0,
    true_anomaly: float = 0.0,
    mu: float = MU_EARTH,
) -> OrbitalPropagator:
    """Creates a Low Earth Orbit (LEO) propagator."""
    a = EARTH_RADIUS + altitude
    e = 0.0006
    return OrbitalPropagator(
        a=a,
        e=e,
        i=inclination,
        raan=raan,
        argp=argument_of_periapsis,
        nu0=true_anomaly,
        mu=mu,
    )


def create_meo_orbit(
    altitude: float = 20200.0,
    inclination: float = 55.0,
    raan: float = 0.0,
    argument_of_periapsis: float = 0.0,
    true_anomaly: float = 0.0,
    mu: float = MU_EARTH,
) -> OrbitalPropagator:
    """Creates a Medium Earth Orbit (MEO) propagator."""
    a = EARTH_RADIUS + altitude
    e = 0.01
    return OrbitalPropagator(
        a=a,
        e=e,
        i=inclination,
        raan=raan,
        argp=argument_of_periapsis,
        nu0=true_anomaly,
        mu=mu,
    )


def create_geo_orbit(
    longitude: float = 0.0,
    raan: float = 0.0,
    argument_of_periapsis: float = 0.0,
    true_anomaly: float = 0.0,
    mu: float = MU_EARTH,
) -> OrbitalPropagator:
    """Creates a Geostationary Earth Orbit (GEO) propagator."""
    a = 42164.0
    e = 0.0001
    i = 0.01
    return OrbitalPropagator(
        a=a,
        e=e,
        i=i,
        raan=raan,
        argp=argument_of_periapsis,
        nu0=true_anomaly,
        mu=mu,
    )


def create_heo_orbit(
    perigee_alt: float = 500.0,
    apogee_alt: float = 39000.0,
    inclination: float = 63.4,
    raan: float = 0.0,
    argument_of_periapsis: float = 270.0,
    true_anomaly: float = 0.0,
    mu: float = MU_EARTH,
) -> OrbitalPropagator:
    """Creates a Highly Elliptical Orbit (HEO) propagator (e.g. Molniya)."""
    locale = Locale()
    if perigee_alt >= apogee_alt:
        raise ValueError(
            locale.t("errors.perigee_apogee_order", perigee=perigee_alt, apogee=apogee_alt)
        )
    rp = EARTH_RADIUS + perigee_alt
    ra = EARTH_RADIUS + apogee_alt
    a = (rp + ra) / 2.0
    e = (ra - rp) / (ra + rp)

    return OrbitalPropagator(
        a=a,
        e=e,
        i=inclination,
        raan=raan,
        argp=argument_of_periapsis,
        nu0=true_anomaly,
        mu=mu,
    )


# ======================================================================
# Backward-Compatible Spanish Aliases
# ======================================================================
PropagadorOrbital = OrbitalPropagator
crear_orbita_leo = create_leo_orbit
crear_orbita_meo = create_meo_orbit
crear_orbita_geo = create_geo_orbit
crear_orbita_heo = create_heo_orbit
