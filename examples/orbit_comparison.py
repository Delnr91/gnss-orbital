#!/usr/bin/env python3
"""Example: Comparison of Earth Orbit Types.

Creates LEO, MEO, GEO, and HEO orbits, displays their parameters in a table,
and renders a 3D comparison plot using Plotly. Accepts a --lang CLI argument.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from orbital import (
    create_leo_orbit,
    create_meo_orbit,
    create_geo_orbit,
    create_heo_orbit,
    plot_multiple_orbits,
    Locale,
)


def main() -> None:
    parser = argparse.ArgumentParser(description="Orbit Comparison Example.")
    parser.add_argument(
        "--lang",
        type=str,
        default="en",
        help="Language for logs and plots (en, es, zh).",
    )
    args = parser.parse_args()

    locale = Locale(args.lang)

    print("================================================================")
    print(locale.t("ui.title_multi_orbit"))
    print("================================================================")

    leo = create_leo_orbit(altitude=408.0, inclination=51.6)
    meo = create_meo_orbit(altitude=20200.0, inclination=55.0)
    geo = create_geo_orbit(longitude=0.0)
    heo = create_heo_orbit(perigee_alt=500.0, apogee_alt=39000.0, inclination=63.4)

    # Show parameters comparison table
    print(f"\n{locale.t('orbit_types.leo')}: a={leo.a:.1f} km, e={leo.e:.4f}, i={leo.i:.1f} deg, T={leo.period()/3600:.2f} h")
    print(f"{locale.t('orbit_types.meo')}: a={meo.a:.1f} km, e={meo.e:.4f}, i={meo.i:.1f} deg, T={meo.period()/3600:.2f} h")
    print(f"{locale.t('orbit_types.geo')}: a={geo.a:.1f} km, e={geo.e:.4f}, i={geo.i:.1f} deg, T={geo.period()/3600:.2f} h")
    print(f"{locale.t('orbit_types.heo')}: a={heo.a:.1f} km, e={heo.e:.4f}, i={heo.i:.1f} deg, T={heo.period()/3600:.2f} h")

    # Generate 3D plot
    fig = plot_multiple_orbits(
        [leo, meo, geo, heo],
        nombres=[
            locale.t("orbit_types.leo"),
            locale.t("orbit_types.meo"),
            locale.t("orbit_types.geo"),
            locale.t("orbit_types.heo"),
        ],
        colores=["#00ff88", "#ff6b35", "#ffd700", "#ff1493"],
        titulo=locale.t("ui.title_multi_orbit"),
    )
    fig.show()


if __name__ == "__main__":
    main()
