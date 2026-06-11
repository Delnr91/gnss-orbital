# Referencia de Cálculos Orbitales de Astrodinámica

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
En una órbita elíptica, la velocidad alcanza su valor máximo en el perigeo (periapsis) y su mínimo en el apogeo (apoapsis).

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

$$\Delta v_{\text{total}} = |\Delta v_1| + |\Delta v_2|$$
