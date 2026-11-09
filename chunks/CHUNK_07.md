# Chunk 07 — PCB Layout & Routing (KiCad 10)

## Overview & Work Completed
- **Motherboard Layout:** Completed the 2-layer PCB layout for `hardware/supreme_chess.kicad_pcb` (75.0 mm × 48.0 mm). Routed the RP2040-Zero castellated module, OLED 4-pin header, FFC interconnect J1, tactile pushbuttons, and M2.5 mounting bosses with a continuous bottom-layer ground plane.
- **Sensor Strip Layout:** Designed the ultra-slim 155.0 mm × 22.0 mm sensor strip (`hardware/sensor_strip.kicad_pcb`), positioning 15 SOT-23 Hall ICs on exact 9.2 mm centers to align underneath the capture tray piece sockets.
- **Manufacturing Validation:** Successfully executed `kicad-cli pcb export svg` to generate vector PCB layer plots (`assets/hour07_motherboard_pcb.svg` and `assets/hour07_sensor_strip_pcb.svg`) directly from the KiCad PCB databases.
- **Deliverables Produced:**
  - `hardware/supreme_chess.kicad_pcb`: Validated motherboard PCB layout.
  - `hardware/sensor_strip.kicad_pcb`: Validated 15-slot capture sensor strip PCB layout.
  - `docs/PCB_DESIGN.md`: 2-layer FR-4 stackup specification, DRC clearance rules, and JLCPCB fabrication constraints.
  - `assets/hour07_pcb_layout.svg`: High-resolution visual board renders and stackup diagram.
  - `assets/hour07_motherboard_pcb.svg` & `assets/hour07_sensor_strip_pcb.svg`: Direct KiCad CLI exports.

## Work Package Deliverables
- [KiCad Motherboard PCB File](../hardware/supreme_chess.kicad_pcb)
- [KiCad Sensor Strip PCB File](../hardware/sensor_strip.kicad_pcb)
- [PCB Design Specification](../docs/PCB_DESIGN.md)
- [PCB Layout & Stackup Overview](../assets/hour07_pcb_layout.svg)

![Hour 07 PCB Layout & Stackup](../assets/hour07_pcb_layout.svg)
