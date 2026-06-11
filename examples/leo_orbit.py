#!/usr/bin/env python3
"""Example: LEO Orbit Simulation (International Space Station).

Demonstrates defining, propagating, and plotting a Low Earth Orbit
using the orbital dynamics package. Accepts a --lang CLI argument.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from orbital import create_leo_orbit, plot_orbit_3d, Locale, EARTH_RADIUS


def main() -> None:
    parser = argparse.ArgumentParser(description="LEO Orbit Simulation.")
    parser.add_argument(
        "--lang",
        type=str,
        default="en",
        help="Language for logs and plots (en, es, zh).",
    )
    args = parser.parse_args()

    locale = Locale(args.lang)

    print("================================================================")
    print(locale.t("ui.title_orbit_simulation"))
    print("================================================================")

    # Create LEO orbit (ISS altitude ~408 km, inclination 51.6 deg)
    leo = create_leo_orbit(altitude=408.0, inclination=51.6)

    # Print summary
    print(leo.summary(args.lang))

    # Calculate additional parameters
    period = leo.period()
    alt = leo.a - EARTH_RADIUS
    r_perigeo = leo.a * (1.0 - leo.e)
    v_perigeo = leo.orbital_velocity(r_perigeo)

    print(f"\n{locale.t('meta.language')} Logs:")
    print(f"  {locale.t('orbit.period')}: {period:.1f} s ({period/60:.1f} min)")
    print(f"  {locale.t('orbit.perigee_altitude')}: {alt:.1f} km")
    print(f"  {locale.t('orbit.velocity_at_perigee')}: {v_perigeo:.3f} km/s")

    # Generate 3D plot
    fig = plot_orbit_3d(
        leo,
        titulo=locale.t("ui.title_orbit_simulation"),
        color="#00ff88",
        num_puntos=800,
    )
    fig.show()


if __name__ == "__main__":
    main()
