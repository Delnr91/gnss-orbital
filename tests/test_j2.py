import numpy as np
import pytest

from orbital.constants import EARTH_RADIUS
from orbital.orbits import (
    J2Propagation,
    KeplerianPropagation,
    OrbitalPropagator,
    j2_secular_rates,
)


def test_sun_synchronous_nodal_regression() -> None:
    # An 800 km SSO at i=98.6 deg must regress ~+0.9856 deg/day to track the Sun
    a = EARTH_RADIUS + 800.0
    raan_dot, _, _ = j2_secular_rates(a, 0.0, 98.6)
    deg_per_day = np.degrees(raan_dot) * 86400.0
    assert 0.85 < deg_per_day < 1.10


def test_critical_inclination_freezes_periapsis() -> None:
    # At i = arccos(sqrt(1/5)) the apsidal rotation vanishes (Molniya design)
    i_crit = np.degrees(np.arccos(np.sqrt(0.2)))
    _, argp_dot, _ = j2_secular_rates(26561.0, 0.74, i_crit)
    assert abs(argp_dot) < 1e-12


def test_polar_orbit_has_no_nodal_drift() -> None:
    raan_dot, _, _ = j2_secular_rates(7000.0, 0.001, 90.0)
    assert abs(raan_dot) < 1e-15


def test_j2_propagation_diverges_from_keplerian() -> None:
    # After many orbits the J2 trajectory must visibly drift away from two-body
    prop = OrbitalPropagator(a=7000.0, e=0.01, i=51.6, raan=40.0, argp=30.0, nu0=0.0)
    T = prop.period()
    t_span = 30.0 * T

    kep = KeplerianPropagation().propagate(prop.elements, t_span, 500, prop.mu)
    j2 = J2Propagation().propagate(prop.elements, t_span, 500, prop.mu)

    final_gap = np.sqrt(
        (kep.x[-1] - j2.x[-1]) ** 2
        + (kep.y[-1] - j2.y[-1]) ** 2
        + (kep.z[-1] - j2.z[-1]) ** 2
    )
    assert final_gap > 10.0  # km

    # Orbit shape is preserved: radius stays within the Keplerian bounds
    r_j2 = np.sqrt(j2.x**2 + j2.y**2 + j2.z**2)
    rp = 7000.0 * (1 - 0.01)
    ra = 7000.0 * (1 + 0.01)
    assert np.all(r_j2 > rp - 5.0)
    assert np.all(r_j2 < ra + 5.0)


def test_j2_strategy_pluggable_into_propagator() -> None:
    # Strategy pattern: the propagator accepts the J2 strategy transparently
    prop = OrbitalPropagator(
        a=7000.0, e=0.001, i=98.6, raan=0.0, argp=0.0, nu0=0.0,
        strategy=J2Propagation(),
    )
    x, y, z = prop.propagate(prop.period(), num_points=100)
    assert len(x) == 100 and np.all(np.isfinite(x + y + z))


def test_j2_rejects_invalid_t_span() -> None:
    prop = OrbitalPropagator(a=7000.0, e=0.001, i=51.6, raan=0.0, argp=0.0, nu0=0.0)
    with pytest.raises(ValueError):
        J2Propagation().propagate(prop.elements, -10.0, 100, prop.mu)
