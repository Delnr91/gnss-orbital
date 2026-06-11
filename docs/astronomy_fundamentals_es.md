# Fundamentos de Astronomía Espacial y Sistemas de Referencia

La operación de naves espaciales y sistemas globales de navegación por satélite requiere marcos de referencia y escalas de tiempo de alta precisión para sincronizar la mecánica orbital y los datos de observación terrestres.

---

## 1. Marcos de Referencia Coordenados Celestiales

La astrodinámica y el posicionamiento por satélite requieren marcos de coordenadas distintos para modelar la mecánica espacial (inercial) y el seguimiento del receptor (fijo a la Tierra).

### 1.1 Marco Inercial Centrado en la Tierra (ECI)
- **Definición**: Un marco de coordenadas no giratorio con su origen en el centro de masa de la Tierra.
- **Ejes**:
  - El eje $X$ apunta hacia el Equinoccio Vernal (la dirección del Sol al inicio de la primavera).
  - El eje $Z$ apunta a lo largo del eje de rotación de la Tierra (Polo Norte).
  - El eje $Y$ completa el sistema de coordenadas cartesianas diestras.
- **Época Estándar**: **J2000.0** (definida por la orientación de la Tierra a las 12:00 UTC del 1 de enero de 2000).
- **Aplicación**: Se utiliza para resolver las ecuaciones de movimiento y propagar órbitas, ya que las leyes de Newton se cumplen en marcos inerciales.

### 1.2 Marco Fijo a la Tierra, Centrado en la Tierra (ECEF)
- **Definición**: Un marco de coordenadas giratorio que se mueve con la Tierra.
- **Ejes**:
  - El eje $X$ apunta hacia el Meridiano de Greenwich (longitud $0^\circ$).
  - El eje $Z$ apunta a lo largo del eje de rotación de la Tierra.
  - El eje $Y$ completa el sistema de coordenadas diestras (longitud $90^\circ$ Este).
- **Referencia Estándar**: **ITRF** (Marco de Referencia Terrestre Internacional) o **WGS 84** (Sistema Geodésico Mundial 1984).
- **Aplicación**: Se utiliza para localizar receptores en la superficie de la Tierra y calcular las coordenadas de posicionamiento del usuario.

---

## 2. Escalas de Tiempo Espaciales

Los sistemas espaciales requieren un cronometraje uniforme porque el UTC estándar se ve perturbado por la velocidad de rotación variable de la Tierra.

### 2.1 Tiempo Atómico Internacional (TAI)
- **Definición**: Una escala de tiempo altamente estable y continua derivada de una red mundial de relojes atómicos.
- **Unidad**: El segundo SI al nivel del mar.
- **Desviación**: El TAI no introduce segundos intercalares (leap seconds).

### 2.2 Tiempo Universal Coordinado (UTC)
- **Definición**: La escala de tiempo civil sincronizada con la rotación de la Tierra (UT1) utilizando segundos intercalares.
- **Restricción**: El UTC se ajusta mediante segundos intercalares para que la diferencia $|UT1 - UTC| < 0.9$ segundos.
- **Relación con el TAI**: Actualmente, $TAI - UTC = 37$ segundos (a partir de 2026).

### 2.3 Tiempo GPS (GPST)
- **Definición**: Una escala de tiempo continua utilizada por la constelación GPS.
- **Época**: 6 de enero de 1980.
- **Desfase**: El GPST se sincronizó con el UTC en su época de inicio. Dado que no introduce segundos intercalares, permanece desfasado del TAI por una constante:
  
  $$TAI - GPST = 19 \; \text{segundos}$$
  
  $$GPST - UTC = 18 \; \text{segundos} \; (\text{a partir de 2026})$$

---

## 3. Efectos Relativistas en los Relojes de GNSS

Los relojes atómicos que orbitan en ranuras MEO experimentan cambios de velocidad y gravedad relativistas en comparación con los receptores terrestres:

1. **Relatividad Especial (Velocidad)**: La velocidad del satélite ($v \approx 3.9$ km/s) ralentiza su reloj:
   
   $$\frac{\Delta f}{f} = -\frac{v^2}{2 c^2} \approx -8.3 \times 10^{-11} \; (-7.1 \; \mu\text{s/día})$$

2. **Relatividad General (Potencial Gravitatorio)**: El satélite se encuentra a mayor altura en el potencial gravitatorio de la Tierra, lo que acelera su reloj:
   
   $$\frac{\Delta f}{f} = \frac{\Delta \Phi}{c^2} \approx +5.3 \times 10^{-11} \; (+45.7 \; \mu\text{s/día})$$

El efecto neto combinado es de **$+38.6 \; \mu\text{s/día}$**. Para compensarlo, los relojes de los satélites se ajustan antes del lanzamiento de $10.23$ MHz a $10.22999999543$ MHz.
