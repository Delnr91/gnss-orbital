# Maniobras Orbitales y Transferencias

Cambiar de órbita cuesta propelente. Los diseñadores de misión miden cada maniobra en **delta-v** ($\Delta v$): el cambio total de velocidad que los motores deben entregar.

---

## Transferencia de Hohmann

La transferencia de Hohmann es la transferencia de mínima energía con dos encendidos entre dos órbitas circulares coplanares. Usa una elipse de transferencia cuyo perigeo toca la órbita interior y cuyo apogeo toca la exterior.

Primer encendido (saliendo de la órbita interior de radio $r_1$):

$$\Delta v_1 = \sqrt{\frac{\mu}{r_1}}\left(\sqrt{\frac{2 r_2}{r_1 + r_2}} - 1\right)$$

Segundo encendido (circularización en el radio $r_2$):

$$\Delta v_2 = \sqrt{\frac{\mu}{r_2}}\left(1 - \sqrt{\frac{2 r_1}{r_1 + r_2}}\right)$$

Una transferencia de LEO (400 km) a GEO necesita aproximadamente $\Delta v \approx 3.9$ km/s en total y tarda unas 5.2 horas (medio periodo de la elipse de transferencia).

---

## Transferencia Bi-Elíptica

Para razones muy grandes $r_2 / r_1 > 11.94$, una transferencia bi-elíptica de tres encendidos a través de un apogeo intermedio lejano puede superar a la de Hohmann en delta-v total, a costa de un tiempo de vuelo mucho mayor.

---

## Cambios de Plano

Rotar el plano orbital es caro. Un cambio puro de inclinación de ángulo $\Delta i$ a velocidad $v$ cuesta:

$$\Delta v = 2 v \sin\left(\frac{\Delta i}{2}\right)$$

Un cambio de plano de 28.5° en LEO (~7.7 km/s) cuesta ~3.8 km/s — casi tanto como toda la transferencia LEO-GEO. Por eso son tan valiosos los sitios de lanzamiento cerca del ecuador y por eso los cambios de plano se combinan con encendidos en apogeo, donde la velocidad es mínima.

---

## Presupuesto de Delta-v

Toda misión lleva una tabla de presupuesto de delta-v: inyección de lanzamiento, encendidos de transferencia, cambios de plano, mantenimiento de posición (GEO necesita ~50 m/s por año), evasión de colisiones y disposición final (órbita cementerio o reentrada). La ecuación del cohete convierte el presupuesto en masa de propelente:

$$\frac{m_0}{m_f} = e^{\Delta v / (I_{sp} g_0)}$$
