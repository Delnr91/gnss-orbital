# The Space Environment

Orbit is not empty. Drag, radiation, debris, and space weather shape every mission's lifetime and design.

---

## Atmospheric Drag

Below ~800 km, residual atmosphere steadily drains orbital energy. Drag acceleration follows:

$$a_D = \frac{1}{2} \rho v^2 \frac{C_D A}{m}$$

The ballistic coefficient $m / (C_D A)$ decides how fast an orbit decays. The ISS at 400 km loses ~2 km of altitude per month and needs periodic reboosts. During solar maximum the upper atmosphere puffs up and drag can increase tenfold.

---

## Radiation Belts and Single-Event Upsets

The Van Allen belts trap energetic protons and electrons. The inner belt (~1000-6000 km) is proton-dominated; the outer belt (~13,000-60,000 km) is electron-dominated. GPS satellites at 20,200 km fly through the heart of the outer belt, which is why their electronics are radiation-hardened. A single energetic particle can flip a memory bit — a **single-event upset** — so critical systems use error-correcting memory and voting logic.

---

## Orbital Debris

More than 36,000 tracked objects larger than 10 cm orbit Earth, plus hundreds of millions of smaller fragments. At LEO closing speeds (~10-14 km/s) a 1 cm bolt carries the energy of a hand grenade. The **Kessler syndrome** describes a cascade where collisions generate debris that causes more collisions. Mitigation rules now require deorbiting LEO satellites within 5 years of end-of-mission (FCC, 2024) and moving GEO satellites to a graveyard orbit ~300 km above the belt.

---

## Space Weather

Solar flares and coronal mass ejections compress the magnetosphere, swell the atmosphere (more drag), disturb the ionosphere (GNSS errors grow), and can charge spacecraft surfaces to kilovolts. Operators monitor indices like Kp and F10.7 and sometimes put satellites in safe mode during major storms.
