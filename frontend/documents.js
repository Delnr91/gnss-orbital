// Expanded Localized Astrodynamics Knowledge Base (Second Brain Vault)
// Fully translated in English, Spanish, and Chinese

const vaultDocuments = {
    en: {
        "gnss_orbital_mechanics.md": String.raw`# GNSS Orbital Mechanics and Precision

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

This is calculated by the receiver dynamically using the eccentric anomaly $E$ solved from Keplerian dynamics.`,

        "space_infrastructure_2030.md": String.raw`# Space Infrastructure and Constellations Roadmap to 2030

The landscape of space infrastructure by 2030 is defined by hybrid, multi-orbital constellations integrating communication (LEO) and navigation (MEO) systems.

---

## 1. The EU IRIS² Constellation (2027–2030)

IRIS² (Infrastructure for Resilience, Interconnection and Security by Satellite) is Europe's secure communication constellation.

- **System Architecture**: Multi-orbital hybrid configuration.
  - LEO Component: High-throughput, low-latency broadband nodes (governmental and commercial).
  - MEO Component: Medium Earth Orbit nodes providing wide-area coverage and links to navigation systems.
- **Quantum Encryption**: Integrates Quantum Key Distribution (QKD) payloads to secure communications against future cryptographic threats.
- **Synergy with Galileo**: Provides cross-link synchronization and satellite-based augmentation systems (SBAS).

---

## 2. Next-Generation Navigation Systems (2030 Roadmap)

### GPS III and IIIF
- **M-code**: Military signal designed to resist jamming and spoofing, featuring high-power spot beams.
- **L1C Signal**: Interoperable civil signal compatible with Galileo E1, GLONASS L1OC, and BeiDou B1C.
- **Laser Retroreflector Arrays**: Enables satellite laser ranging (SLR) to calibrate orbits independently of radio signals.

### Galileo Second Generation (G2G)
- **Electric Propulsion**: Speeds up transit from transfer orbit to operational slot, allowing faster constellation replenishment.
- **Inter-Satellite Links (ISL)**: Satellites communicate directly in space. This reduces dependence on ground monitoring stations and improves real-time orbit determination accuracy.
- **Onboard Atomic Clocks**: High-performance rubidium and passive hydrogen maser clocks, offering sub-nanosecond synchronization.

### BeiDou-4 (BDS-4)
- **High-Precision LEO Augmentation**: Incorporates a LEO constellation to broadcast correction messages, reducing receiver convergence times for PPP positioning from minutes to seconds.
- **Integrated Communications**: Enhanced short-message and search-and-rescue services.

---

## 3. Collaborative Space Mechanics

Operating these constellations requires precise orbit design to prevent collisions and optimize coverage:
- **Station Keeping**: Active orbit maintenance to counter Earth's oblateness perturbations.
- **Decommissioning**: Satellites must be moved to graveyard orbits at end-of-life:
  - LEO: De-orbit to burn up in the atmosphere within 5 years.
  - MEO/GEO: Propelled to a graveyard orbit ($a > a_{\text{nominal}} + 300$ km).
- **Hohmann Transfer Orbit**: Fundamental transfer maneuver used to transition satellites from launch trajectories to operational slots.`,

        "orbital_perturbations.md": String.raw`# Non-Keplerian Orbital Perturbations

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

SRP is critical for MEO navigation satellites (GPS/Galileo), where it is the largest non-gravitational force and must be modeled to maintain orbit determination accuracy.`,

        "astronomy_fundamentals.md": String.raw`# Fundamentals of Space Astronomy and Reference Systems

Operating spacecraft and global navigation satellite systems requires high-precision reference frames and time scales to synchronize orbital mechanics and ground observation data.

---

## 1. Celestial Coordinate Reference Frames

Astrodynamics and satellite positioning require distinct coordinate frames to model space mechanics (inertial) and receiver tracking (earth-fixed).

### 1.1 Earth-Centered Inertial (ECI) Frame
- **Definition**: A non-rotating coordinate frame with its origin at Earth's center of mass.
- **Axes**:
  - $X$-axis points toward the Vernal Equinox (direction of the Sun at the beginning of spring).
  - $Z$-axis points along Earth's rotational axis (North Pole).
  - $Y$-axis completes the right-handed Cartesian coordinate system.
- **Standard Epoch**: **J2000.0** (defined by Earth's orientation at 12:00 UTC on January 1, 2000).
- **Application**: Used to solve equations of motion and propagate orbits, as Newton's laws hold true in inertial frames.

### 1.2 Earth-Centered, Earth-Fixed (ECEF) Frame
- **Definition**: A rotating coordinate frame that moves with the Earth.
- **Axes**:
  - $X$-axis points toward the Prime Meridian (Greenwich Meridian, $0^\circ$ longitude).
  - $Z$-axis points along Earth's spin axis.
  - $Y$-axis completes the right-handed coordinate system ($90^\circ$ East longitude).
- **Standard Reference**: **ITRF** (International Terrestrial Reference Frame) or **WGS 84** (World Geodetic System 1984).
- **Application**: Used to locate receivers on Earth's surface and calculate user positioning coordinates.

---

## 2. Space Time Scales

Space systems require uniform time-keeping because standard UTC is perturbed by Earth's variable rotation rate.

### 2.1 International Atomic Time (TAI)
- **Definition**: A highly stable, continuous time scale derived from a worldwide network of atomic clocks.
- **Unit**: The SI second at sea level.
- **Drift**: TAI does not introduce leap seconds.

### 2.2 Coordinated Universal Time (UTC)
- **Definition**: The civil time scale synchronized with Earth's rotation (UT1) using leap seconds.
- **Constraint**: UTC is adjusted via leap seconds so that the difference $|UT1 - UTC| < 0.9$ seconds.
- **Relation to TAI**: Currently, $TAI - UTC = 37$ seconds (as of 2026).

### 2.3 GPS Time (GPST)
- **Definition**: A continuous time scale used by the GPS constellation.
- **Epoch**: January 6, 1980.
- **Offset**: GPST was synchronized with UTC at its epoch. Since it does not introduce leap seconds, it remains offset from TAI by a constant:
  
  $$TAI - GPST = 19 \; \text{seconds}$$
  
  $$GPST - UTC = 18 \; \text{seconds} \; (\text{as of 2026})$$

---

## 3. Relativistic Clock Effects in GNSS

Atomic clocks orbiting in MEO slots experience relativistic velocity and gravity shifts relative to Earth receivers:

1. **Special Relativity (Velocity)**: Satellite speed ($v \approx 3.9$ km/s) slows the clock:
   
   $$\frac{\Delta f}{f} = -\frac{v^2}{2 c^2} \approx -8.3 \times 10^{-11} \; (-7.1 \; \mu\text{s/day})$$

2. **General Relativity (Gravitational Potential)**: Satellite is higher in Earth's gravity potential, speeding up the clock:
   
   $$\frac{\Delta f}{f} = \frac{\Delta \Phi}{c^2} \approx +5.3 \times 10^{-11} \; (+45.7 \; \mu\text{s/day})$$

The combined effect is **$+38.6 \; \mu\text{s/day}$**. To compensate, satellite clocks are tuned down before launch from $10.23$ MHz to $10.22999999543$ MHz.`,

        "orbital_calculations.md": String.raw`# Astrodynamics Orbital Calculations Reference

A technical summary of formulas and numerical steps required to compute velocities, period lengths, and orbital maneuvers in a two-body central gravitational system.

---

## 1. Velocity Analysis Using Vis-Viva

The vis-viva equation relates a satellite's speed ($v$) at any point along its orbit to its distance ($r$) from Earth's center and the semi-major axis ($a$):

$$v = \sqrt{\mu \left( \frac{2}{r} - \frac{1}{a} \right)}$$

### 1.1 Special Case: Circular Orbits
In a circular orbit, $r = a$. The velocity is constant:

$$v_{\text{circular}} = \sqrt{\frac{\mu}{a}}$$

For LEO orbits at $400$ km altitude ($a = 6771$ km): $v \approx 7.67$ km/s.

### 1.2 Velocity at Absides (Apoapsis and Periapsis)
In an elliptical orbit, velocity reaches its maximum at periapsis and its minimum at apoapsis.

1. **Periapsis Velocity ($v_p$)** (where $r_p = a(1 - e)$):
   
   $$v_p = \sqrt{\frac{\mu}{a} \left( \frac{1 + e}{1 - e} \right)}$$

2. **Apoapsis Velocity ($v_a$)** (where $r_a = a(1 + e)$):
   
   $$v_a = \sqrt{\frac{\mu}{a} \left( \frac{1 - e}{1 + e} \right)}$$

---

## 2. Escape Velocity

The minimum speed required for an unpropelled body to escape Earth's gravitational field completely, moving on a parabolic trajectory ($e = 1$, specific energy $\varepsilon = 0$):

$$v_{\text{escape}} = \sqrt{\frac{2\mu}{r}}$$

At Earth's surface ($r = 6371$ km): $v_{\text{escape}} \approx 11.2$ km/s.

---

## 3. The Hohmann Transfer Maneuver

A Hohmann transfer is a two-impulse coplanar maneuver used to transition a satellite between two circular coplanar orbits of different radii ($r_1$ and $r_2$) using an elliptical transfer orbit.

### 3.1 Step 1: Initial State
The satellite orbits at radius $r_1$ with circular speed:

$$v_1 = \sqrt{\frac{\mu}{r_1}}$$

### 3.2 Step 2: First Burn ($\Delta v_1$)
To enter the elliptical transfer orbit, which has a periapsis of $r_1$ and apogee of $r_2$, we compute the transfer semi-major axis ($a_{tx}$):

$$a_{tx} = \frac{r_1 + r_2}{2}$$

The required velocity at periapsis of the transfer orbit is:

$$v_{tx,1} = \sqrt{\mu \left( \frac{2}{r_1} - \frac{1}{a_{tx}} \right)}$$

The first velocity increment is:

$$\Delta v_1 = v_{tx,1} - v_1$$

### 3.3 Step 3: Second Burn ($\Delta v_2$)
Upon arriving at the apogee of the transfer orbit ($r = r_2$), the satellite's speed is:

$$v_{tx,2} = \sqrt{\mu \left( \frac{2}{r_2} - \frac{1}{a_{tx}} \right)}$$

The final circular orbit at radius $r_2$ requires circular speed:

$$v_2 = \sqrt{\frac{\mu}{r_2}}$$

The second velocity increment is:

$$\Delta v_2 = v_2 - v_{tx,2}$$

### 3.4 Total Delta-V Budget
The total delta-v required for the Hohmann transfer is:

$$\Delta v_{\text{total}} = |\Delta v_1| + |\Delta v_2|$$`,

        "gnss_positioning_precision.md": String.raw`# GNSS Positioning Precision and Signal Frequencies

A technical guide on signal structures, coordinate calculation errors, and Dilution of Precision (DOP) math in satellite positioning systems.

---

## 1. GNSS Frequency Bands

Modern navigation systems transmit signals across multiple radio frequencies to allow receivers to calculate ionospheric delay and maintain signal locking in challenging environments.

### 1.1 GPS (USA)
- **L1 Band**: $1575.42$ MHz. Broadcasts the civil Coarse/Acquisition (C/A) code and the military P(Y) code.
- **L2 Band**: $1227.60$ MHz. Used to measure ionospheric delays by comparing with L1. Broadcasts L2C and military codes.
- **L5 Band**: $1176.45$ MHz. Safe-of-life civil frequency, featuring higher power and wider bandwidth to resist interference.

### 1.2 Galileo (EU)
- **E1 Band**: $1575.42$ MHz. Co-aligned with GPS L1, enabling inter-system civil navigation compatibility.
- **E5a / E5b Bands**: $1176.45$ MHz (E5a, co-aligned with L5) and $1207.14$ MHz (E5b). Used for high-precision civil services and clock synchronization.
- **E6 Band**: $1278.75$ MHz. Used for the Commercial Service (CS) offering High Accuracy Service (HAS) with PPP corrections.

---

## 2. Pseudorange Error Budget

The measured range between a satellite and a receiver contains errors that must be modeled or double-differenced out:

$$\text{Pseudorange Error} = d_{\text{orbit}} + d_{\text{clock}} + d_{\text{ion}} + d_{\text{trop}} + d_{\text{multipath}} + \eta$$

### 2.1 Ionospheric Delay ($d_{\text{ion}}$)
- The ionosphere ($50$ to $1000$ km altitude) contains free electrons that refract radio waves.
- **Correction**: Can be calculated using a dual-frequency receiver (e.g., L1 and L2 comparison) since refractivity is frequency-dependent ($d_{\text{ion}} \propto 1/f^2$).

### 2.2 Tropospheric Delay ($d_{\text{trop}}$)
- The neutral atmosphere ($0$ to $50$ km altitude) delays signals due to dry gases and water vapor.
- **Correction**: Modeled using empirical formulas based on pressure, temperature, and receiver elevation angle (e.g., Saastamoinen or Hopfield models).

---

## 3. Dilution of Precision (DOP)

DOP is a multiplier that maps satellite geometry errors into user coordinate errors. It is derived from the geometry matrix $A$ containing unit vectors pointing from the receiver to each visible satellite.

### 3.1 Mathematical Derivation
Let the geometry matrix $A$ be defined as:

$$A = \begin{bmatrix}
x_1 & y_1 & z_1 & 1 \\
x_2 & y_2 & z_2 & 1 \\
\vdots & \vdots & \vdots & \vdots \\
x_n & y_n & z_n & 1
\end{bmatrix}$$

The covariance matrix $Q$ of the receiver position and clock offset is:

$$Q = (A^T A)^{-1} = \begin{bmatrix}
q_{xx} & q_{xy} & q_{xz} & q_{xt} \\
q_{yx} & q_{yy} & q_{yz} & q_{yt} \\
q_{zx} & q_{zy} & q_{zz} & q_{zt} \\
q_{tx} & q_{ty} & q_{tz} & q_{tt}
\end{bmatrix}$$

### 3.2 DOP Parameters
- **GDOP (Geometric DOP)**: Overal precision containing 3D coordinates and clock offset.
  
  $$\text{GDOP} = \sqrt{q_{xx} + q_{yy} + q_{zz} + q_{tt}}$$

- **PDOP (Position DOP)**: 3D coordinates precision.
  
  $$\text{PDOP} = \sqrt{q_{xx} + q_{yy} + q_{zz}}$$

- **HDOP (Horizontal DOP)**: 2D horizontal precision (Latitude, Longitude).
  
  $$\text{HDOP} = \sqrt{q_{xx} + q_{yy}}$$

- **VDOP (Vertical DOP)**: 1D altitude precision (typically higher than HDOP due to satellites only being visible above the horizon).
  
  $$\text{VDOP} = \sqrt{q_{zz}}$$`
    },
    es: {
        "gnss_orbital_mechanics.md": String.raw`# Mecánica Orbital y Precisión de GNSS

Las constelaciones GNSS (Sistemas Globales de Navegación por Satélite) dependen de ranuras orbitales de alta precisión para garantizar la cobertura de posicionamiento mundial y la exactitud de la fase portadora.

---

## 1. Geometría de las Constelaciones

Las constelaciones GNSS operan en órbitas terrestres medias (MEO) para maximizar el área de cobertura mientras se minimiza el arrastre atmosférico.

| Parámetro | GPS (EE. UU.) | Galileo (UE) | GLONASS (RU) | BeiDou-3 (CN) |
|-----------|-----------|--------------|--------------|---------------|
| **Semieje Mayor ($a$)** | 26,560 km | 29,600 km | 25,510 km | 27,910 km (MEO) |
| **Excentricidad ($e$)** | < 0.01 | < 0.002 | < 0.01 | < 0.005 |
| **Inclinación ($i$)** | $55^\circ$ | $56^\circ$ | $64.8^\circ$ | $55^\circ$ |
| **Planos Orbitales** | 6 (A al F) | 3 (A, B, C) | 3 | 3 |
| **Satélites** | 31 (nominal) | 24 (nominal) | 24 (nominal) | 24 MEO |

---

## 2. Precisión de Fase Portadora y Sincronización

La precisión del posicionamiento GNSS está determinada por las ecuaciones de rango:

$$P_i^s = \rho_i^s + c \cdot (dt_i - dt^s) + T_i^s + I_i^s + \epsilon$$

donde:
- $\rho_i^s$ es el rango geométrico: $\rho = \sqrt{(x^s - x_i)^2 + (y^s - y_i)^2 + (z^s - z_i)^2}$.
- $dt_i$ es el error del reloj del receptor.
- $dt^s$ es el error del reloj del satélite (modelado mediante coeficientes polinomiales enviados en el mensaje de navegación).
- $T_i^s, I_i^s$ son los retrasos de propagación troposférica e ionosférica.

### RTK (Cinemática en Tiempo Real) y PPP (Posicionamiento de Punto Preciso)
- **RTK**: Emplea doble diferenciación entre una estación base y un receptor móvil, cancelando los errores orbitales, ionosféricos y troposféricos comunes. Logra precisión a nivel de centímetros.
- **PPP**: Se basa en mediciones de una sola estación combinadas con productos precisos de órbitas y relojes de satélites (p. ej., del IGS - Servicio Internacional de GNSS) para lograr precisión a nivel de decímetros o centímetros de forma global.

---

## 3. Correcciones Relativistas

Los satélites GNSS experimentan dos efectos relativistas distintos:
1. **Relatividad Especial (Dilatación del Tiempo)**: La velocidad del satélite hace que su reloj funcione más lento en relación con un receptor en la Tierra.
2. **Relatividad General (Desplazamiento al Rojo Gravitacional)**: Al estar más alto en el campo de potencial gravitatorio de la Tierra, el reloj del satélite funciona más rápido en relación con la Tierra.

El cambio neto de la tasa del reloj se compensa antes del lanzamiento ajustando la frecuencia del reloj de $10.23$ MHz a $10.22999999543$ MHz.

Además, la excentricidad orbital introduce una corrección relativista periódica:

$$\Delta t_{rel} = \frac{2 \vec{r} \cdot \vec{v}}{c^2} = \frac{2 \sqrt{\mu a}}{c^2} e \sin E$$

Esto es calculado por el receptor dinámicamente utilizando la anomalía excéntrica $E$ resuelta a partir de la ecuación de Kepler.`,

        "space_infrastructure_2030.md": String.raw`# Hoja de Ruta de la Infraestructura Espacial y Constelaciones al 2030

El panorama de la infraestructura espacial para 2030 está definido por constelaciones híbridas y multiorbitales que integran sistemas de comunicación (LEO) y navegación (MEO).

---

## 1. La Constelación IRIS² de la UE (2027–2030)

IRIS² (Infraestructura para la Resiliencia, Interconexión y Seguridad por Satélite) es la constelación de comunicaciones seguras de Europa.

- **Arquitectura del Sistema**: Configuración híbrida multiorbital.
  - Componente LEO: Nodos de banda ancha de alto rendimiento y baja latencia (gubernamentales y comerciales).
  - Componente MEO: Nodos de órbita terrestre media que proporcionan cobertura de área amplia y enlaces a sistemas de navegación.
- **Cifrado Cuántico**: Integra cargas útiles de Distribución de Claves Cuánticas (QKD) para proteger las comunicaciones contra futuras amenazas criptográficas.
- **Sinergia con Galileo**: Proporciona sincronización de enlaces cruzados y sistemas de aumentación basados en satélites (SBAS).

---

## 2. Sistemas de Navegación de Próxima Generación (Hoja de Ruta al 2030)

### GPS III y IIIF
- **Código M**: Señal militar diseñada para resistir interferencias y suplantaciones de identidad, con haces focalizados de alta potencia.
- **Señal L1C**: Señal civil interoperable compatible con Galileo E1, GLONASS L1OC y BeiDou B1C.
- **Matrices de retrorreflectores láser**: Permite el rango láser por satélite (SLR) para calibrar órbitas independientemente de las señales de radio.

### Galileo Segunda Generación (G2G)
- **Propulsión Eléctrica**: Acelera el tránsito desde la órbita de transferencia hasta la ranura operativa, permitiendo una reposición más rápida de la constelación.
- **Enlaces Inter-Satelitales (ISL)**: Los satélites se comunican directamente en el espacio. Esto reduce la dependencia de las estaciones terrestres y mejora la precisión de determinación orbital en tiempo real.
- **Relojes Atómicos a Bordo**: Relojes de rubidio y máseres de hidrógeno pasivos de alto rendimiento, que ofrecen sincronización de sub-nanosegundos.

### BeiDou-4 (BDS-4)
- **Aumentación LEO de Alta Precisión**: Incorpora una constelación LEO para transmitir mensajes de corrección, reduciendo los tiempos de convergencia del receptor para el posicionamiento PPP de minutos a segundos.
- **Comunicaciones Integradas**: Servicios mejorados de mensajes cortos y búsqueda y rescate.

---

## 3. Mecánica Espacial Colaborativa

La operación de estas constelaciones requiere un diseño orbital preciso para evitar colisiones y optimizar la cobertura:
- **Mantenimiento de Estación (Station Keeping)**: Mantenimiento activo de la órbita para contrarrestar la deformación de la Tierra.
- **Retiro de Servicio (Decommissioning)**: Los satélites deben trasladarse a órbitas cementerio al final de su vida útil:
  - LEO: Desorbitar para quemarse en la atmósfera en un plazo de 5 años.
  - MEO/GEO: Propulsados a una órbita cementerio ($a > a_{\text{nominal}} + 300$ km).
- **Órbita de Transferencia de Hohmann**: Maniobra de transferencia fundamental utilizada para la transición de satélites desde trayectorias de lanzamiento a sus ranuras operativas.`,

        "orbital_perturbations.md": String.raw`# Perturbaciones Orbitales No Keplerianas

En la astrodinámica del mundo real, los satélites no siguen elipses keplerianas perfectas. Las fuerzas no gravitacionales y no esféricas perturban los elementos orbitales a lo largo del tiempo.

---

## 1. Achatamiento de la Tierra (Perturbación $J_2$)

La Tierra no es una esfera perfecta; el achatamiento polar crea un ensanchamiento de masa en el ecuador. Este potencial no esférico se modela mediante armónicos esféricos, dominados por el coeficiente armónico zonal $J_2 = 1.08263 \times 10^{-3}$.

El potencial $J_2$ introduce tasas de deriva seculares (lineales) en tres elementos orbitales:
1. **Regresión del Nodo Ascendente ($\dot{\Omega}$)**: El plano de la órbita gira alrededor del eje de rotación de la Tierra.
2. **Precesión del Perigeo ($\dot{\omega}$)**: El eje mayor de la elipse gira dentro del plano orbital.
3. **Corrección de la Tasa de Anomalía Media ($\dot{M_0}$)**: Correige el movimiento medio.

### Formulaciones Matemáticas

$$\dot{\Omega} = -\frac{3 n J_2 R_{\text{Tierra}}^2}{2 a^2 (1 - e^2)^2} \cos i$$

$$\dot{\omega} = \frac{3 n J_2 R_{\text{Tierra}}^2}{4 a^2 (1 - e^2)^2} (5 \cos^2 i - 1)$$

### Inclinaciones Críticas
Nótese que $\dot{\omega} = 0$ cuando $5 \cos^2 i - 1 = 0$, lo que produce las **inclinaciones críticas**:
- $i \approx 63.43^\circ$
- $i \approx 116.57^\circ$

A estas inclinaciones, el perigeo no precesa. Esta propiedad es utilizada por las constelaciones HEO Molniya para mantener su apogeo fijo sobre objetivos terrestres de alta latitud sin necesidad de combustible de mantenimiento de estación.

---

## 2. Arrastre Atmosférico

En órbitas LEO (altitudes inferiores a 1,000 km), las partículas atmosféricas residuales desaceleran el satélite, provocando el decaimiento orbital.

La aceleración del arrastre se modela como:

$$\vec{a}_{\text{drag}} = -\frac{1}{2} \rho \frac{C_D A}{m} v_{\text{rel}} \vec{v}_{\text{rel}}$$

donde:
- $\rho$ es la densidad atmosférica local (varía exponencialmente con la altitud y la actividad solar).
- $C_D$ es el coeficiente de arrastre (generalmente de 2.0 a 2.2).
- $A/m$ es la relación área-masa.
- $\vec{v}_{\text{rel}}$ es el vector de velocidad relativo a la atmósfera en rotación.

### Efecto sobre los Elementos
El arrastre atmosférico disminuye la energía de la órbita, lo que provoca que el semieje mayor ($a$) y la excentricidad ($e$) disminuyan. La órbita se circulariza y desciende hasta que el satélite reingresa en la atmósfera densa.

---

## 3. Presión de Radiación Solar (SRP)

Los fotones solares transfieren momento al chocar con las superficies del satélite, creando una fuerza pequeña pero continua.

$$\vec{a}_{\text{srp}} = -p_{\text{SR}} \frac{A}{m} (1 + q) \hat{u}_{\text{sun}}$$

donde:
- $p_{\text{SR}} \approx 4.57 \times 10^{-6} \; \text{N/m}^2$ es la presión de radiación solar a 1 UA.
- $q$ es el coeficiente de reflectividad (0 para absorción, 1 para reflexión especular).
- $\hat{u}_{\text{sun}}$ es el vector unitario que apunta del satélite al Sol.

La SRP es crítica para los satélites de navegación MEO (GPS/Galileo), donde es la fuerza no gravitatoria más grande y debe modelarse para mantener la precisión en la determinación de la órbita.`,

        "astronomy_fundamentals.md": String.raw`# Fundamentos de Astronomía Espacial y Sistemas de Referencia

La operación de naves espaciales y sistemas globales de navegación por satélite requiere marcos de referencia y escalas de tiempo de alta precisión para sincronizar la mecánica orbital y los datos de observación terrestres.

---

## 1. Marcos de Referencia Coordenados Celestiales

La astrodinámica y el posicionamiento por satélite requieren marcos de coordenadas distintos para modelar la mecánica espacial (inercial) y el seguimiento del receptor (fijo a la Tierra).

### 1.1 Marco Inercial Centrado en la Tierra (ECI)
- **Definición**: Un marco de coordenadas no giratorio con su origen en el centro de masa de la Tierra.
- **Ejes**:
  - El eje $X$ apunta hacia el Equinoccio Vernal (la dirección del Sol al inicio de la primavera).
  - El eje $Z$ apunta a lo largo del eje de rotación de la Tierra (Polo Norte).
  - El eje $Y$ completa el sistema de coordenadas cartesianas diestras.
- **Época Estándar**: **J2000.0** (definida por la orientación de la Tierra a las 12:00 UTC del 1 de enero de 2000).
- **Aplicación**: Se utiliza para resolver las ecuaciones de movimiento y propagar órbitas, ya que las leyes de Newton se cumplen en marcos inerciales.

### 1.2 Marco Fijo a la Tierra, Centrado en la Tierra (ECEF)
- **Definición**: Un marco de coordenadas giratorio que se mueve con la Tierra.
- **Ejes**:
  - El eje $X$ apunta hacia el Meridiano de Greenwich (longitud $0^\circ$).
  - El eje $Z$ apunta a lo largo del eje de rotación de la Tierra.
  - El eje $Y$ completa el sistema de coordenadas diestras (longitud $90^\circ$ Este).
- **Referencia Estándar**: **ITRF** (Marco de Referencia Terrestre Internacional) o **WGS 84** (Sistema Geodésico Mundial 1984).
- **Aplicación**: Se utiliza para localizar receptores en la superficie de la Tierra y calcular las coordenadas de posicionamiento del usuario.

---

## 2. Escalas de Tiempo Espaciales

Los sistemas espaciales requieren un cronometraje uniforme porque el UTC estándar se ve perturbado por la velocidad de rotación variable de la Tierra.

### 2.1 Tiempo Atómico Internacional (TAI)
- **Definición**: Una escala de tiempo altamente estable y continua derivada de una red mundial de relojes atómicos.
- **Unidad**: El segundo SI al nivel del mar.
- **Desviación**: El TAI no introduce segundos intercalares.

### 2.2 Tiempo Universal Coordinado (UTC)
- **Definición**: La escala de tiempo civil sincronizada con la rotación de la Tierra (UT1) utilizando segundos intercalares.
- **Restricción**: El UTC se ajusta mediante segundos intercalares para que la diferencia $|UT1 - UTC| < 0.9$ segundos.
- **Relación con el TAI**: Actualmente, $TAI - UTC = 37$ segundos (a partir de 2026).

### 2.3 Tiempo GPS (GPST)
- **Definición**: Una escala de tiempo continua utilizada por la constelación GPS.
- **Época**: 6 de enero de 1980.
- **Desfase**: El GPST se sincronizó con el UTC en su época de inicio. Dado que no introduce segundos intercalares, permanece desfasado del TAI por una constante:
  
  $$TAI - GPST = 19 \; \text{segundos}$$
  
  $$GPST - UTC = 18 \; \text{segundos} \; (\text{a partir de 2026})$$

---

## 3. Efectos Relativistas en los Relojes de GNSS

Los relojes atómicos que orbitan en ranuras MEO experimentan cambios de velocidad y gravedad relativistas en comparación con los receptores terrestres:

1. **Relatividad Especial (Velocidad)**: La velocidad del satélite ($v \approx 3.9$ km/s) ralentiza su reloj:
   
   $$\frac{\Delta f}{f} = -\frac{v^2}{2 c^2} \approx -8.3 \times 10^{-11} \; (-7.1 \; \mu\text{s/día})$$

2. **Relatividad General (Potencial Gravitatorio)**: El satélite se encuentra a mayor altura en el potencial gravitatorio de la Tierra, lo que acelera su reloj:
   
   $$\frac{\Delta f}{f} = \frac{\Delta \Phi}{c^2} \approx +5.3 \times 10^{-11} \; (+45.7 \; \mu\text{s/día})$$

El efecto neto combinado es de **$+38.6 \; \mu\text{s/día}$**. Para compensarlo, los relojes de los satélites se ajustan antes del lanzamiento de $10.23$ MHz a $10.22999999543$ MHz.`,

        "orbital_calculations.md": String.raw`# Referencia de Cálculos Orbitales de Astrodinámica

Un resumen técnico de las fórmulas y pasos numéricos requeridos para calcular velocidades, periodos orbitales y maniobras orbitales en un sistema gravitacional de dos cuerpos.

---

## 1. Análisis de Velocidad Mediante Vis-Viva

La ecuación vis-viva relaciona la velocidad ($v$) de un satélite en cualquier punto de su órbita con su distancia ($r$) al centro de la Tierra y el semieje mayor ($a$):

$$v = \sqrt{\mu \left( \frac{2}{r} - \frac{1}{a} \right)}$$

### 1.1 Caso Especial: Órbitas Circulares
En una órbita circular, $r = a$. La velocidad es constante:

$$v_{\text{circular}} = \sqrt{\frac{\mu}{a}}$$

Para órbitas LEO a una altitud de $400$ km ($a = 6771$ km): $v \approx 7.67$ km/s.

### 1.2 Velocidad en los Ábsides (Perigeo y Apogeo)
En una órbita elíptica, la velocidad alcanza su valor máximo en el perigeo y su mínimo en el apogeo.

1. **Velocidad en el Perigeo ($v_p$)** (donde $r_p = a(1 - e)$):
   
   $$v_p = \sqrt{\frac{\mu}{a} \left( \frac{1 + e}{1 - e} \right)}$$

2. **Velocidad en el Apogeo ($v_a$)** (donde $r_a = a(1 + e)$):
   
   $$v_a = \sqrt{\frac{\mu}{a} \left( \frac{1 - e}{1 + e} \right)}$$

---

## 2. Velocidad de Escape

La velocidad mínima requerida para que un cuerpo sin propulsión escape completamente del campo gravitatorio de la Tierra, moviéndose en una trayectoria parabólica ($e = 1$, energía específica $\varepsilon = 0$):

$$v_{\text{escape}} = \sqrt{\frac{2\mu}{r}}$$

En la superficie de la Tierra ($r = 6371$ km): $v_{\text{escape}} \approx 11.2$ km/s.

---

## 3. La Maniobra de Transferencia de Hohmann

Una transferencia de Hohmann es una maniobra coplanar de dos impulsos utilizada para la transición de un satélite entre dos órbitas coplanares circulares de radios diferentes ($r_1$ y $r_2$) utilizando una órbita de transferencia elíptica.

### 3.1 Paso 1: Estado Inicial
El satélite orbita en el radio inicial $r_1$ a velocidad circular:

$$v_1 = \sqrt{\frac{\mu}{r_1}}$$

### 3.2 Paso 2: Primer Encendido ($\Delta v_1$)
Para ingresar a la órbita de transferencia elíptica (que tiene un perigeo de $r_1$ y un apogeo de $r_2$), calculamos el semieje mayor de transferencia ($a_{tx}$):

$$a_{tx} = \frac{r_1 + r_2}{2}$$

La velocidad requerida en el perigeo de la órbita de transferencia es:

$$v_{tx,1} = \sqrt{\mu \left( \frac{2}{r_1} - \frac{1}{a_{tx}} \right)}$$

El primer incremento de velocidad es:

$$\Delta v_1 = v_{tx,1} - v_1$$

### 3.3 Paso 3: Segundo Encendido ($\Delta v_2$)
Al llegar al apogeo de la órbita de transferencia ($r = r_2$), la velocidad del satélite es:

$$v_{tx,2} = \sqrt{\mu \left( \frac{2}{r_2} - \frac{1}{a_{tx}} \right)}$$

La órbita circular final en el radio $r_2$ requiere una velocidad circular:

$$v_2 = \sqrt{\frac{\mu}{r_2}}$$

El segundo incremento de velocidad es:

$$\Delta v_2 = v_2 - v_{tx,2}$$

### 3.4 Presupuesto Total de Delta-V
El delta-v total requerido para la transferencia de Hohmann es:

$$\Delta v_{\text{total}} = |\Delta v_1| + |\Delta v_2|$$`,

        "gnss_positioning_precision.md": String.raw`# Precisión de Posicionamiento GNSS y Frecuencias de Señal

Una guía técnica sobre las estructuras de las señales, los errores de cálculo de coordenadas y la matemática de la Dilución de la Precisión (DOP) en los sistemas de posicionamiento por satélite.

---

## 1. Bandas de Frecuencia de GNSS

Los sistemas de navegación modernos transmiten señales a través de múltiples frecuencias de radio para permitir que los receptores calculen el retraso ionosférico y mantengan el bloqueo de la señal en entornos difíciles.

### 1.1 GPS (EE. UU.)
- **Banda L1**: $1575.42$ MHz. Transmite el código civil de Adquisición/Grueso (C/A) y el código militar P(Y).
- **Banda L2**: $1227.60$ MHz. Se utiliza para medir los retrasos ionosféricos mediante la comparación con L1. Transmite el código L2C y códigos militares.
- **Banda L5**: $1176.45$ MHz. Frecuencia civil para la seguridad de la vida, que cuenta con mayor potencia y un ancho de banda más amplio para resistir interferencias.

### 1.2 Galileo (UE)
- **Banda E1**: $1575.42$ MHz. Co-alineada con GPS L1, lo que permite la compatibilidad de navegación civil entre sistemas.
- **Bandas E5a / E5b**: $1176.45$ MHz (E5a, co-alineada con L5) y $1207.14$ MHz (E5b). Se utiliza para servicios civiles de alta precisión y sincronización de relojes.
- **Banda E6**: $1278.75$ MHz. Utilizada para el Servicio Comercial (CS) que ofrece el Servicio de Alta Precisión (HAS) con correcciones PPP.

---

## 2. Presupuesto de Errores de Pseudodistancia

La distancia medida entre un satélite y un receptor contiene errores que deben modelarse o eliminarse mediante doble diferenciación:

$$\text{Error de Pseudodistancia} = d_{\text{órbita}} + d_{\text{reloj}} + d_{\text{ion}} + d_{\text{trop}} + d_{\text{multipath}} + \eta$$

### 2.1 Retraso Ionosférico ($d_{\text{ion}}$)
- La ionosfera (de $50$ a $1000$ km de altitud) contiene electrones libres que refractan las ondas de radio.
- **Corrección**: Se puede calcular utilizando un receptor de doble frecuencia (p. ej., comparación L1 y L2) ya que la refractividad depende de la frecuencia ($d_{\text{ion}} \propto 1/f^2$).

### 2.2 Retraso Troposférico ($d_{\text{trop}}$)
- La atmósfera neutra (de $0$ a $50$ km de altitud) retrasa las señales debido a los gases secos y al vapor de agua.
- **Corrección**: Se modela mediante fórmulas empíricas basadas en la presión, la temperatura y el ángulo de elevación del receptor (p. ej., los modelos de Saastamoinen o Hopfield).

---

## 3. Dilución de la Precisión (DOP)

DOP es un multiplicador que mapea los errores de geometría del satélite en errores de coordenadas del usuario. Se deriva de la matriz geométrica $A$ que contiene vectores unitarios que apuntan desde el receptor a cada satélite visible.

### 3.1 Derivación Matemática
Definamos la matriz geométrica $A$ como:

$$A = \begin{bmatrix}
x_1 & y_1 & z_1 & 1 \\
x_2 & y_2 & z_2 & 1 \\
\vdots & \vdots & \vdots & \vdots \\
x_n & y_n & z_n & 1
\end{bmatrix}$$

La matriz de covarianza $Q$ de la posición del receptor y el error de reloj es:

$$Q = (A^T A)^{-1} = \begin{bmatrix}
q_{xx} & q_{xy} & q_{xz} & q_{xt} \\
q_{yx} & q_{yy} & q_{yz} & q_{yt} \\
q_{zx} & q_{zy} & q_{zz} & q_{zt} \\
q_{tx} & q_{ty} & q_{tz} & q_{tt}
\end{bmatrix}$$

### 3.2 Parámetros DOP
- **GDOP (DOP Geométrica)**: Precisión general que contiene las coordenadas 3D y el desfase del reloj.
  
  $$\text{GDOP} = \sqrt{q_{xx} + q_{yy} + q_{zz} + q_{tt}}$$

- **PDOP (DOP de Posición)**: Precisión de las coordenadas 3D.
  
  $$\text{PDOP} = \sqrt{q_{xx} + q_{yy} + q_{zz}}$$

- **HDOP (DOP Horizontal)**: Conexión horizontal 2D (Latitud, Longitud).
  
  $$\text{HDOP} = \sqrt{q_{xx} + q_{yy}}$$

- **VDOP (DOP Vertical)**: Precisión de altitud 1D (generalmente mayor que la HDOP debido a que los satélites solo son visibles por encima del horizonte).
  
  $$\text{VDOP} = \sqrt{q_{zz}}$$`
    },
    zh: {
        "gnss_orbital_mechanics.md": String.raw`# GNSS 轨道动力学与精度

GNSS（全球导航卫星系统）星座依赖高精度的轨道槽，以保证全球定位覆盖 and 载波相位精度。

---

## 1. 星座几何结构

GNSS 星座在中地球轨道（MEO）槽中运行，以在最小化大气阻力的同时最大化覆盖面积。

| 参数 | GPS (美国) | Galileo (欧盟) | GLONASS (俄罗斯) | BeiDou-3 (中国) |
|-----------|-----------|--------------|--------------|---------------|
| **半长轴 ($a$)** | 26,560 km | 29,600 km | 25,510 km | 27,910 km (MEO) |
| **偏心率 ($e$)** | < 0.01 | < 0.002 | < 0.01 | < 0.005 |
| **轨道倾角 ($i$)** | $55^\circ$ | $56^\circ$ | $64.8^\circ$ | $55^\circ$ |
| **轨道平面** | 6 (A 到 F) | 3 (A, B, C) | 3 | 3 |
| **卫星数量** | 31 (标称) | 24 (标称) | 24 (标称) | 24 MEO |

---

## 2. 载波相位精度与同步

GNSS 定位精度由伪距测量方程决定：

$$P_i^s = \rho_i^s + c \cdot (dt_i - dt^s) + T_i^s + I_i^s + \epsilon$$

其中：
- $\rho_i^s$ 是几何距离：$\rho = \sqrt{(x^s - x_i)^2 + (y^s - y_i)^2 + (z^s - z_i)^2}$。
- $dt_i$ 是接收机钟差。
- $dt^s$ 是卫星钟差（使用导航电文中发送的多项式系数进行建模）。
- $T_i^s, I_i^s$ 是对流层和电离层传播延迟。

### RTK（实时动态定位）和 PPP（精密单点定位）
- **RTK**：采用基准站和流动站之间的双差技术，消除公共的对流层、电离层和轨道误差。实现厘米级定位精度。
- **PPP**：依赖单站观测值，结合精密的卫星钟差和轨道产品（例如来自 IGS - 国际 GNSS 服务组织）来实现全球分米级或厘米级精度。

---

## 3. 相对论效应修正

GNSS 卫星经历两种不同的相对论效应：
1. **狭义相对论（时间膨胀）**：卫星的速度导致其时钟相对于地球上的接收机变慢。
2. **广义相对论（引力红移）**：由于卫星处于地球引力位较低的地方（即高度更高），卫星时钟相对于地球变快。

在发射前，通过将时钟基准频率从 $10.23$ MHz 调低至 $10.22999999543$ MHz 来补偿这一净时钟漂移。

此外，轨道偏心率还会引入周期性的相对论修正：

$$\Delta t_{rel} = \frac{2 \vec{r} \cdot \vec{v}}{c^2} = \frac{2 \sqrt{\mu a}}{c^2} e \sin E$$

这由接收机利用从轨道动力学解算出的偏心异常 $E$ 进行动态计算。`,

        "space_infrastructure_2030.md": String.raw`# 2030年空间基础设施与星座发展路线图

2030年的空间基础设施格局由集成了通信（LEO）和导航（MEO）系统的混合、多轨道星座所定义。

---

## 1. 欧盟 IRIS² 星座 (2027–2030)

IRIS²（利用卫星实现韧性、互联和安全的基础设施）是欧洲的安全通信星座。

- **系统架构**：多轨道混合配置。
  - LEO 组件：高吞吐量、低延迟宽带节点（政府和商业）。
  - MEO 组件：中地球轨道节点，提供宽区域覆盖以及与导航系统的链路。
- **量子加密**：集成量子密钥分发（QKD）载荷，以保护通信免受未来密码学威胁。
- **与伽利略（Galileo）的协同**：提供跨星链路同步和星基增强系统（SBAS）。

---

## 2. 下一代导航系统（2030年路线图）

### GPS III 和 IIIF
- **M 码**：专门设计的军用信号，具有高功率点面波束，抗干扰和防欺骗。
- **L1C 信号**：与 Galileo E1、GLONASS L1OC 和 BeiDou B1C 兼容的互操作民用信号。
- **激光角反射器阵列**：支持卫星激光测距（SLR），以便独立于无线电信号校准轨道。

### 第二代伽利略 (G2G)
- **电推进**：加快从转移轨道到工作轨道的过渡，允许更快的星座部署和补网。
- **星间链路 (ISL)**：卫星在空间直接通信。这减少了对地面监测站的依赖，并提高了实时轨道确定的精度。
- **车载原子钟**：高性能铷钟和被动氢钟，提供亚纳秒级同步。

### 北斗四号 (BDS-4)
- **高精度 LEO 增强**：结合低轨星座广播改正信息，将接收机 PPP 定位收敛时间从几分钟缩短到几秒钟。
- **集成通信**：增强短报文和搜救服务。

---

## 3. 协同空间力学

运行这些星座需要精确的轨道设计，以防止碰撞并优化覆盖：
- **轨道保持 (Station Keeping)**：主动维护轨道，对抗地球的非球形摄动。
- **退役处置**：卫星在寿命结束时必须移至坟墓轨道：
  - LEO：在5年内退轨并在大气层中烧毁。
  - MEO/GEO：推进至坟墓轨道（$a > a_{\text{nominal}} + 300$ 公里）。
- **霍曼转移轨道**：用于将卫星从发射轨道转移到工作轨道的经典轨道转移机动。`,

        "orbital_perturbations.md": String.raw`# 非开普勒轨道摄动

在现实世界的航天动力学中，卫星并不遵循完美的开普勒椭圆。非引力和非球形力会随着时间的推移扰动轨道要素。

---

## 1. 地球扁率（$J_2$ 摄动）

地球不是一个完美的球体；极地扁平化在赤道上产生了一个质量隆起。这种非球形势能通常使用球谐函数建模，其中带谐系数 $J_2 = 1.08263 \times 10^{-3}$ 起主导作用。

$J_2$ 势能在三个轨道要素中引入了长期（线性）漂移率：
1. **升交点赤经回归 ($\dot{\Omega}$)**：轨道平面围绕地球自转轴旋转。
2. **近地点幅角进动 ($\dot{\omega}$)**：椭圆的长轴在轨道平面内旋转。
3. **平近点角变化率修正 ($\dot{M_0}$)**：修正平均运动。

### 数学公式

$$\dot{\Omega} = -\frac{3 n J_2 R_{\text{Earth}}^2}{2 a^2 (1 - e^2)^2} \cos i$$

$$\dot{\omega} = \frac{3 n J_2 R_{\text{Earth}}^2}{4 a^2 (1 - e^2)^2} (5 \cos^2 i - 1)$$

### 临界倾角
注意，当 $5 \cos^2 i - 1 = 0$ 时 $\dot{\omega} = 0$，这产生了**临界倾角**：
- $i \approx 63.43^\circ$
- $i \approx 116.57^\circ$

在这些倾角下，近地点不会发生进动。这一特性被大椭圆闪电（HEO Molniya）轨道星座所利用，以便将其远地点固定在高纬度地面目标上空，而无需消耗轨道保持燃料。

---

## 2. 大气阻力

在低地球轨道（LEO，高度低于1000公里）中，稀薄的大气粒子会使卫星减速，导致轨道衰减。

阻力加速度模型为：

$$\vec{a}_{\text{drag}} = -\frac{1}{2} \rho \frac{C_D A}{m} v_{\text{rel}} \vec{v}_{\text{rel}}$$

其中：
- $\rho$ 是局部大气密度（随高度和太阳活动呈指数变化）。
- $C_D$ 是阻力系数（通常为 2.0 至 2.2）。
- $A/m$ 是面质比。
- $\vec{v}_{\text{rel}}$ 是相对于旋转大气的速度向量。

### 对轨道要素的影响
大气阻力会减少轨道能量，导致半长轴 ($a$) 和偏心率 ($e$) 衰减。轨道会逐渐圆化并下降，直到卫星重新进入稠密的大气层。

---

## 3. 太阳辐射压力 (SRP)

太阳光子在碰撞卫星表面时传递动量，产生一个微弱但持续的力。

$$\vec{a}_{\text{srp}} = -p_{\text{SR}} \frac{A}{m} (1 + q) \hat{u}_{\text{sun}}$$

其中：
- $p_{\text{SR}} \approx 4.57 \times 10^{-6} \; \text{N/m}^2$ 是 1 天文单位处的太阳辐射压力。
- $q$ 是反射率系数（0 表示完全制造，1 表示镜面反射）。
- $\hat{u}_{\text{sun}}$ 是指向太阳的单位方向向量。

对于中地球轨道导航卫星（GPS/Galileo）来说，太阳辐射压力是最大的非引力，必须对其进行建模以维持轨道确定精度。`,

        "astronomy_fundamentals.md": String.raw`# 空间天文学与参考系基础

运行航天器和全球导航卫星系统（GNSS）需要高精度的参考坐标系和时间尺度，以同步轨道力学方程和地面观测数据。

---

## 1. 天球坐标参考系

航天动力学与卫星定位需要不同的坐标系来对空间力学（惯性系）和接收机跟踪（地球固定系）进行建模。

### 1.1 地心惯性（ECI）坐标系
- **定义**：一个不随地球自转的坐标系，其原点设在地球质心。
- **坐标轴**：
  - $X$ 轴指向春分点（春季开始时太阳的方向）。
  - $Z$ 轴指向地球自转轴（北极方向）。
  - $Y$ 轴完成右手笛卡尔坐标系。
- **标准历元**：**J2000.0**（由地球在 2000 年 1 月 1 日 12:00 UTC 的取向定义）。
- **应用**：用于求解运动方程和进行轨道外推，因为牛顿定律在惯性系中成立。

### 1.2 地心地球固定（ECEF）坐标系
- **定义**：一个随地球自转的旋转坐标系。
- **坐标轴**：
  - $X$ 轴指向本初子午线（格林尼治子午线，经度 $0^\circ$）。
  - $Z$ 轴指向地球自转轴。
  - $Y$ 轴完成右手坐标系（指向东经 $90^\circ$ 处）。
- **标准参考**：**ITRF**（国际陆地参考系）或 **WGS 84**（1984年世界大地测量系统）。
- **应用**：用于确定接收机在地球表面的位置，以及计算用户的定位坐标。

---

## 2. 空间时间尺度

空间系统需要均匀的时间计量，因为标准 UTC 会受到地球自转速度变化的影响。

### 2.1 国际原子时 (TAI)
- **定义**：由全球原子钟网络得出的高度稳定且连续的时间尺度。
- **单位**：海平面处的国际单位制（SI）秒。
- **偏差**：TAI 不引入闰秒。

### 2.2 协调世界时 (UTC)
- **定义**：通过使用闰秒与地球自转（UT1）保持同步的民用时间尺度。
- **约束**：调整 UTC 闰秒，使其与自转时间差值满足 $|UT1 - UTC| < 0.9$ 秒。
- **与 TAI 的关系**：目前，$TAI - UTC = 37$ 秒（自2026年起）。

### 2.3 GPS 时间 (GPST)
- **定义**：GPS 星座所使用的连续时间尺度。
- **起点历元**：1980年1月6日。
- **偏差**：GPST 在其起点时与 UTC 同步。由于它不引入闰秒，所以它与 TAI 始终保持常量差值：
  
  $$TAI - GPST = 19 \; \text{秒}$$
  
  $$GPST - UTC = 18 \; \text{秒} \; (\text{截至2026年})$$

---

## 3. GNSS 中的相对论时钟效应

在中地球轨道（MEO）运行的原子钟相对于地球接收机，会受到相对论速度和重力位移的影响：

1. **狭义相对论（速度效应）**：卫星运行速度（$v \approx 3.9$ km/s）会导致时钟变慢：
   
   $$\frac{\Delta f}{f} = -\frac{v^2}{2 c^2} \approx -8.3 \times 10^{-11} \; (-7.1 \; \mu\text{s/天})$$

2. **广义相对论（重力红移）**：卫星在地球引力势场中高度较高，会导致时钟变快：
   
   $$\frac{\Delta f}{f} = \frac{\Delta \Phi}{c^2} \approx +5.3 \times 10^{-11} \; (+45.7 \; \mu\text{s/天})$$

两者的综合净效应为 **$+38.6 \; \mu\text{s/天}$**。为了补偿这一偏差，卫星时钟在发射前会被故意调低基准频率，从 $10.23$ MHz 调至 $10.22999999543$ MHz。`,

        "orbital_calculations.md": String.raw`# 航天动力学轨道计算参考

在二体中心引力系统中计算卫星速度、轨道周期以及轨道机动所需公式和数值步骤的技术摘要。

---

## 1. 使用 Vis-Viva 方程进行速度分析

活力公式（vis-viva equation）将卫星在轨道上任意一点的速度 ($v$) 与其距地心距离 ($r$) 以及半长轴 ($a$) 关联起来：

$$v = \sqrt{\mu \left( \frac{2}{r} - \frac{1}{a} \right)}$$

### 1.1 特例：圆轨道
在圆轨道中，距离 $r = a$。速度为恒定值：

$$v_{\text{circular}} = \sqrt{\frac{\mu}{a}}$$

对于高度为 $400$ km 的近地轨道（LEO，$a = 6771$ km）：其速度 $v \approx 7.67$ km/s。

### 1.2 拱点速度（近地点与远地点速度）
在椭圆轨道中，速度在近地点达到最大值，在远地点达到最小值。

1. **近地点速度 ($v_p$)**（此时距离 $r_p = a(1 - e)$）：
   
   $$v_p = \sqrt{\frac{\mu}{a} \left( \frac{1 + e}{1 - e} \right)}$$

2. **远地点速度 ($v_a$)**（此时距离 $r_a = a(1 + e)$）：
   
   $$v_a = \sqrt{\frac{\mu}{a} \left( \frac{1 - e}{1 + e} \right)}$$

---

## 2. 逃逸速度

无动力物体完全脱离地球引力场所必需的最小速度，此时物体处于抛物线轨道上（$e = 1$，比能量 $\varepsilon = 0$）：

$$v_{\text{escape}} = \sqrt{\frac{2\mu}{r}}$$

在地球表面（$r = 6371$ km）处：逃逸速度 $v_{\text{escape}} \approx 11.2$ km/s。

---

## 3. 霍曼转移轨道机动

霍曼转移是一种双脉冲共面轨道机动，用于利用椭圆转移轨道将卫星在两个不同半径（$r_1$ 和 $r_2$）的共面圆轨道之间进行转移。

### 3.1 步骤 1：初始状态
卫星在半径为 $r_1$ 的初始轨道上以圆轨道速度运行：

$$v_1 = \sqrt{\frac{\mu}{r_1}}$$

### 3.2 步骤 2：第一次加速点火 ($\Delta v_1$)
为了进入椭圆转移轨道（该转移轨道的近地点为 $r_1$，远地点为 $r_2$），我们计算转移轨道的半长轴 ($a_{tx}$ )：

$$a_{tx} = \frac{r_1 + r_2}{2}$$

转移轨道近地点所需的瞬时速度为：

$$v_{tx,1} = \sqrt{\mu \left( \frac{2}{r_1} - \frac{1}{a_{tx}} \right)}$$

第一次速度增量为：

$$\Delta v_1 = v_{tx,1} - v_1$$

### 3.3 步骤 3：第二次加速点火 ($\Delta v_2$)
当到达转移轨道的远地点（距离 $r = r_2$）时，卫星的瞬时速度为：

$$v_{tx,2} = \sqrt{\mu \left( \frac{2}{r_2} - \frac{1}{a_{tx}} \right)}$$

在半径为 $r_2$ 的最终工作轨道上，卫星需要保持圆轨道速度：

$$v_2 = \sqrt{\frac{\mu}{r_2}}$$

第二次速度增量为：

$$\Delta v_2 = v_2 - v_{tx,2}$$

### 3.4 总 Delta-V 预算
霍曼转移所需的总速度增量（Delta-V）为：

$$\Delta v_{\text{total}} = |\Delta v_1| + |\Delta v_2|$$`,

        "gnss_positioning_precision.md": String.raw`# GNSS 定位精度与信号频率

关于卫星定位系统中的信号结构、坐标计算误差以及几何精度因子（DOP）计算的数学与技术指南。

---

## 1. GNSS 频段

现代卫星导航系统通过多个无线电频率发射信号，以允许接收机消除电离层延迟并维持在复杂环境中的信号锁定。

### 1.1 GPS（美国）
- **L1 频段**：$1575.42$ MHz。广播民用粗捕获（C/A）码和军用 P(Y) 码。
- **L2 频段**：$1227.60$ MHz。通过与 L1 比较来测量电离层延迟。广播 L2C 和军用代码。
- **L5 频段**：$1176.45$ MHz。生命安全民用频段，具有更高的发射功率和更宽的带宽，抗干扰能力极强。

### 1.2 伽利略星座（欧盟）
- **E1 频段**：$1575.42$ MHz。与 GPS L1 频点相同，实现了系统间的民用导航互操作兼容性。
- **E5a / E5b 频段**：$1176.45$ MHz（E5a，与 L5 同频）和 $1207.14$ MHz（E5b）。用于高精度民用服务与高精密时钟同步。
- **E6 频段**：$1278.75$ MHz。用于商业服务（CS），通过精密单点定位（PPP）改正提供高精度服务（HAS）。

---

## 2. 伪距误差源分析

卫星与接收机之间的测量距离（伪距）包含必须建模消除或通过双差消除的系统误差：

$$\text{伪距误差} = d_{\text{orbit}} + d_{\text{clock}} + d_{\text{ion}} + d_{\text{trop}} + d_{\text{multipath}} + \eta$$

### 2.1 电离层延迟 ($d_{\text{ion}}$)
- 电离层（$50$ 至 $1000$ 公里高度）含有自由电子，会使无线电波发生折射。
- **改正**：由于折射率与频率有关（$d_{\text{ion}} \propto 1/f^2$），因此可以使用双频接收机（如比较 L1 和 L2 的延迟差）进行精确计算消除。

### 2.2 对流层延迟 ($d_{\text{trop}}$)
- 中性大气层（$0$ 至 $50$ 公里高度）由于干燥气体和水增气而延迟信号传播。
- **改正**：使用根据气压、温度和接收机高度角建立的经验公式模型（例如 Saastamoinen 模型或 Hopfield 模型）进行修正。

---

## 3. 几何精度因子（DOP）

DOP 是一个无量纲乘数，表示卫星空间几何分布对用户定位精度的放大程度。它由包含接收机指向每颗可见卫星的单位方向矢量的几何矩阵 $A$ 导出。

### 3.1 数学推导
设几何观测矩阵 $A$ 为：

$$A = \begin{bmatrix}
x_1 & y_1 & z_1 & 1 \\
x_2 & y_2 & z_2 & 1 \\
\vdots & \vdots & \vdots & \vdots \\
x_n & y_n & z_n & 1
\end{bmatrix}$$

接收机三维位置和接收机钟差的协方差矩阵 $Q$ 为：

$$Q = (A^T A)^{-1} = \begin{bmatrix}
q_{xx} & q_{xy} & q_{xz} & q_{xt} \\
q_{yx} & q_{yy} & q_{yz} & q_{yt} \\
q_{zx} & q_{zy} & q_{zz} & q_{zt} \\
q_{tx} & q_{ty} & q_{tz} & q_{tt}
\end{bmatrix}$$

### 3.2 DOP 参数定义
- **GDOP（几何精度因子）**：包含三维位置坐标和接收机钟差的整体定位几何精度。
  
  $$\text{GDOP} = \sqrt{q_{xx} + q_{yy} + q_{zz} + q_{tt}}$$

- **PDOP（位置精度因子）**：反映三维位置坐标（经度、纬度、高度）的几何精度。
  
  $$\text{PDOP} = \sqrt{q_{xx} + q_{yy} + q_{zz}}$$

- **HDOP（水平精度因子）**：反映二维水平面位置坐标（纬度、经度）的几何精度。
  
  $$\text{HDOP} = \sqrt{q_{xx} + q_{yy}}$$

- **VDOP（垂直精度因子）**：反映一维高度（海拔）坐标的几何精度。由于卫星仅在仰角大于零的地平线以上可见，VDOP 的值通常大于 HDOP。
  
  $$\text{VDOP} = \sqrt{q_{zz}}$$`
    }
};
