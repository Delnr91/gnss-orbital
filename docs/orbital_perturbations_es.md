# Perturbaciones Orbitales No Keplerianas

En la astrodinámica del mundo real, los satélites no siguen elipses keplerianas perfectas. Las fuerzas no gravitacionales y no esféricas perturban los elementos orbitales a lo largo del tiempo.

---

## 1. Achatamiento de la Tierra (Perturbación $J_2$)

La Tierra no es una esfera perfecta; el achatamiento polar crea un ensanchamiento de masa en el ecuador. Este potencial no esférico se modela mediante armónicos esféricos, dominados por el coeficiente armónico zonal $J_2 = 1.08263 \times 10^{-3}$.

El potencial $J_2$ introduce tasas de deriva seculares (lineales) en tres elementos orbitales:
1. **Regresión del Nodo Ascendente ($\dot{\Omega}$)**: El plano de la órbita gira alrededor del eje de rotación de la Tierra.
2. **Precesión del Perigeo ($\dot{\omega}$)**: El eje mayor de la elipse gira dentro del plano orbital.
3. **Corrección de la Tasa de Anomalía Media ($\dot{M_0}$)**: Corrige el movimiento medio.

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

La SRP es crítica para los satélites de navegación MEO (GPS/Galileo), donde es la fuerza no gravitatoria más grande y debe modelarse para mantener la precisión en la determinación de la órbita.
