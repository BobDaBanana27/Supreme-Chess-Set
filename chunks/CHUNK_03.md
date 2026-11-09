# Chunk 03 — System Architecture & Capture Sensor Topology

## Overview & Work Completed
- **Architecture Design:** Designed the complete system topology interconnecting the RP2040-Zero microcontroller, 4-stage cascaded 74HC165 shift register chain, dual capture trays (30 Hall sensors), and 0.96" SSD1306 OLED display.
- **Pin Efficiency:** Solved the I/O bottleneck by routing all 30 digital Hall sensors through four cascaded 8-bit PISO (Parallel-In Serial-Out) shift registers. This reduces microcontroller I/O demand from 30 pins to just 3 pins (Clock, Latch, Data), leaving remaining pins available for I2C display, tactile navigation buttons, and power monitoring.
- **Bitfield Mapping:** Mapped the 30 sensor locations into a structured 32-bit integer array matching FIDE chess piece point valuations (Pawns=1, Knights/Bishops=3, Rooks=5, Queens=9).
- **Deliverables Produced:**
  - `docs/ARCHITECTURE.md`: Complete bus architecture, signal routing, bitfield mapping, and state machine specification.
  - `assets/hour03_system_architecture.svg`: System architecture diagram illustrating bus topology and power flow.

## Work Package Deliverables
- [System Architecture Document](../docs/ARCHITECTURE.md)
- [System Architecture Diagram](../assets/hour03_system_architecture.svg)

![Hour 03 System Architecture](../assets/hour03_system_architecture.svg)
