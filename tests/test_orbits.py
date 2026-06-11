import pytest
from orbital.orbits import OrbitalPropagator, create_leo_orbit
from orbital.exceptions import SubsurfaceOrbitError


def test_propagator_properties() -> None:
    # ISS LEO orbit
    prop = create_leo_orbit(altitude=400, inclination=51.6)
    assert prop.a == 6371.0 + 400.0
    assert prop.e == 0.0006
    assert prop.i == 51.6


def test_propagator_period() -> None:
    prop = create_leo_orbit(altitude=400, inclination=51.6)
    period = prop.period()
    # Expected LEO period is around 5500-5600 seconds (~92.4 minutes)
    assert 5500 < period < 5600


def test_subsurface_orbit_error() -> None:
    # Perigee must be above Earth surface (6371.0 km)
    # If a=6000 and e=0, perigee = 6000 < 6371, should raise error
    with pytest.raises(SubsurfaceOrbitError):
        OrbitalPropagator(a=6000.0, e=0.0, i=0.0, raan=0.0, argp=0.0, nu0=0.0)
