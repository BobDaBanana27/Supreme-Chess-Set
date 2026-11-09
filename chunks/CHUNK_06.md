# Chunk 06 — Multiplexed Sensor Matrix & Shift Register Circuitry

## Overview & Work Completed
- **Sub-circuit Engineering:** Designed the complete sensor strip multiplexing architecture (`hardware/sensor_strip.kicad_sch`), packaging 15 miniature Hall sensors and two cascaded 74HC165 8-bit PISO shift registers into a slim 155 mm × 22 mm PCB strip.
- **Timing & Waveform Analysis:** Modeled parallel load pulse timing ($1.0\text{ µs}$ active-LOW strobe) and shift clock train (32 clock pulses at 1.0 MHz). The complete 30-slot capture state is latched and read into the RP2040 in just **32 µs**—leaving 99.94% of MCU cycles free for UI rendering, power management, and ultra-low-power sleep modes.
- **Signal Integrity & Noise Conditioning:** Added dedicated 100nF bypass capacitors adjacent to each IC and 10kΩ pull-up networks on all Hall open-drain outputs to guarantee crisp rise times.
- **Deliverables Produced:**
  - `hardware/sensor_strip.kicad_sch`: Validated KiCad 10 schematic for the 15-slot capture sensor board.
  - `docs/SENSOR_MATRIX.md`: Cascade bus architecture, timing analysis, and open-drain conditioning notes.
  - `assets/hour06_sensor_matrix.svg`: Circuit daisy-chain schematic and digital timing waveform diagram.

## Work Package Deliverables
- [Sensor Strip KiCad Schematic](../hardware/sensor_strip.kicad_sch)
- [Sensor Matrix Design Document](../docs/SENSOR_MATRIX.md)
- [Timing Waveform & Cascade Diagram](../assets/hour06_sensor_matrix.svg)

![Hour 06 Sensor Matrix & Timing](../assets/hour06_sensor_matrix.svg)
