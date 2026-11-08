# Supreme Chess Set — Multiplexed Sensor Matrix & Shift Register Circuitry

## 1. Overview
The Supreme Chess Set features 30 discrete piece capture locations (15 per side):
- **White Tray:** 8× Pawns (Slots 0–7), 2× Knights (Slots 8–9), 2× Bishops (Slots 10–11), 2× Rooks (Slots 12–13), 1× Queen (Slot 14).
- **Black Tray:** 8× Pawns (Slots 16–23), 2× Knights (Slots 24–25), 2× Bishops (Slots 26–27), 2× Rooks (Slots 28–29), 1× Queen (Slot 30).

To eliminate routing 30 dedicated wires across the folding hinge mechanism, each tray houses a modular sensing strip PCB containing two cascaded 74HC165 8-bit Parallel-In Serial-Out (PISO) shift registers.

---

## 2. Shift Register Cascading Architecture
Each 74HC165 contains 8 parallel data inputs ($D_0$ through $D_7$), an asynchronous parallel load input ($\overline{PL}$), clock input ($CP$), clock inhibit ($\overline{CE}$), serial data input ($DS$), and complementary serial outputs ($Q_7$ and $\overline{Q_7}$).

```
[From MCU]
  |-- PL (Parallel Load / Latch) ----> All 4x 74HC165 PL pins (in parallel)
  |-- CP (Shift Clock) -------------> All 4x 74HC165 CP pins (in parallel)
  |-- CE (Clock Inhibit) -----------> Tied to GND (permanently enabled)

Cascade Data Path:
  [IC1: W Pawns] Q7 ----> DS [IC2: W Major/Minor] Q7 ----> DS [IC3: B Pawns] Q7 ----> DS [IC4: B Major/Minor] Q7 ----> [MCU GP12]
```

---

## 3. High-Speed Readout Timing & Propagation
The shift register chain is read by the RP2040 using a high-speed bit-bang or SPI peripheral clock at 1 MHz ($T_{clk} = 1.0\text{ µs}$):

1. **Strobe Parallel Load ($\overline{PL}$):** MCU drives GP10 LOW for $1.0\text{ µs}$ (minimum spec is $20\text{ ns}$ at 3.3V). All 30 Hall sensor outputs are asynchronously latched into the internal flip-flops simultaneously.
2. **Read Bit 0:** The level of IC4 bit 7 is immediately available on $Q_7$ (MCU GP12).
3. **Clock Pulse Train (31 pulses):** MCU toggles GP11 HIGH then LOW. On each rising edge, data shifts left by one stage.
4. **Total Readout Duration:** 32 clock cycles × $1.0\text{ µs} = \mathbf{32\text{ µs}}$ total scan time! This consumes only 0.06% of the 50 ms tick interval, leaving 99.94% of CPU cycles free for display rendering and sleep modes.

---

## 4. Hall Sensor Pull-Up & Signal Conditioning
- The AH49E / A3144 Hall-effect sensors feature open-collector NPN outputs.
- When no magnetic field is present (empty slot), the internal NPN is OFF, and the external 10 kΩ pull-up resistor pulls the shift register input to 3.3V (`HIGH` = 1).
- When a magnetic chess piece is placed into the socket (flux $> 40\text{ Gauss}$), the internal NPN conducts, pulling the input to ground (`LOW` = 0).
- Firmware inverts the bitfield (`captured = ~raw_bits`) so that a `1` bit represents a seated, captured piece.
