# Chunk 05 — Electrical Schematic Design (KiCad)

## Overview & Work Completed
- **Schematic Engineering:** Developed the complete system schematic in KiCad 10 (`hardware/supreme_chess.kicad_sch` and project configuration `hardware/supreme_chess.kicad_pro`).
- **Core Processing & Power Subsystem:** Integrated the RP2040-Zero MCU, TP4056 Lithium battery charging controller with DW01A protection IC, SPDT slide power switch SW1, 10µF/0.1µF rail decoupling filter bank, and battery voltage divider network (GP26/ADC0).
- **Interface & Bus Topology:** Designed the 400kHz I2C display interface for the 0.96" SSD1306 OLED with 4.7kΩ pull-up resistors, navigation tactile buttons (SW2 Mode, SW3 Reset), and the 6-pin FFC inter-board ribbon connector J1 routing 3.3V, GND, Latch, Clock, and dual serial data streams to the capture trays.
- **Verification:** Verified schematic symbol netlists and BOM generation using `kicad-cli sch export bom`.
- **Deliverables Produced:**
  - `hardware/supreme_chess.kicad_pro`: KiCad 10 project definition.
  - `hardware/supreme_chess.kicad_sch`: Validated main system schematic.
  - `docs/ELECTRICAL.md`: Circuit theory, decoupling specifications, and complete GPIO mapping table.
  - `assets/hour05_schematic.svg`: High-resolution visual schematic diagram.

## Work Package Deliverables
- [KiCad Schematic Source File](../hardware/supreme_chess.kicad_sch)
- [Electrical Specification Document](../docs/ELECTRICAL.md)
- [Electrical Schematic Diagram](../assets/hour05_schematic.svg)

![Hour 05 Electrical Schematic](../assets/hour05_schematic.svg)
