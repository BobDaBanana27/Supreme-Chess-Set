# Supreme Chess Set — Electrical Engineering Specification

## 1. Power Tree Architecture
The system operates from a single-cell 3.7V 500mAh Lithium-Polymer (LiPo) battery.

```
       [USB-C 5V Input]
              |
              v
      +-----------------+
      | TP4056 Charger  | ----> [3.7V 500mAh LiPo Cell]
      | (DW01A Protect) |             |
      +-----------------+             | (VBAT ~3.0V - 4.2V)
              |                       v
              +---------------> [SPDT Power Switch SW1]
                                      |
                                      v
                             [RP2040-Zero 3.3V LDO]
                                      |
                                      v  (VCC = 3.3V System Rail)
              +-----------------------+-----------------------+
              |                       |                       |
              v                       v                       v
     [RP2040 Dual MCU]       [0.96" SSD1306 OLED]    [30x Hall Sensors]
        (12 - 20 mA)              (10 - 15 mA)        + [4x 74HC165 ICs]
                                                          (2.5 mA)
```

- **Nominal Rail:** 3.3V regulated.
- **Maximum System Current Draw:** 37.5 mA (all pixels on, continuous shift scanning).
- **Typical Current Draw:** 22.0 mA.
- **Estimated Operating Time:** $500\text{ mAh} / 22.0\text{ mA} \approx \mathbf{22.7\text{ Hours}}$ of continuous gameplay!

---

## 2. GPIO Pinout Mapping (RP2040-Zero)

| Pin # | MCU GPIO | Function Name | Direction | Connected Peripheral / Net | Electrical Characteristics |
|:---:|:---:|:---:|:---:|:---:|---|
| 1 | GP0 | `TRAY_WHITE_EN` | Output | White Tray Shift Register CE (Clock Enable) | Active LOW, 3.3V CMOS |
| 2 | GP1 | `TRAY_BLACK_EN` | Output | Black Tray Shift Register CE (Clock Enable) | Active LOW, 3.3V CMOS |
| 3 | GP2 | `BTN_MODE` | Input | Mode / Clock Toggle Pushbutton (SW2) | Internal Pull-up (50kΩ), active LOW |
| 4 | GP3 | `BTN_RESET` | Input | New Game / Reset Pushbutton (SW3) | Internal Pull-up (50kΩ), active LOW |
| 6 | GP4 | `I2C0_SDA` | Bidirectional | SSD1306 OLED Display Serial Data | Open-drain, external 4.7kΩ pull-up |
| 7 | GP5 | `I2C0_SCL` | Output | SSD1306 OLED Display Serial Clock | Open-drain, external 4.7kΩ pull-up |
| 12 | GP10 | `SR_LOAD` | Output | 74HC165 Shift Register Parallel Load (PL) | Active LOW strobe pulse (1 µs) |
| 13 | GP11 | `SR_CLK` | Output | 74HC165 Shift Clock (CP) | 1 MHz SPI Master Clock |
| 14 | GP12 | `SR_DATA_IN` | Input | 74HC165 Cascaded Serial Data Out (Q7) | Digital CMOS input |
| 28 | GP26/ADC0 | `VBAT_SENSE` | Analog In | Battery Voltage Sense Divider | 100kΩ / 100kΩ divider (reads 0–2.1V) |

---

## 3. Decoupling & Noise Immunity
- Every 74HC165 shift register IC has a dedicated 0.1 µF (100 nF) X7R 0805 decoupling capacitor located within 3 mm of its VCC pin.
- Each Hall sensor input line features a 10 kΩ pull-up resistor to 3.3V. The open-collector output of the AH49E/A3144 Hall switches drives the shift register inputs directly.
- The I2C lines include 4.7 kΩ pull-up resistors and a 10 µF tantalum filter cap at the OLED power rail to suppress display switching ripple.
