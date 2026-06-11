# Mission Operations and Tracking

After launch, a satellite lives or dies by its operations: tracking, commanding, station-keeping, and end-of-life disposal.

---

## Ground Stations and Passes

A LEO satellite is only visible from a given ground station for ~5-12 minutes per pass, a handful of times per day. Operators chain stations into networks (KSAT, AWS Ground Station, NASA Near Space Network) for more contact time. GEO satellites, fixed in the sky, enjoy continuous contact with one dish.

A satellite is visible when its **elevation** above the local horizon exceeds a mask angle (typically 5-10°), which is the same geometry that decides how many GNSS satellites your phone can see.

---

## Two-Line Elements (TLE)

The classic format for sharing orbits. Two 69-character lines encode epoch, mean motion, eccentricity, inclination, RAAN, argument of perigee, mean anomaly, and a drag term. TLEs are generated for the SGP4 propagator and are accurate to roughly 1-3 km, degrading within days — which is why they are refreshed continuously on sources like CelesTrak.

---

## Station-Keeping

Perturbations never sleep. GEO satellites drift east-west (triaxial Earth) and north-south (lunisolar pull, ~0.85°/year inclination growth) and burn ~50 m/s of delta-v per year to stay inside their assigned box (±0.05°). LEO constellations like Starlink use onboard electric propulsion and autonomous collision avoidance.

---

## Launch Windows

A launch window opens when the launch site rotates under the target orbital plane. Planar windows are daily and short (minutes for rendezvous with the ISS); interplanetary windows follow synodic periods — Mars opens for a few weeks every ~26 months.

---

## End of Life

Disposal is now part of mission design: LEO satellites deorbit to burn up in the atmosphere; GEO satellites raise to a graveyard orbit and passivate (vent propellant, discharge batteries) so they cannot explode and create debris.
