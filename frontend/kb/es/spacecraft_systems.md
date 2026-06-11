# Anatomía de los Sistemas de un Satélite

Un satélite es una central eléctrica, una torre de radio y una computadora voladora que debe sobrevivir al vacío, la radiación y oscilaciones térmicas de ±200 °C durante años sin una sola visita de reparación.

---

## El Bus y la Carga Útil

La **carga útil** es la razón de la misión: generadores de señal de navegación en GPS, transpondedores en satélites de comunicaciones, telescopios en misiones de observación. El **bus** es todo lo que mantiene viva la carga útil — estructura, potencia, control térmico, control de actitud, comunicaciones y manejo de comandos/datos.

---

## Subsistema de Potencia Eléctrica (EPS)

Los paneles solares convierten la luz solar (~1361 W/m² en la Tierra) en potencia; las baterías (hoy de ion-litio) sostienen al satélite durante los eclipses. Un satélite GPS III genera ~4.5 kW. La potencia se degrada ~2-3% por año por daño de radiación, así que los paneles se sobredimensionan al lanzamiento.

---

## Determinación y Control de Actitud (ADCS)

Los rastreadores de estrellas, sensores solares y giróscopos miden la orientación; las **ruedas de reacción** giran para rotar la nave sin propelente; los magnetorquers desaturan las ruedas usando el campo magnético terrestre. La precisión de apuntamiento va de grados (cubesats) a segundos de arco (telescopios espaciales).

---

## Propulsión

Los propulsores químicos (hidracina monopropelente, ~220 s de impulso específico) dan encendidos rápidos. La propulsión eléctrica (iónica o de efecto Hall, 1500-3000 s de impulso específico) cambia empuje por eficiencia — los satélites GEO modernos la usan para elevación de órbita y mantenimiento de posición, recortando drásticamente la masa de propelente.

---

## Térmico y Comunicaciones

Mantas de aislamiento multicapa, radiadores y tubos de calor mantienen la electrónica dentro de límites mientras un lado mira al Sol y el otro al espacio profundo a 2.7 K. El subsistema de comunicaciones cierra el enlace con las estaciones terrestres; el **presupuesto de enlace** balancea potencia transmitida, ganancia de antena, pérdida por distancia ($\propto 1/d^2$) y ruido del receptor.
