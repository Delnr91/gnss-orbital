# GNSS Orbital Mechanics and Precision

GNSS (Global Navigation Satellite Systems) constellations rely on high-precision orbital slots to guarantee worldwide positioning coverage and carrier-phase accuracy.

---

## 1. Constellation Geometry

GNSS constellations operate in MEO (Medium Earth Orbit) slots to maximize coverage area while minimizing atmospheric drag.

| Parameter | GPS (USA) | Galileo (EU) | GLONASS (RU) | BeiDou-3 (CN) |
|-----------|-----------|--------------|--------------|---------------|
| **Semi-major Axis ($a$)** | 26,560 km | 29,600 km | 25,510 km | 27,910 km (MEO) |
| **Eccentricity ($e$)** | < 0.01 | < 0.002 | < 0.01 | < 0.005 |
| **Inclination ($i$)** | $55^\circ$ | $56^\circ$ | $64.8^\circ$ | $55^\circ$ |
| **Orbital Planes** | 6 (A to F) | 3 (A, B, C) | 3 | 3 |
| **Satellites** | 31 (nominal) | 24 (nominal) | 24 (nominal) | 24 MEO |

---

## 2. Carrier-Phase Precision and Synchronization

GNSS positioning accuracy is determined by the ranging equations:

$$P_i^s = \rho_i^s + c \cdot (dt_i - dt^s) + T_i^s + I_i^s + \epsilon$$

where:
- $\rho_i^s$ is the geometric range: $\rho = \sqrt{(x^s - x_i)^2 + (y^s - y_i)^2 + (z^s - z_i)^2}$.
- $dt_i$ is the receiver clock error.
- $dt^s$ is the satellite clock error (modeled using polynomial coefficients sent in the navigation message).
- $T_i^s, I_i^s$ are tropospheric and ionospheric propagation delays.

### RTK (Real-Time Kinematic) and PPP (Precise Point Positioning)
- **RTK**: Employs double-differencing between a base station and a rover, canceling common tropospheric, ionospheric, and orbital errors. Achieves centimeter-level accuracy.
- **PPP**: Relies on single-station measurements combined with precise satellite clock and orbit products (e.g., from IGS - International GNSS Service) to achieve decimeter or centimeter-level accuracy globally.

---

## 3. Relativistic Corrections

GNSS satellites experience two distinct relativistic effects:
1. **Special Relativity (Time Dilation)**: The satellite's velocity causes its clock to tick slower relative to a receiver on Earth.
2. **General Relativity (Gravitational Redshift)**: Being higher in Earth's gravitational potential field, the satellite clock ticks faster relative to Earth.

The net clock rate shift is offset before launch by tuning the clock frequency from $10.23$ MHz to $10.22999999543$ MHz.

Additionally, the orbital eccentricity introduces a periodic relativistic correction:

$$\Delta t_{rel} = \frac{2 \vec{r} \cdot \vec{v}}{c^2} = \frac{2 \sqrt{\mu a}}{c^2} e \sin E$$

This is calculated by the receiver dynamically using the eccentric anomaly $E$ solved from [[docs/orbital_theory.md]].
