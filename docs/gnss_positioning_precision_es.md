# Precisión de Posicionamiento GNSS y Frecuencias de Señal

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

- **HDOP (DOP Horizontal)**: Precisión horizontal 2D (Latitud, Longitud).
  
  $$\text{HDOP} = \sqrt{q_{xx} + q_{yy}}$$

- **VDOP (DOP Vertical)**: Precisión de altitud 1D (generalmente mayor que la HDOP debido a que los satélites solo son visibles por encima del horizonte).
  
  $$\text{VDOP} = \sqrt{q_{zz}}$$
