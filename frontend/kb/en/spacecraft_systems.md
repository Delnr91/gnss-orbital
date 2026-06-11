# Spacecraft Systems Anatomy

A satellite is a flying power station, radio tower, and computer that must survive vacuum, radiation, and ±200 °C temperature swings for years without a single repair visit.

---

## The Bus and the Payload

The **payload** is the reason the mission exists: navigation signal generators on GPS, transponders on communication satellites, telescopes on observation missions. The **bus** is everything that keeps the payload alive — structure, power, thermal control, attitude control, communications, and command/data handling.

---

## Electrical Power Subsystem (EPS)

Solar arrays convert sunlight (~1361 W/m² at Earth) into power; batteries (today lithium-ion) carry the satellite through eclipse. A GPS III satellite generates ~4.5 kW. Power degrades ~2-3% per year from radiation damage, so arrays are oversized at launch.

---

## Attitude Determination and Control (ADCS)

Star trackers, sun sensors, and gyroscopes measure orientation; **reaction wheels** spin to rotate the spacecraft without propellant; magnetorquers desaturate the wheels using Earth's magnetic field. Pointing accuracy ranges from degrees (cubesats) to arcseconds (space telescopes).

---

## Propulsion

Chemical thrusters (hydrazine monopropellant, ~220 s specific impulse) deliver quick burns. Electric propulsion (ion or Hall-effect, 1500-3000 s specific impulse) trades thrust for efficiency — modern GEO satellites use it for orbit raising and station-keeping, cutting propellant mass dramatically.

---

## Thermal and Communications

Multi-layer insulation blankets, radiators, and heat pipes keep electronics within limits while one side faces the Sun and the other faces 2.7 K deep space. The communication subsystem closes the link with ground stations; the **link budget** balances transmit power, antenna gain, distance loss ($\propto 1/d^2$), and receiver noise.
