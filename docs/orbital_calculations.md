# Astrodynamics Orbital Calculations Reference

A technical summary of formulas and numerical steps required to compute velocities, period lengths, and orbital maneuvers in a two-body central gravitational system.

---

## 1. Velocity Analysis Using Vis-Viva

The vis-viva equation relates a satellite's speed ($v$) at any point along its orbit to its distance ($r$) from Earth's center and the semi-major axis ($a$):

$$v = \sqrt{\mu \left( \frac{2}{r} - \frac{1}{a} \right)}$$

### 1.1 Special Case: Circular Orbits
In a circular orbit, $r = a$. The velocity is constant:

$$v_{\text{circular}} = \sqrt{\frac{\mu}{a}}$$

For LEO orbits at $400$ km altitude ($a = 6771$ km): $v \approx 7.67$ km/s.

### 1.2 Velocity at Absides (Apoapsis and Periapsis)
In an elliptical orbit, velocity reaches its maximum at periapsis and its minimum at apoapsis.

1. **Periapsis Velocity ($v_p$)** (where $r_p = a(1 - e)$):
   
   $$v_p = \sqrt{\frac{\mu}{a} \left( \frac{1 + e}{1 - e} \right)}$$

2. **Apoapsis Velocity ($v_a$)** (where $r_a = a(1 + e)$):
   
   $$v_a = \sqrt{\frac{\mu}{a} \left( \frac{1 - e}{1 + e} \right)}$$

---

## 2. Escape Velocity

The minimum speed required for an unpropelled body to escape Earth's gravitational field completely, moving on a parabolic trajectory ($e = 1$, specific energy $\varepsilon = 0$):

$$v_{\text{escape}} = \sqrt{\frac{2\mu}{r}}$$

At Earth's surface ($r = 6371$ km): $v_{\text{escape}} \approx 11.2$ km/s.

---

## 3. The Hohmann Transfer Maneuver

A Hohmann transfer is a two-impulse coplanar maneuver used to transition a satellite between two circular coplanar orbits of different radii ($r_1$ and $r_2$) using an elliptical transfer orbit.

```
                      Transfer Ellipse
                     . - - - - - - - - .
                   .         .         .
                 .         Earth         .
                .            o            .  Circular Orbit 2 (r2)
                .                         .___________
                .                         .          |
                 .         . . .         .           |
                   .     .       .     .             |
                     . - - - - - - - - .             |
                      Circular Orbit 1 (r1)          v
                                                   Delta-v 2
```

### 3.1 Step 1: Initial State
The satellite orbits at radius $r_1$ with circular speed:

$$v_1 = \sqrt{\frac{\mu}{r_1}}$$

### 3.2 Step 2: First Burn ($\Delta v_1$)
To enter the elliptical transfer orbit, which has a periapsis of $r_1$ and apogee of $r_2$, we compute the transfer semi-major axis ($a_{tx}$):

$$a_{tx} = \frac{r_1 + r_2}{2}$$

The required velocity at periapsis of the transfer orbit is:

$$v_{tx,1} = \sqrt{\mu \left( \frac{2}{r_1} - \frac{1}{a_{tx}} \right)}$$

The first velocity increment is:

$$\Delta v_1 = v_{tx,1} - v_1$$

### 3.3 Step 3: Second Burn ($\Delta v_2$)
Upon arriving at the apogee of the transfer orbit ($r = r_2$), the satellite's speed is:

$$v_{tx,2} = \sqrt{\mu \left( \frac{2}{r_2} - \frac{1}{a_{tx}} \right)}$$

The final circular orbit at radius $r_2$ requires circular speed:

$$v_2 = \sqrt{\frac{\mu}{r_2}}$$

The second velocity increment is:

$$\Delta v_2 = v_2 - v_{tx,2}$$

### 3.4 Total Delta-V Budget
The total delta-v required for the Hohmann transfer is:

$$\Delta v_{\text{total}} = |\Delta v_1| + |\Delta v_2|$$
