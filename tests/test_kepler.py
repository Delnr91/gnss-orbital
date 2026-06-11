import numpy as np
import pytest
from orbital.kepler import solve_kepler_equation, true_anomaly_from_eccentric
from orbital.exceptions import ConvergenceError


def test_solve_kepler_circular() -> None:
    # For e=0, E must equal M
    M = np.linspace(0, 2 * np.pi, 100)
    E = solve_kepler_equation(M, 0.0)
    np.testing.assert_allclose(E, M, atol=1e-12)


def test_solve_kepler_eccentric() -> None:
    M = np.pi / 4
    e = 0.5
    E = solve_kepler_equation(M, e)
    # Validate E - e*sin(E) = M
    res = E - e * np.sin(E)
    assert abs(res - M) < 1e-10


def test_invalid_eccentricity() -> None:
    with pytest.raises(ValueError):
        solve_kepler_equation(0.5, 1.2)
    with pytest.raises(ValueError):
        solve_kepler_equation(0.5, -0.1)


def test_true_anomaly_conversion() -> None:
    E = 0.0
    nu = true_anomaly_from_eccentric(E, 0.5)
    assert abs(nu) < 1e-12

    E_pi = np.pi
    nu_pi = true_anomaly_from_eccentric(E_pi, 0.5)
    assert abs(nu_pi - np.pi) < 1e-12
