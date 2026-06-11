# Hoja de Ruta de la Infraestructura Espacial y Constelaciones al 2030

El panorama de la infraestructura espacial para 2030 está definido por constelaciones híbridas y multiorbitales que integran sistemas de comunicación (LEO) y navegación (MEO).

---

## 1. La Constelación IRIS² de la UE (2027–2030)

IRIS² (Infraestructura para la Resiliencia, Interconexión y Seguridad por Satélite) es la constelación de comunicaciones seguras de Europa.

- **Arquitectura del Sistema**: Configuración híbrida multiorbital.
  - Componente LEO: Nodos de banda ancha de alto rendimiento y baja latencia (gubernamentales y comerciales).
  - Componente MEO: Nodos de órbita terrestre media que proporcionan cobertura de área amplia y enlaces a sistemas de navegación.
- **Cifrado Cuántico**: Integra cargas útiles de Distribución de Claves Cuánticas (QKD) para proteger las comunicaciones contra futuras amenazas criptográficas.
- **Sinergia con Galileo**: Proporciona sincronización de enlaces cruzados y sistemas de aumentación basados en satélites (SBAS).

---

## 2. Sistemas de Navegación de Próxima Generación (Hoja de Ruta al 2030)

### GPS III y IIIF
- **Código M**: Señal militar diseñada para resistir interferencias y suplantaciones de identidad, con haces focalizados de alta potencia.
- **Señal L1C**: Señal civil interoperable compatible con Galileo E1, GLONASS L1OC y BeiDou B1C.
- **Matrices de retrorreflectores láser**: Permite el rango láser por satélite (SLR) para calibrar órbitas independientemente de las señales de radio.

### Galileo Segunda Generación (G2G)
- **Propulsión Eléctrica**: Acelera el tránsito desde la órbita de transferencia hasta la ranura operativa, permitiendo una reposición más rápida de la constelación.
- **Enlaces Inter-Satelitales (ISL)**: Los satélites se comunican directamente en el espacio. Esto reduce la dependencia de las estaciones terrestres y mejora la precisión de determinación orbital en tiempo real.
- **Relojes Atómicos a Bordo**: Relojes de rubidio y máseres de hidrógeno pasivos de alto rendimiento, que ofrecen sincronización de sub-nanosegundos.

### BeiDou-4 (BDS-4)
- **Aumentación LEO de Alta Precisión**: Incorpora una constelación LEO para transmitir mensajes de corrección, reduciendo los tiempos de convergencia del receptor para el posicionamiento PPP de minutos a segundos.
- **Comunicaciones Integradas**: Servicios mejorados de mensajes cortos y búsqueda y rescate.

---

## 3. Mecánica Espacial Colaborativa

La operación de estas constelaciones requiere un diseño orbital preciso para evitar colisiones y optimizar la cobertura:
- **Mantenimiento de Estación (Station Keeping)**: Mantenimiento activo de la órbita para contrarrestar la deformación de la Tierra.
- **Retiro de Servicio (Decommissioning)**: Los satélites deben trasladarse a órbitas cementerio al final de su vida útil:
  - LEO: Desorbitar para quemarse en la atmósfera en un plazo de 5 años.
  - MEO/GEO: Propulsados a una órbita cementerio ($a > a_{\text{nominal}} + 300$ km).
- **Órbita de Transferencia de Hohmann**: Maniobra de transferencia fundamental utilizada para la transición de satélites desde trayectorias de lanzamiento a sus ranuras operativas.
