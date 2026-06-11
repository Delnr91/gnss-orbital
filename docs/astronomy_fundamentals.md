# Fundamentals of Space Astronomy and Reference Systems

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

The combined effect is **$+38.6 \; \mu\text{s/day}$**. To compensate, satellite clocks are tuned down before launch from $10.23$ MHz to $10.22999999543$ MHz.
