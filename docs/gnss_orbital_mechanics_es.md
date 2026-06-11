# Mecánica Orbital y Precisión de GNSS

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

Esto es calculado por el receptor dinámicamente utilizando la anomalía excéntrica $E$ resuelta a partir de la ecuación de Kepler.
