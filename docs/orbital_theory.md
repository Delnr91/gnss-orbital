# Theory of Keplerian Orbital Dynamics

Reference document for Keplerian two-body mechanics and orbital propagation.

---

## Table of Contents

1. [The Two-Body Problem](#1-the-two-body-problem)
2. [Kepler's Laws](#2-keplers-laws)
3. [Classical Orbital Elements](#3-classical-orbital-elements)
4. [Kepler's Equation](#4-keplers-equation)
5. [Orbit Types by Eccentricity](#5-orbit-types-by-eccentricity)
6. [Classification of Earth Orbits](#6-classification-of-earth-orbits)
7. [The Vis-Viva Equation](#7-the-vis-viva-equation)
8. [Summary of Fundamental Equations](#8-summary-of-fundamental-equations)

---

## 1. The Two-Body Problem

### 1.1 Problem Formulation

The two-body problem describes the motion of two point masses ($m_1$ and $m_2$) interacting solely through their mutual gravitational attraction. It forms the basis of classical astrodynamics.

Key assumptions:
- The bodies are modeled as spherical point masses of uniform density.
- No external perturbations act on the system.
- Relativistic effects are neglected.
- The central body (Earth, $m_1$) is much more massive than the orbiting body (satellite, $m_2$): $m_1 \gg m_2$.

### 1.2 Mathematical Formulation

#### Newton's Law of Universal Gravitation

The gravitational force between the two bodies is:

$$\vec{F} = -\frac{G \, m_1 \, m_2}{r^2} \hat{r}$$

where $G$ is the universal gravitational constant, $r$ is the distance between their centers of mass, and $\hat{r}$ is the radial unit vector.

#### Equation of Motion

Applying Newton's second law in an Earth-centered inertial (ECI) frame:

$$\ddot{\vec{r}} = -\frac{\mu}{r^3} \vec{r}$$

where $\mu = G \, M_{\text{Earth}} = 398600.4418 \; \text{km}^3/\text{s}^2$ is the standard gravitational parameter of Earth.

---

## 2. Kepler's Laws

Johannes Kepler formulated three laws of planetary motion, which are direct consequences of Newton's laws of motion and gravitation.

### 2.1 First Law - Law of Orbits

> "The orbit of a planet is an ellipse with the Sun at one of the two foci."

In polar coordinates (origin at the Earth's center of mass), the radial distance $r$ is given by:

$$r(\nu) = \frac{a(1 - e^2)}{1 + e \cos\nu}$$

where $a$ is the semi-major axis, $e$ is the eccentricity, and $\nu$ is the true anomaly.

```
                    Apoapsis (furthest point)
                          r_a = a(1+e)
                             .
                         .       .
                      .             .
                    .                 .
      Semi-minor   .                   .
      axis (b)     .        Center      .
                   .          x          .
                    .    Focus (Earth)  .
                      .      |       .
                         .   |   .
                             .
                    Periapsis (closest point)
                          r_p = a(1-e)

                    |<------ a ------->|
                    |<-- Semi-major axis ->|
```

### 2.2 Second Law - Law of Areas

> "A line segment joining a planet and the Sun sweeps out equal areas during equal intervals of time."

$$\frac{dA}{dt} = \frac{h}{2} = \text{constant}$$

where $h = |\vec{r} \times \dot{\vec{r}}|$ is the specific angular momentum. Consequently, a satellite moves faster near periapsis than apoapsis.

### 2.3 Third Law - Law of Periods

> "The square of the orbital period of a planet is directly proportional to the cube of the semi-major axis of its orbit."

$$T = 2\pi \sqrt{\frac{a^3}{\mu}}$$

---

## 3. Classical Orbital Elements

The state of a satellite can be defined by six Keplerian elements:

1. **Semi-major Axis ($a$)**: Defines orbit size and total energy.
2. **Eccentricity ($e$)**: Defines orbit shape (0 for circular, $0 < e < 1$ for elliptic).
3. **Inclination ($i$)**: Defines the tilt of the orbit plane relative to the equatorial reference plane ($0^\circ \le i \le 180^\circ$).
4. **Right Ascension of the Ascending Node ($\Omega$, RAAN)**: Defines the orientation of the orbital plane in ECI coordinates.
5. **Argument of Periapsis ($\omega$)**: Defines the orientation of the ellipse within the orbital plane.
6. **True Anomaly ($\nu$)**: Defines the satellite's position along the orbit, measured from periapsis.

---

## 4. Kepler's Equation

To determine position as a function of time, we relate the mean anomaly $M$ (which varies linearly with time) to the eccentric anomaly $E$:

$$M = E - e \sin E$$

where $M = n(t - t_0)$ and $n = \sqrt{\mu/a^3}$ is the mean motion.

### 4.1 Numerical Solution: Newton-Raphson Method

Because Kepler's equation is transcendental, it is solved numerically:

$$E_{k+1} = E_k - \frac{E_k - e \sin E_k - M}{1 - e \cos E_k}$$

The method typically converges in 3–5 iterations for standard eccentricities.

---

## 5. Orbit Types by Eccentricity

| Orbit Type | Eccentricity | Energy ($\varepsilon$) | Semi-major Axis ($a$) | Trajectory |
|------------|--------------|------------------------|-----------------------|------------|
| Circular   | $e = 0$      | $< 0$                  | $> 0$                 | Closed     |
| Elliptical | $0 < e < 1$  | $< 0$                  | $> 0$                 | Closed     |
| Parabolic  | $e = 1$      | $= 0$                  | $\to \infty$          | Open       |
| Hyperbolic | $e > 1$      | $> 0$                  | $< 0$                 | Open       |

---

## 6. Classification of Earth Orbits

- **LEO (Low Earth Orbit)**: Altitude 200 – 2,000 km. Orbital period ~90 min. High atmospheric drag. (e.g., ISS).
- **MEO (Medium Earth Orbit)**: Altitude 2,000 – 35,786 km. (e.g., GNSS constellations like GPS, Galileo).
- **GEO (Geostationary Earth Orbit)**: Altitude 35,786 km. Orbital period matches Earth sidereal day (~23 h 56 min). Satellites appear stationary over the equator.
- **HEO (Highly Elliptical Orbit)**: High-apogee, low-perigee orbits (e.g., Molniya orbits). Used for communication at high latitudes.

---

## 7. The Vis-Viva Equation

Derived from the conservation of mechanical energy, the vis-viva equation relates orbital velocity $v$ to radial distance $r$:

$$v = \sqrt{\mu \left(\frac{2}{r} - \frac{1}{a}\right)}$$

---

## 8. Summary of Fundamental Equations

| Parameter | Formula |
|-----------|---------|
| Orbit Equation | $r = \frac{a(1-e^2)}{1+e\cos\nu}$ |
| Period | $T = 2\pi\sqrt{a^3/\mu}$ |
| Circular Velocity | $v_c = \sqrt{\mu/a}$ |
| Escape Velocity | $v_{esc} = \sqrt{2\mu/r}$ |
| Mechanical Energy | $\varepsilon = -\mu/(2a)$ |
