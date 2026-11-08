# Supreme Chess Set — Maker Assembly & Build Guide

## 1. Bill of Materials Preparation
Before beginning assembly, verify all components according to [`docs/BOM.md`](BOM.md):
- 1× RP2040-Zero Microcontroller
- 1× 0.96" I2C 128×64 OLED Display (SSD1306)
- 30× AH49E / A3144 Digital Hall-Effect Sensors (SOT-23 or TO-92)
- 4× 74HC165 Shift Registers (SOIC-16)
- 2× Custom Sensor Carrier PCBs (`hardware/sensor_strip.kicad_pcb`)
- 1× Custom Motherboard PCB (`hardware/supreme_chess.kicad_pcb`)
- 96× 5×2 mm N35 Neodymium Disc Magnets
- 1× 3.7V 500mAh 602040 LiPo Battery + TP4056 USB-C Charger Module
- 3D Printed Parts: 2× Base Halves, 2× Board Inlay Halves, 2× Capture Trays, 1× Electronics Bezel, 32× Chess Pieces

---

## 2. Step-by-Step Build Instructions

### Step 1: 3D Printing the Mechanical Enclosure & Pieces
1. Print the base chassis halves (`cad/supreme_chess_base.FCStd`) and capture drawers (`cad/capture_tray.FCStd`) using PLA+ at 0.20 mm layer height with 3 perimeters and 20% gyroid infill.
2. Print the board grid halves (`cad/board_grid_half.FCStd`) using a two-color filament swap at layer height $Z = 2.9\text{ mm}$ for dark vs light squares.
3. Print the chess piece set (`cad/chess_pieces.FCStd`) at 0.12 mm layer height with 100% solid base infill for bottom-heavy stability.

### Step 2: Magnet Installation & Polarity Check (CRITICAL)
> [!IMPORTANT]
> Magnet polarity must be consistent across the entire project!
1. **Board Grid:** Press-fit one 5×2 mm disc magnet into each of the 32 cavities on the bottom of both board grid halves with **NORTH POLE FACING UP** (toward the playing surface). Secure with a drop of cyanoacrylate (superglue) if press-fit is loose.
2. **Chess Pieces:** Press-fit one 5×2 mm disc magnet into the base cavity of each of the 32 pieces with **SOUTH POLE FACING DOWN** (toward the board).
3. Test every piece on a test square: it should cleanly snap to square center without repulsion.

### Step 3: Soldering the Electronics
1. **Sensor Strips:** Solder two 74HC165 shift registers, 15 Hall sensors (H1–H15), and 15 pull-up resistors (10kΩ) onto both `sensor_strip` PCBs. Solder the 6-pin FFC ribbon connector J1.
2. **Motherboard:** Solder the RP2040-Zero castellated module, OLED 4-pin female socket, tactile pushbuttons SW2/SW3, power switch SW1, and TP4056 charger leads to `supreme_chess.kicad_pcb`.
3. Connect the 6-conductor flexible ribbon cables between the motherboard and both sensor strips.

### Step 4: Firmware Flashing
1. Connect the RP2040-Zero to your PC via USB-C while holding the `BOOT` button.
2. Open `firmware/supreme_chess_firmware.ino` in Arduino IDE (or use PlatformIO in `firmware/`).
3. Select board: **Raspberry Pi Pico / RP2040**.
4. Click **Upload**. The OLED screen will initialize with the *Supreme Chess* splash screen!

### Step 5: Final Mechanical Assembly
1. Snap the sensor strips into the bottom recesses of each capture tray.
2. Slide the capture trays into the base chassis guide rails.
3. Snap the magnetic board grid inlays into the top chassis frame.
4. Insert the hinge pivot pin (Ø3.0 mm stainless rod) through the knuckles.
5. Power on, seat captured pieces into their labeled sockets, and watch the OLED count points in real-time!
