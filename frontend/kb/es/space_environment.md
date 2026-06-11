# El Entorno Espacial

La órbita no está vacía. El arrastre, la radiación, la basura espacial y el clima espacial moldean la vida útil y el diseño de toda misión.

---

## Arrastre Atmosférico

Por debajo de ~800 km, la atmósfera residual drena energía orbital constantemente. La aceleración de arrastre sigue:

$$a_D = \frac{1}{2} \rho v^2 \frac{C_D A}{m}$$

El coeficiente balístico $m / (C_D A)$ decide qué tan rápido decae una órbita. La ISS a 400 km pierde ~2 km de altitud por mes y necesita reimpulsos periódicos. Durante el máximo solar la atmósfera superior se infla y el arrastre puede multiplicarse por diez.

---

## Cinturones de Radiación y Eventos Únicos

Los cinturones de Van Allen atrapan protones y electrones energéticos. El cinturón interior (~1000-6000 km) está dominado por protones; el exterior (~13,000-60,000 km) por electrones. Los satélites GPS a 20,200 km vuelan por el corazón del cinturón exterior — por eso su electrónica está endurecida contra radiación. Una sola partícula energética puede voltear un bit de memoria — un **single-event upset** — así que los sistemas críticos usan memoria con corrección de errores y lógica por votación.

---

## Basura Orbital

Más de 36,000 objetos rastreados mayores de 10 cm orbitan la Tierra, más cientos de millones de fragmentos menores. A velocidades de cierre en LEO (~10-14 km/s) un tornillo de 1 cm lleva la energía de una granada de mano. El **síndrome de Kessler** describe una cascada donde las colisiones generan basura que causa más colisiones. Las reglas de mitigación ahora exigen desorbitar los satélites LEO dentro de 5 años del fin de misión (FCC, 2024) y mover los GEO a una órbita cementerio ~300 km sobre el cinturón.

---

## Clima Espacial

Las fulguraciones solares y eyecciones de masa coronal comprimen la magnetosfera, inflan la atmósfera (más arrastre), perturban la ionosfera (crecen los errores GNSS) y pueden cargar las superficies de la nave a kilovoltios. Los operadores monitorean índices como Kp y F10.7 y a veces ponen los satélites en modo seguro durante tormentas mayores.
