# Supreme Chess Set — System Architecture & Topology

## 1. System Overview
The **Supreme Chess Set** integrates physical magnetic game mechanics with an embedded electronic scoring and timing system. The design separates into four primary functional domains:
1. **Physical Mechanical Grid & Pieces:** 64-square folding magnetic chess board with 32 magnetically weighted pieces.
2. **Sensor Capture Trays:** Two 15-slot capture storage drawers (White and Black), each equipped with an underlying Hall-effect sensing PCB strip.
3. **Core Processing & Multiplexing:** An RP2040-Zero microcontroller interfacing with a 4-stage cascaded 74HC165 shift register chain to scan all 30 piece slots over a 4-wire serial bus.
4. **User Interface & Power Management:** A 0.96" SSD1306 OLED display, dual tactical navigation buttons, and a 500mAh LiPo power management subsystem with USB-C recharging.

---

## 2. Bus Architecture & Signal Routing

```
                        +----------------------------+
                        |  RP2040-Zero MCU (133 MHz) |
                        +----------------------------+
                                |             |
            [I2C Bus: GPIO 4/5] |             | [SPI/Shift Bus: GPIO 10,11,12]
                                v             v
                    +----------------+   +-------------------------------+
                    | SSD1306 OLED   |   | 74HC165 Shift Register Chain  |
                    | (128x64 Pixels)|   | (4x Cascaded ICs, 32-Bit PISO)|
                    +----------------+   +-------------------------------+
                                                         |
                                    +--------------------+--------------------+
                                    |                                         |
                                    v                                         v
                         +--------------------+                    +--------------------+
                         | White Capture Tray |                    | Black Capture Tray |
                         | (15 Hall Sensors)  |                    | (15 Hall Sensors)  |
                         +--------------------+                    +--------------------+
```

### 2.1 I2C Display Interface (Fast Mode 400 kHz)
- **SDA:** RP2040 GPIO 4 (Pin 6) with 4.7kΩ pull-up to 3.3V.
- **SCL:** RP2040 GPIO 5 (Pin 7) with 4.7kΩ pull-up to 3.3V.
- **Frame Rate:** 30 Hz double-buffered display updates.

### 2.2 Shift Register Sensor Scanning Bus (PISO Chain)
Instead of consuming 30 individual GPIO pins on the microcontroller, all 30 digital Hall sensors connect directly into parallel input pins (D0–D7) across four cascaded 74HC165 8-bit shift registers:
- **PL (Parallel Load / Latch):** RP2040 GPIO 10 (Active LOW pulse to capture all 30 slot states simultaneously).
- **CP (Clock Pulse):** RP2040 GPIO 11 (Shift clock driven at 1 MHz).
- **Q7 (Serial Data In):** RP2040 GPIO 12 (Bitstream read into MCU SPI/GPIO input).
- **CE (Clock Enable):** RP2040 GPIO 13 (Tied to GND or driven active LOW during readout).

---

## 3. Capture Slot Allocation & Bit Mapping

The 30 capture slots map into a 32-bit integer bitfield (Bits 0–29 used, Bits 30–31 reserved):

| Byte / IC | Bit Index | Tray Side | Piece Sockets | Point Value Each |
|---|---|---|---|---|
| **IC1 (Byte 0)** | Bit 0–7 | White Captures | White Pawns 1 to 8 | 1 pt each |
| **IC2 (Byte 1)** | Bit 8–9 | White Captures | White Knights 1 & 2 | 3 pts each |
| | Bit 10–11 | White Captures | White Bishops 1 & 2 | 3 pts each |
| | Bit 12–13 | White Captures | White Rooks 1 & 2 | 5 pts each |
| | Bit 14 | White Captures | White Queen | 9 pts |
| | Bit 15 | Reserved | Test alignment bit | — |
| **IC3 (Byte 2)** | Bit 16–23 | Black Captures | Black Pawns 1 to 8 | 1 pt each |
| **IC4 (Byte 3)** | Bit 24–25 | Black Captures | Black Knights 1 & 2 | 3 pts each |
| | Bit 26–27 | Black Captures | Black Bishops 1 & 2 | 3 pts each |
| | Bit 28–29 | Black Captures | Black Rooks 1 & 2 | 5 pts each |
| | Bit 30 | Black Captures | Black Queen | 9 pts |
| | Bit 31 | Reserved | Test alignment bit | — |

---

## 4. Software State Machine & Data Flow

```
 [Power On / Boot] --> [Hardware Self-Test & Calibration]
          |
          v
 [Scan Sensor Bitfield (50ms interval)]
          |
          v
 [Debounce Filter: Require 3 consecutive stable samples]
          |
          v
 [State Changed?] ---> No ---> [Idle / Sleep Timer Count]
          |
         Yes
          v
 [Calculate Captured Material: White Pts, Black Pts, Net Lead]
          |
          v
 [Render OLED Display: Material Bar, Point Delta, Piece Badges]
          |
          v
 [Optional: Update Match Clock (Blitz 5+3s Timer)]
```

---

## 5. Power Architecture
- **Battery:** 3.7V 500mAh LiPo cell with integrated DW01A/FS8205 overcharge and overdischarge protection.
- **Charger:** Onboard TP4056 module programmed for 250mA charge rate (safe 0.5C rate).
- **LDO Regulation:** The RP2040-Zero includes an onboard RT9013-3.3V ultra-low-dropout (LDO) regulator delivering up to 500mA at 3.3V with 70dB PSRR.
- **Power Consumption:**
  - Active Scanning + OLED on: 28 mA (~17.8 hours runtime on 500mAh).
  - Standby / Display Dimmed: 6 mA (>80 hours standby).
