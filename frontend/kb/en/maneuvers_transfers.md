# Orbital Maneuvers and Transfers

Changing orbits costs propellant. Mission designers measure every maneuver in **delta-v** ($\Delta v$): the total change in velocity the engines must deliver.

---

## Hohmann Transfer

The Hohmann transfer is the minimum-energy two-burn transfer between two coplanar circular orbits. It uses an elliptical transfer orbit whose perigee touches the inner orbit and whose apogee touches the outer orbit.

First burn (leaving the inner orbit of radius $r_1$):

$$\Delta v_1 = \sqrt{\frac{\mu}{r_1}}\left(\sqrt{\frac{2 r_2}{r_1 + r_2}} - 1\right)$$

Second burn (circularizing at radius $r_2$):

$$\Delta v_2 = \sqrt{\frac{\mu}{r_2}}\left(1 - \sqrt{\frac{2 r_1}{r_1 + r_2}}\right)$$

A LEO (400 km) to GEO transfer needs roughly $\Delta v \approx 3.9$ km/s total and takes about 5.2 hours (half the transfer ellipse period).

---

## Bi-Elliptic Transfer

For very large ratios $r_2 / r_1 > 11.94$, a three-burn bi-elliptic transfer through a distant intermediate apogee can beat the Hohmann transfer in total delta-v, at the cost of much longer flight time.

---

## Plane Changes

Rotating the orbital plane is expensive. A pure inclination change of angle $\Delta i$ at speed $v$ costs:

$$\Delta v = 2 v \sin\left(\frac{\Delta i}{2}\right)$$

A 28.5° plane change in LEO (~7.7 km/s) costs ~3.8 km/s — nearly as much as the whole LEO-to-GEO transfer. That is why launch sites near the equator are so valuable and why plane changes are combined with apogee burns, where velocity is lowest.

---

## Delta-v Budget

Every mission carries a delta-v budget table: launch injection, transfer burns, plane changes, station-keeping (GEO needs ~50 m/s per year), collision avoidance, and final disposal (graveyard orbit or deorbit). The rocket equation converts the budget into propellant mass:

$$\frac{m_0}{m_f} = e^{\Delta v / (I_{sp} g_0)}$$
