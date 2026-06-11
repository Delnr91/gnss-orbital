#!/usr/bin/env python3
"""Example: Solving Kepler's Equation.

Demonstrates the numerical solution of Kepler's equation M = E - e*sin(E)
using the Newton-Raphson method and plots anomaly relationships.
Accepts a --lang CLI argument.
"""

import argparse
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from orbital import solve_kepler_equation, true_anomaly_from_eccentric, Locale


def main() -> None:
    parser = argparse.ArgumentParser(description="Kepler Equation Solver Example.")
    parser.add_argument(
        "--lang",
        type=str,
        default="en",
        help="Language for logs and plots (en, es, zh).",
    )
    args = parser.parse_args()

    locale = Locale(args.lang)

    print("================================================================")
    print("Kepler's Equation Solver")
    print("================================================================")

    # Solve for multiple eccentricities
    M_vals = np.linspace(0, 2 * np.pi, 500)
    eccentricities = [0.0, 0.2, 0.5, 0.7, 0.9]

    fig = make_subplots(
        rows=1,
        cols=2,
        subplot_titles=(
            "Eccentric Anomaly E vs Mean Anomaly M",
            "True Anomaly nu vs Mean Anomaly M",
        ),
    )

    colors = ["#00ff88", "#ff6b35", "#ffd700", "#ff1493", "#00bfff"]

    for e, color in zip(eccentricities, colors):
        E_vals = np.array([solve_kepler_equation(M, e) for M in M_vals])
        nu_vals = np.array([true_anomaly_from_eccentric(E, e) for E in E_vals])
        nu_vals = np.unwrap(nu_vals)

        fig.add_trace(
            go.Scatter(
                x=np.degrees(M_vals),
                y=np.degrees(E_vals),
                name=f"e = {e}",
                line=dict(color=color, width=2),
                legendgroup=f"e{e}",
            ),
            row=1,
            col=1,
        )

        fig.add_trace(
            go.Scatter(
                x=np.degrees(M_vals),
                y=np.degrees(nu_vals),
                name=f"e = {e}",
                line=dict(color=color, width=2, dash="dash"),
                legendgroup=f"e{e}",
                showlegend=False,
            ),
            row=1,
            col=2,
        )

        val_pi = solve_kepler_equation(np.pi, e)
        print(f"e = {e}: E(M=pi) = {np.degrees(val_pi):.2f} deg")

    fig.update_layout(
        template="plotly_dark",
        height=500,
        font=dict(family="Inter, sans-serif"),
    )
    fig.show()


if __name__ == "__main__":
    main()
