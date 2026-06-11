# Operaciones de Misión y Seguimiento

Después del lanzamiento, un satélite vive o muere por sus operaciones: seguimiento, comandos, mantenimiento de posición y disposición al final de su vida.

---

## Estaciones Terrestres y Pases

Un satélite LEO solo es visible desde una estación terrestre durante ~5-12 minutos por pase, unas pocas veces al día. Los operadores encadenan estaciones en redes (KSAT, AWS Ground Station, Near Space Network de NASA) para más tiempo de contacto. Los satélites GEO, fijos en el cielo, gozan de contacto continuo con una sola antena.

Un satélite es visible cuando su **elevación** sobre el horizonte local supera un ángulo de máscara (típicamente 5-10°) — la misma geometría que decide cuántos satélites GNSS ve tu teléfono.

---

## Elementos de Dos Líneas (TLE)

El formato clásico para compartir órbitas. Dos líneas de 69 caracteres codifican época, movimiento medio, excentricidad, inclinación, RAAN, argumento del perigeo, anomalía media y un término de arrastre. Los TLE se generan para el propagador SGP4 y tienen precisión de ~1-3 km, degradándose en días — por eso se refrescan continuamente en fuentes como CelesTrak.

---

## Mantenimiento de Posición

Las perturbaciones nunca duermen. Los satélites GEO derivan este-oeste (Tierra triaxial) y norte-sur (atracción lunisolar, ~0.85°/año de crecimiento de inclinación) y queman ~50 m/s de delta-v por año para permanecer en su caja asignada (±0.05°). Las constelaciones LEO como Starlink usan propulsión eléctrica a bordo y evasión autónoma de colisiones.

---

## Ventanas de Lanzamiento

Una ventana de lanzamiento se abre cuando el sitio de lanzamiento rota bajo el plano orbital objetivo. Las ventanas planares son diarias y cortas (minutos para encuentros con la ISS); las interplanetarias siguen periodos sinódicos — Marte se abre unas semanas cada ~26 meses.

---

## Fin de Vida

La disposición final es ya parte del diseño de misión: los satélites LEO se desorbitan para quemarse en la atmósfera; los GEO se elevan a una órbita cementerio y se pasivan (ventean propelente, descargan baterías) para que no puedan explotar y crear basura.
