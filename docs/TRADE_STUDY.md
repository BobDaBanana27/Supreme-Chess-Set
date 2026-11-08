# Supreme Chess Set — Engineering Trade Studies & Component Selection

## 1. Capture Sensor Technology Trade Study
The primary innovation of this project is detecting chess captures without expensive camera vision or RFID tags inside every piece. We evaluated five candidate sensing technologies:

| Criteria (Weight) | Digital Hall-Effect (AH49E / A3144) | Reed Switch (Glass Capsule) | Miniature Microswitch | Optical IR Reflective (TCRT5000) | RFID / NFC (MFRC522 per slot) |
|---|---|---|---|---|---|
| **Cost per 30 units (30%)** | **$3.60 ($0.12 ea)** — *Score: 9/10* | $4.50 ($0.15 ea) — *Score: 8/10* | $6.00 ($0.20 ea) — *Score: 6/10* | $7.50 ($0.25 ea) — *Score: 5/10* | >$45.00 — *Score: 1/10* |
| **Mechanical Reliability (25%)** | Solid-state, zero moving parts, infinite cycles — *Score: 10/10* | Glass envelope prone to shock fracture — *Score: 6/10* | Moving contacts wear out over time — *Score: 6/10* | Sensitive to dust/ambient light — *Score: 5/10* | Solid state — *Score: 9/10* |
| **Enclosure Packaging (20%)** | TO-92 or SOT-23 package, <2mm thickness — *Score: 10/10* | Glass body 14mm long, fragile leads — *Score: 6/10* | High tactile force, 6mm height — *Score: 4/10* | Needs optical window / aperture — *Score: 6/10* | Needs 20mm PCB antenna per slot — *Score: 2/10* |
| **Piece Interaction (15%)** | Seamless: utilizes the existing board magnet in piece base — *Score: 10/10* | Uses piece magnet — *Score: 9/10* | Requires physical weight of piece to depress button — *Score: 5/10* | Piece must have specific optical reflectance — *Score: 7/10* | Requires bulky RFID tag in piece — *Score: 3/10* |
| **Power Consumption (10%)** | 3.5 mA active / duty cycled to <100 µA — *Score: 8/10* | 0 mA passive — *Score: 10/10* | 0 mA passive — *Score: 10/10* | 15 mA per LED (high power) — *Score: 4/10* | >30 mA RF transceiver — *Score: 3/10* |
| **Weighted Total** | **9.45 / 10 (Selected)** | **7.40 / 10** | **5.75 / 10** | **5.60 / 10** | **2.95 / 10** |

**Selection Decision:** Digital unipolar Hall-effect sensors (TO-92 / SOT-23) offer the perfect blend of zero moving parts, miniature packaging beneath the 3D-printed capture pockets, and seamless leverage of the neodymium magnets already embedded in the chess piece bases.

---

## 2. Microcontroller Platform Trade Study

| Evaluation Criteria | Waveshare / Seeed RP2040-Zero | ATmega328P (Arduino Pro Mini) | ESP32-C3 SuperMini | STM32F103C8T6 (BluePill) |
|---|---|---|---|---|
| **Price (Single Unit)** | **$4.20** | $3.50 | $4.80 | $4.10 |
| **Form Factor** | **18 mm × 23.5 mm (ultra-compact)** | 33 mm × 18 mm | 22 mm × 18 mm | 53 mm × 22 mm (too long) |
| **Core Architecture** | Dual ARM Cortex-M0+ @ 133MHz | 8-bit AVR @ 16MHz | 32-bit RISC-V @ 160MHz | 32-bit ARM Cortex-M3 @ 72MHz |
| **Flash / SRAM** | 2MB Flash / 264KB SRAM | 32KB Flash / 2KB SRAM | 4MB Flash / 400KB SRAM | 64KB Flash / 20KB SRAM |
| **Native USB-C** | Yes (Built-in UF2 bootloader) | No (Requires external FTDI) | Yes | Mini-USB / Micro-USB |
| **Power Efficiency** | Low power sleep modes supported | Excellent sleep, but slow | Wi-Fi standby draw is higher | Moderate |
| **Recommendation** | **SELECTED: RP2040-Zero** | Viable backup | Overkill RF power draw | Clunky form factor |

**Selection Decision:** The **RP2040-Zero** provides exceptional processing speed, generous 264KB SRAM (for responsive double-buffered OLED graphics and game state logging), a native USB-C port for firmware flashing without an FTDI adapter, and a sub-$4.50 cost profile.

---

## 3. Display Interface Trade Study

| Option | Cost | Resolution | Viewing Angle | Power Draw | Physical Volume |
|---|---|---|---|---|---|
| **0.96" SSD1306 OLED (I2C)** | **$2.20** | **128 × 64 monochrome** | **>160° (OLED self-emissive)** | **~15 mA @ 3.3V** | **27 × 27 × 4 mm** |
| 0.91" SSD1306 OLED (I2C) | $2.00 | 128 × 32 monochrome | >160° | ~10 mA | 38 × 12 × 4 mm |
| 0.56" 4-Digit 7-Segment LED | $1.80 | 4 numerical characters | Moderate | ~30 mA | 40 × 14 × 8 mm |
| 1602 LCD with I2C Backpack | $2.90 | 16 × 2 characters | Poor (<90°) | ~45 mA with backlight | 80 × 36 × 12 mm (huge) |

**Selection Decision:** The **0.96" SSD1306 OLED (128×64)** is chosen. Its crisp monochrome pixels allow displaying not only numerical point tallies, but also custom chess piece glyphs (♛, ♜, ♝, ♞, ♟), a graphical material balance gauge bar, and an optional blitz chess match clock.
