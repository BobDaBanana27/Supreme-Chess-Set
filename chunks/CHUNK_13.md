# Chunk 13 — Firmware Core (Hardware Abstraction & Sensor Driver)

## Overview & Work Completed
- **Driver Development:** Implemented the high-speed shift register abstraction layer (`firmware/include/sensor_matrix.h` and `firmware/src/sensor_matrix.cpp`).
- **Parallel Load & Bit-Bang Timing:** Programmed the 2 µs parallel load strobe (`/PL` pin GP10) to simultaneously latch all 30 Hall sensor lines, followed by a 32-cycle 1 MHz bit-bang shift clock readout loop executing in just 32 µs.
- **Inversion & 3-Sample Temporal Debouncer:** Handled the active-LOW output characteristics of the Hall sensors with bitwise inversion, routing samples through a 3-entry temporal ring buffer (`history[0] & history[1] & history[2]`). This eliminates false transitions caused by finger hover or vibration.
- **Deliverables Produced:**
  - `firmware/include/sensor_matrix.h`: C/C++ driver header with bitfield masks and structs.
  - `firmware/src/sensor_matrix.cpp`: High-speed shift register scanning and debouncing implementation.
  - `assets/hour13_firmware_driver.svg`: Firmware timing and filtering architecture flowchart.

## Work Package Deliverables
- [Sensor Matrix Header](../firmware/include/sensor_matrix.h)
- [Sensor Matrix Source](../firmware/src/sensor_matrix.cpp)
- [Driver Architecture Flowchart](../assets/hour13_firmware_driver.svg)

![Hour 13 Driver Flowchart](../assets/hour13_firmware_driver.svg)
