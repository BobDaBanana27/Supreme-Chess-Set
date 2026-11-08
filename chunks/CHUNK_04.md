# Chunk 04 — Magnetic Coupling & Hall Effect Sensor Physics Simulation

## Overview & Work Completed
- **Physics Modeling:** Simulated the axial magnetic dipole field using the Biot-Savart magnetostatic formula for a 5.0 mm dia × 2.0 mm thk N35 Neodymium magnet.
- **Actuation & Hysteresis Margin:** Derived the vertical mechanical stackup tolerance ($z = 2.20\text{ mm}$ between magnet and sensor active silicon). At this distance, the seated field is 385 Gauss—yielding a **7.7× safety factor** over the digital Hall sensor operate threshold ($B_{op} \approx 40\text{ Gauss}$).
- **Crosstalk Elimination:** Analyzed lateral magnetic fringe decay over the 18.0 mm slot pitch. At the neighboring slot ($r = 18.0\text{ mm}$), the residual field decays to $< 3\text{ Gauss}$, far below the release threshold ($B_{rp} \approx 20\text{ Gauss}$), mathematically preventing false triggers from neighboring captured pieces.
- **Deliverables Produced:**
  - `docs/MAGNETIC_DESIGN.md`: Full mathematical derivation, tolerance stackup tables, and hysteresis safety analysis.
  - `assets/hour04_magnetic_physics.svg`: Assembly cross-section diagram and Biot-Savart flux-vs-distance curve.

## Work Package Deliverables
- [Magnetic Coupling & Physics Analysis](../docs/MAGNETIC_DESIGN.md)
- [Magnetic Simulation & Stackup Diagram](../assets/hour04_magnetic_physics.svg)

![Hour 04 Magnetic Simulation](../assets/hour04_magnetic_physics.svg)
