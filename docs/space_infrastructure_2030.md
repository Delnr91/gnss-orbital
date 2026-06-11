# Space Infrastructure and Constellations Roadmap to 2030

The landscape of space infrastructure by 2030 is defined by hybrid, multi-orbital constellations integrating communication (LEO) and navigation (MEO) systems.

---

## 1. The EU IRIS² Constellation (2027–2030)

IRIS² (Infrastructure for Resilience, Interconnection and Security by Satellite) is Europe's secure communication constellation.

- **System Architecture**: Multi-orbital hybrid configuration.
  - LEO Component: High-throughput, low-latency broadband nodes (governmental and commercial).
  - MEO Component: Medium Earth Orbit nodes providing wide-area coverage and links to navigation systems.
- **Quantum Encryption**: Integrates Quantum Key Distribution (QKD) payloads to secure communications against future cryptographic threats.
- **Synergy with Galileo**: Provides cross-link synchronization and satellite-based augmentation systems (SBAS).

---

## 2. Next-Generation Navigation Systems (2030 Roadmap)

### GPS III and IIIF
- **M-code**: Military signal designed to resist jamming and spoofing, featuring high-power spot beams.
- **L1C Signal**: Interoperable civil signal compatible with Galileo E1, GLONASS L1OC, and BeiDou B1C.
- **Laser Retroreflector Arrays**: Enables satellite laser ranging (SLR) to calibrate orbits independently of radio signals.

### Galileo Second Generation (G2G)
- **Electric Propulsion**: Speeds up transit from transfer orbit to operational slot, allowing faster constellation replenishment.
- **Inter-Satellite Links (ISL)**: Satellites communicate directly in space. This reduces dependence on ground monitoring stations and improves real-time orbit determination accuracy.
- **Onboard Atomic Clocks**: High-performance rubidium and passive hydrogen maser clocks, offering sub-nanosecond synchronization.

### BeiDou-4 (BDS-4)
- **High-Precision LEO Augmentation**: Incorporates a LEO constellation to broadcast correction messages, reducing receiver convergence times for PPP positioning from minutes to seconds.
- **Integrated Communications**: Enhanced short-message and search-and-rescue services.

---

## 3. Collaborative Space Mechanics

Operating these constellations requires precise orbit design to prevent collisions and optimize coverage:
- **Station Keeping**: Active orbit maintenance to counter Earth's oblateness [[docs/orbital_perturbations.md]].
- **Decommissioning**: Satellites must be moved to graveyard orbits at end-of-life:
  - LEO: De-orbit to burn up in the atmosphere within 5 years.
  - MEO/GEO: Propelled to a graveyard orbit ($a > a_{\text{nominal}} + 300$ km).
- **Hohmann Transfer Orbit**: Fundamental transfer maneuver used to transition satellites from launch trajectories to operational slots [[docs/api_reference.md]].
