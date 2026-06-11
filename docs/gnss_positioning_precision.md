# GNSS Positioning Precision and Signal Frequencies

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
  
  $$\text{VDOP} = \sqrt{q_{zz}}$$
