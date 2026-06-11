"""3D interactive visualization engine for orbits using Plotly.

Implements the Template Method design pattern with the OrbitPlotter class,
allowing layout customization and full i18n support.
"""

from __future__ import annotations

from typing import List, Optional, Sequence, Tuple
import numpy as np
import plotly.graph_objects as go

from .constants import EARTH_RADIUS
from .i18n import Locale
from .orbits import OrbitalPropagator

_DEFAULT_COLORS: List[str] = [
    "cyan",
    "magenta",
    "#FF6F61",  # coral
    "#FFD700",  # gold
    "#00FF7F",  # spring green
    "#FF69B4",  # deep pink
    "#1E90FF",  # dodger blue
    "#FFA500",  # orange
]


class OrbitPlotter:
    """Plotly-based 3D orbit visualizer.

    Uses the Template Method pattern to define plot construction steps, allowing
    customization of trace styling and layout configuration.
    """

    def __init__(self, locale: Optional[Locale] = None) -> None:
        self.locale = locale or Locale()

    def create_earth_sphere(self, radius: float = EARTH_RADIUS, num_points: int = 50) -> go.Surface:
        """Creates a single Plotly Surface trace representing Earth.

        Fixes Bug 1 by returning a single go.Surface instance.
        """
        theta = np.linspace(0, np.pi, num_points)
        phi = np.linspace(0, 2 * np.pi, num_points)
        theta_grid, phi_grid = np.meshgrid(theta, phi)

        x = radius * np.sin(theta_grid) * np.cos(phi_grid)
        y = radius * np.sin(theta_grid) * np.sin(phi_grid)
        z = radius * np.cos(theta_grid)

        # Blue-green ocean color scale
        colorscale = [
            [0.0, "rgb(10, 40, 80)"],
            [0.3, "rgb(20, 80, 120)"],
            [0.5, "rgb(30, 120, 100)"],
            [0.7, "rgb(40, 160, 120)"],
            [1.0, "rgb(60, 200, 150)"],
        ]

        return go.Surface(
            x=x,
            y=y,
            z=z,
            colorscale=colorscale,
            surfacecolor=np.sqrt(x**2 + y**2),
            opacity=0.45,
            showscale=False,
            name=self.locale.t("ui.earth"),
            hoverinfo="skip",
        )

    def create_orbit_trace(
        self,
        x: np.ndarray,
        y: np.ndarray,
        z: np.ndarray,
        name: str,
        color: str,
    ) -> go.Scatter3d:
        """Creates a 3D Scatter line trace for the orbit path (extension hook)."""
        return go.Scatter3d(
            x=x,
            y=y,
            z=z,
            mode="lines",
            name=name,
            line=dict(color=color, width=4),
            hovertemplate=(
                f"<b>%{{fullData.name}}</b><br>"
                f"X: %{{x:.1f}} {self.locale.t('orbit.units.km')}<br>"
                f"Y: %{{y:.1f}} {self.locale.t('orbit.units.km')}<br>"
                f"Z: %{{z:.1f}} {self.locale.t('orbit.units.km')}<extra></extra>"
            ),
        )

    def create_satellite_marker(
        self,
        x0: float,
        y0: float,
        z0: float,
        name: str,
        color: str,
    ) -> go.Scatter3d:
        """Creates a diamond marker trace at the starting position (extension hook)."""
        return go.Scatter3d(
            x=[x0],
            y=[y0],
            z=[z0],
            mode="markers",
            marker=dict(size=6, color=color, symbol="diamond"),
            name=name,
            hovertemplate=(
                f"<b>{name}</b><br>"
                f"X: %{{x:.1f}} {self.locale.t('orbit.units.km')}<br>"
                f"Y: %{{y:.1f}} {self.locale.t('orbit.units.km')}<br>"
                f"Z: %{{z:.1f}} {self.locale.t('orbit.units.km')}<extra></extra>"
            ),
        )

    def configure_layout(self, fig: go.Figure, title: str, reference_range: float) -> None:
        """Configures the dark-themed Plotly layout for 3D graphs (extension hook)."""
        margin_size = reference_range * 1.3

        axis_config = dict(
            title_font=dict(size=13, color="white"),
            range=[-margin_size, margin_size],
            backgroundcolor="rgba(0,0,0,0)",
            gridcolor="rgba(80,80,80,0.3)",
            showbackground=True,
            zerolinecolor="rgba(120,120,120,0.4)",
        )

        fig.update_layout(
            template="plotly_dark",
            title=dict(
                text=title,
                font=dict(size=20, color="white"),
                x=0.5,
            ),
            scene=dict(
                xaxis=dict(**axis_config, title=self.locale.t("ui.axes.x")),
                yaxis=dict(**axis_config, title=self.locale.t("ui.axes.y")),
                zaxis=dict(**axis_config, title=self.locale.t("ui.axes.z")),
                aspectmode="cube",
                camera=dict(
                    eye=dict(x=1.5, y=1.5, z=1.0),
                    up=dict(x=0, y=0, z=1),
                ),
            ),
            legend=dict(
                font=dict(size=12, color="white"),
                bgcolor="rgba(0,0,0,0.5)",
                bordercolor="rgba(255,255,255,0.2)",
                borderwidth=1,
            ),
            margin=dict(l=0, r=0, t=50, b=0),
            paper_bgcolor="rgb(10,10,25)",
        )

    def plot_orbit(
        self,
        propagator: OrbitalPropagator,
        title: Optional[str] = None,
        show_earth: bool = True,
        color: str = "red",
        num_points: int = 500,
    ) -> go.Figure:
        """Template Method: Builds and returns a 3D Plotly figure for a single orbit."""
        T = propagator.period()
        x, y, z = propagator.propagate(T, num_points)

        traces: List[go.BaseTraceType] = []

        if show_earth:
            traces.append(self.create_earth_sphere())

        orbit_name = self.locale.t("ui.legend_orbit")
        traces.append(self.create_orbit_trace(x, y, z, name=orbit_name, color=color))

        sat_name = f"{self.locale.t('ui.satellite')} ({self.locale.t('orbit.true_anomaly')})"
        traces.append(self.create_satellite_marker(x[0], y[0], z[0], name=sat_name, color="yellow"))

        fig = go.Figure(data=traces)
        
        plot_title = title or self.locale.t("ui.title_orbit_simulation")
        self.configure_layout(fig, plot_title, propagator.a)

        return fig

    def plot_comparison(
        self,
        propagators: Sequence[OrbitalPropagator],
        names: Optional[List[str]] = None,
        colors: Optional[List[str]] = None,
        title: Optional[str] = None,
        show_earth: bool = True,
        num_points: int = 500,
    ) -> go.Figure:
        """Template Method: Builds and returns a 3D Plotly figure comparing multiple orbits."""
        n_orbits = len(propagators)
        if n_orbits == 0:
            raise ValueError("At least one propagator is required.")

        if names is None:
            names = [f"Orbit {k + 1}" for k in range(n_orbits)]
        if colors is None:
            colors = [_DEFAULT_COLORS[k % len(_DEFAULT_COLORS)] for k in range(n_orbits)]

        traces: List[go.BaseTraceType] = []

        if show_earth:
            traces.append(self.create_earth_sphere())

        max_val = 0.0
        for prop, name, color in zip(propagators, names, colors):
            T = prop.period()
            x, y, z = prop.propagate(T, num_points)
            traces.append(self.create_orbit_trace(x, y, z, name=name, color=color))

            sat_marker_name = f"{name} ({self.locale.t('ui.satellite')})"
            traces.append(self.create_satellite_marker(x[0], y[0], z[0], name=sat_marker_name, color=color))
            
            # Show marker legend control separately or exclude
            # For simplicity, we keep markers visible under the same name or slightly altered
            
            max_val = max(max_val, prop.a * (1.0 + prop.e))

        fig = go.Figure(data=traces)
        
        plot_title = title or self.locale.t("ui.title_multi_orbit")
        self.configure_layout(fig, plot_title, max_val)

        return fig


# ======================================================================
# Standalone functions for backward compatibility (delegating to OrbitPlotter)
# ======================================================================

def create_earth_sphere(R: float = EARTH_RADIUS, num_puntos: int = 50) -> go.Surface:
    """Creates an Earth sphere trace."""
    plotter = OrbitPlotter()
    return plotter.create_earth_sphere(radius=R, num_points=num_puntos)


def plot_orbit_3d(
    propagator: OrbitalPropagator,
    titulo: Optional[str] = None,
    mostrar_tierra: bool = True,
    color: str = "red",
    num_puntos: int = 500,
) -> go.Figure:
    """Plots a single orbit in 3D."""
    plotter = OrbitPlotter()
    # Handle Spanish parameters mapping to English signature
    return plotter.plot_orbit(
        propagator=propagator,
        title=titulo,
        show_earth=mostrar_tierra,
        color=color,
        num_points=num_puntos,
    )


def plot_multiple_orbits(
    propagators: Sequence[OrbitalPropagator],
    nombres: Optional[List[str]] = None,
    colores: Optional[List[str]] = None,
    titulo: Optional[str] = None,
    mostrar_tierra: bool = True,
    num_puntos: int = 500,
) -> go.Figure:
    """Plots multiple orbits in 3D."""
    plotter = OrbitPlotter()
    return plotter.plot_comparison(
        propagators=propagators,
        names=nombres,
        colors=colores,
        title=titulo,
        show_earth=mostrar_tierra,
        num_points=num_puntos,
    )


# ======================================================================
# Backward-Compatible Spanish Aliases
# ======================================================================
crear_esfera_tierra = create_earth_sphere
graficar_orbita_3d = plot_orbit_3d
graficar_multiples_orbitas = plot_multiple_orbits
