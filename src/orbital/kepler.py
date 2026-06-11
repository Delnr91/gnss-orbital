"""Algorithms for solving Kepler's equation and anomaly conversions.

This module implements the core mathematical and numerical algorithms required
to solve Kepler's equation:

    M = E - e*sin(E)

where M is mean anomaly, E is eccentric anomaly, and e is eccentricity.
Vectorized operations are supported using NumPy.
"""

from __future__ import annotations

import numpy as np
import numpy.typing as npt

from .constants import MU_EARTH
from .exceptions import ConvergenceError
from .i18n import Locale

_ArrayLike = npt.ArrayLike


def solve_kepler_equation(
    M: _ArrayLike,
    e: float,
    tol: float = 1e-10,
    max_iter: int = 100,
) -> np.ndarray:
    """Solves Kepler's equation using the Newton-Raphson method.

    Finds the eccentric anomaly E for a given mean anomaly M and eccentricity e.
    Supports both scalar inputs and NumPy arrays.

    Args:
        M: Mean anomaly in radians.
        e: Orbital eccentricity (0 <= e < 1).
        tol: Convergence tolerance.
        max_iter: Maximum number of iterations.

    Returns:
        Eccentric anomaly in radians.

    Raises:
        ValueError: If eccentricity or numerical parameters are invalid.
        ConvergenceError: If Newton-Raphson fails to converge.
    """
    locale = Locale()

    if not (0.0 <= e < 1.0):
        raise ValueError(locale.t("errors.eccentricity_range", e=e))
    if tol <= 0:
        raise ValueError(locale.t("errors.tolerance_positive", tol=tol))
    if max_iter < 1:
        raise ValueError(locale.t("errors.max_iter_positive", max_iter=max_iter))

    M_arr = np.asarray(M, dtype=np.float64)
    is_scalar = M_arr.ndim == 0
    M_arr = np.atleast_1d(M_arr)

    # Initial guess: E0 = M + e*sin(M) for e < 0.8
    E = M_arr + e * np.sin(M_arr)

    for iteration in range(max_iter):
        f_E = E - e * np.sin(E) - M_arr
        f_prime_E = 1.0 - e * np.cos(E)
        delta = f_E / f_prime_E
        E = E - delta

        if np.all(np.abs(delta) < tol):
            return float(E[0]) if is_scalar else E  # type: ignore[return-value]

    raise ConvergenceError(
        locale.t("errors.kepler_convergence", max_iter=max_iter, tol=tol)
    )


def true_anomaly_from_eccentric(
    E: _ArrayLike,
    e: float,
) -> np.ndarray:
    """Converts eccentric anomaly to true anomaly.

    Uses the half-angle tangent relation to map anomalies correctly:
    tan(nu/2) = sqrt((1 + e) / (1 - e)) * tan(E/2)

    Args:
        E: Eccentric anomaly in radians.
        e: Orbital eccentricity (0 <= e < 1).

    Returns:
        True anomaly in radians in range [0, 2pi).
    """
    locale = Locale()

    if not (0.0 <= e < 1.0):
        raise ValueError(locale.t("errors.eccentricity_range", e=e))

    E_arr = np.asarray(E, dtype=np.float64)
    is_scalar = E_arr.ndim == 0
    E_arr = np.atleast_1d(E_arr)

    factor = np.sqrt((1.0 + e) / (1.0 - e))
    nu = 2.0 * np.arctan2(
        factor * np.sin(E_arr / 2.0),
        np.cos(E_arr / 2.0),
    )

    # Normalize to [0, 2pi)
    nu = nu % (2.0 * np.pi)

    return float(nu[0]) if is_scalar else nu  # type: ignore[return-value]


def mean_anomaly(
    n: float,
    t: _ArrayLike,
    t0: float = 0.0,
) -> np.ndarray:
    """Computes mean anomaly over time.

    M = n * (t - t0)

    Args:
        n: Mean motion in rad/s.
        t: Time(s) in seconds.
        t0: Time of periapsis passage in seconds.

    Returns:
        Mean anomaly in radians.
    """
    if n <= 0:
        locale = Locale()
        raise ValueError(locale.t("errors.mean_motion_positive", n=n))

    t_arr = np.asarray(t, dtype=np.float64)
    is_scalar = t_arr.ndim == 0
    t_arr = np.atleast_1d(t_arr)

    M = n * (t_arr - t0)

    return float(M[0]) if is_scalar else M  # type: ignore[return-value]


def mean_motion(
    a: float,
    mu: float = MU_EARTH,
) -> float:
    """Calculates mean motion from semi-major axis.

    n = sqrt(mu / a^3)

    Args:
        a: Semi-major axis in km.
        mu: Gravitational parameter in km^3/s^2.

    Returns:
        Mean motion in rad/s.
    """
    locale = Locale()

    if a <= 0:
        raise ValueError(locale.t("errors.semi_major_positive", a=a))
    if mu <= 0:
        raise ValueError(locale.t("errors.mu_positive", mu=mu))

    return float(np.sqrt(mu / a**3))


# ====================================================================
# Backward-Compatible Spanish Aliases
# ====================================================================
resolver_ecuacion_kepler = solve_kepler_equation
anomalia_verdadera_desde_excentrica = true_anomaly_from_eccentric
anomalia_media = mean_anomaly
movimiento_medio = mean_motion
