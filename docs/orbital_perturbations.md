# Non-Keplerian Orbital Perturbations

In real-world astrodynamics, satellites do not follow perfect Keplerian ellipses. Non-gravitational and non-spherical forces perturb the orbital elements over time.

---

## 1. Earth's Oblateness ($J_2$ Perturbation)

Earth is not a perfect sphere; polar flattening creates a mass bulge at the equator. This non-spherical potential is modeled using spherical harmonics, dominated by the zonal harmonic coefficient $J_2 = 1.08263 \times 10^{-3}$.

The $J_2$ potential introduces secular (linear) drift rates in three orbital elements:
1. **Regression of the Ascending Node ($\dot{\Omega}$)**: The plane of the orbit rotates around the Earth's spin axis.
2. **Precession of Perigee ($\dot{\omega}$)**: The major axis of the ellipse rotates within the orbital plane.
3. **Mean Anomaly Rate Correction ($\dot{M_0}$)**: Corrects the mean motion.

### Mathematical Formulations

$$\dot{\Omega} = -\frac{3 n J_2 R_{\text{Earth}}^2}{2 a^2 (1 - e^2)^2} \cos i$$

$$\dot{\omega} = \frac{3 n J_2 R_{\text{Earth}}^2}{4 a^2 (1 - e^2)^2} (5 \cos^2 i - 1)$$

### Critical Inclinations
Notice that $\dot{\omega} = 0$ when $5 \cos^2 i - 1 = 0$, which yields the **critical inclinations**:
- $i \approx 63.43^\circ$
- $i \approx 116.57^\circ$

At these inclinations, the perigee does not precess. This property is used by HEO Molniya constellations to keep their apogee fixed over high-latitude ground targets without requiring station-keeping fuel.

---

## 2. Atmospheric Drag

In LEO orbits (altitudes below 1,000 km), residual atmospheric particles decelerate the satellite, causing orbital decay.

The drag acceleration is modeled as:

$$\vec{a}_{\text{drag}} = -\frac{1}{2} \rho \frac{C_D A}{m} v_{\text{rel}} \vec{v}_{\text{rel}}$$

where:
- $\rho$ is the local atmospheric density (varies exponentially with altitude and solar activity).
- $C_D$ is the drag coefficient (typically 2.0 to 2.2).
- $A/m$ is the area-to-mass ratio.
- $\vec{v}_{\text{rel}}$ is the velocity vector relative to the rotating atmosphere.

### Effect on Elements
Atmospheric drag decreases energy, causing the semi-major axis ($a$) and eccentricity ($e$) to decay. The orbit circularizes and descends until the satellite re-enters the dense atmosphere.

---

## 3. Solar Radiation Pressure (SRP)

Solar photons transfer momentum when colliding with satellite surfaces, creating a small but continuous force.

$$\vec{a}_{\text{srp}} = -p_{\text{SR}} \frac{A}{m} (1 + q) \hat{u}_{\text{sun}}$$

where:
- $p_{\text{SR}} \approx 4.57 \times 10^{-6} \; \text{N/m}^2$ is the solar radiation pressure at 1 AU.
- $q$ is the reflectivity coefficient (0 for absorption, 1 for specular reflection).
- $\hat{u}_{\text{sun}}$ is the unit vector pointing from the satellite to the Sun.

SRP is critical for MEO navigation satellites (GPS/Galileo), where it is the largest non-gravitational force and must be modeled to maintain orbit determination accuracy.
