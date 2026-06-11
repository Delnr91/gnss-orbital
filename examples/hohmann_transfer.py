#!/usr/bin/env python3
"""Example: Hohmann Transfer Orbit Calculation.

Calculates the delta-v requirements and time of flight for a Hohmann transfer
from a circular LEO (altitude 400 km) to a circular GEO (altitude 35786 km).
Accepts a --lang CLI argument.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import numpy as np
import plotly.graph_objects as go

from orbital import (
    create_leo_orbit,
    create_geo_orbit,
    OrbitalPropagator,
    plot_multiple_orbits,
    Locale,
    MU_EARTH,
    EARTH_RADIUS,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Hohmann Transfer Calculator.")
    parser.add_argument(
        "--lang",
        type=str,
        default="en",
        help="Language for logs and plots (en, es, zh).",
    )
    args = parser.parse_args()

    locale = Locale(args.lang)

    print("================================================================")
    print("Hohmann Transfer Orbit Calculator")
    print("================================================================")

    # Initial and final radii
    r1 = EARTH_RADIUS + 400.0  # LEO
    r2 = 42164.0  # GEO

    # Velocities in circular orbits
    vc1 = np.sqrt(MU_EARTH / r1)
    vc2 = np.sqrt(MU_EARTH / r2)

    # Transfer ellipse semi-major axis
    a_tx = (r1 + r2) / 2.0
    e_tx = (r2 - r1) / (r1 + r2)

    # Velocities on the transfer ellipse
    v_tx1 = np.sqrt(MU_EARTH * (2.0 / r1 - 1.0 / a_tx))
    v_tx2 = np.sqrt(MU_EARTH * (2.0 / r2 - 1.0 / a_tx))

    # Delta-v burns
    dv1 = v_tx1 - vc1
    dv2 = vc2 - v_tx2
    total_dv = dv1 + dv2

    # Time of flight (half of the transfer orbit period)
    tof = np.pi * np.sqrt(a_tx**3 / MU_EARTH)

    print(f"Initial LEO Radius: {r1:.1f} km (velocity: {vc1:.3f} km/s)")
    print(f"Final GEO Radius: {r2:.1f} km (velocity: {vc2:.3f} km/s)")
    print(f"Transfer Semi-Major Axis: {a_tx:.1f} km (eccentricity: {e_tx:.4f})")
    print(f"First Burn (LEO to Transfer): Delta-V = {dv1:.3f} km/s")
    print(f"Second Burn (Transfer to GEO): Delta-V = {dv2:.3f} km/s")
    print(f"Total Delta-V required: {total_dv:.3f} km/s")
    print(f"Time of Flight: {tof:.1f} s ({tof/60:.1f} min or {tof/3600:.2f} hours)")

    # Create orbits to plot
    leo = create_leo_orbit(altitude=400.0, inclination=0.0)
    geo = create_geo_orbit(longitude=0.0)
    
    # Custom transfer orbit propagator
    # We define it starting at perigee (nu=0)
    transfer = OrbitalPropagator(a=a_tx, e=e_tx, i=0.0, raan=0.0, argp=0.0, nu0=0.0)

    fig = plot_multiple_orbits(
        [leo, geo, transfer],
        nombres=["LEO Orbit", "GEO Orbit", "Hohmann Transfer Orbit"],
        colores=["#00ff88", "#ffd700", "#ff1493"],
        titulo="Hohmann Transfer Trajectory",
    )
    fig.show()


if __name__ == "__main__":
    main()
