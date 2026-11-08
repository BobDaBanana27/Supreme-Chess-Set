# Supreme Chess Set — PCB Layout, Stackup & Manufacturing Specification

## 1. Board Specifications
The hardware consists of two custom printed circuit boards:
1. **Supreme Chess Motherboard (`supreme_chess.kicad_pcb`):** Dimensions: 75.0 mm × 48.0 mm. Hosts the RP2040-Zero MCU, SSD1306 OLED display socket, LiPo power regulation, buttons, and sensor bus output connector.
2. **15-Slot Capture Sensor Strip (`sensor_strip.kicad_pcb`):** Dimensions: 155.0 mm × 22.0 mm. Sits directly under the slide-out capture tray with 15 SOT-23 Hall sensors pitch-matched to the molded piece sockets and two cascaded 74HC165 shift registers.

---

## 2. Layer Stackup (Standard 2-Layer FR-4)

| Layer | Type | Material | Thickness | Description |
|---|---|---|---|---|
| **Top Silkscreen** | Legend | White Ink | ~0.01 mm | Component outlines, pin 1 indicators, piece socket labels |
| **Top Solder Mask** | Mask | Liquid Photo-Imageable (Matte Black) | ~0.01 mm | Solder mask relief, minimum 0.1 mm bridge |
| **Top Copper (F.Cu)** | Signal / Power | 1 oz Cu | 0.035 mm (35 µm) | I2C, SPI/Shift bus, regulated 3.3V power traces |
| **Dielectric Core** | Core | FR-4 Standard Glass Epoxy | 1.51 mm | $T_g \ge 130^\circ\text{C}$, $\epsilon_r \approx 4.5$ |
| **Bottom Copper (B.Cu)** | Ground Plane | 1 oz Cu | 0.035 mm (35 µm) | Solid continuous low-impedance ground plane |
| **Bottom Solder Mask** | Mask | Liquid Photo-Imageable (Matte Black) | ~0.01 mm | Solder mask |
| **Total Board Thickness** | — | — | **1.60 mm** | Standard nominal tolerance $\pm 10\%$ |

---

## 3. Design Rules & Fabrication Constraints (JLCPCB Tier)
- **Minimum Trace Width:** 0.20 mm (8 mil)
- **Minimum Trace Clearance:** 0.20 mm (8 mil)
- **Minimum Annular Ring:** 0.15 mm (6 mil)
- **Minimum Drill Hole Size:** 0.30 mm (vias), 1.0 mm (headers), 2.7 mm (M2.5 mounting screws)
- **Surface Finish:** Lead-Free HASL (Hot Air Solder Leveling) or ENIG (Electroless Nickel Immersion Gold)
- **Silkscreen Minimum Text Height:** 1.0 mm, line thickness 0.15 mm
