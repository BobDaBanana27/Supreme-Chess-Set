# Chunk 16 — Power Management & USB-C LiPo Charging Logic

## Overview & Work Completed
- **Power Architecture Engineering:** Modeled and implemented power state management (`firmware/include/power_mgr.h`, `firmware/src/power_mgr.cpp`, and `docs/POWER.md`).
- **Battery Fuel Gauge:** Programmed 12-bit ADC voltage sampling on GP26 with 16-sample rolling noise averaging and a non-linear LiPo open-circuit voltage look-up curve.
- **Dynamic Energy Conservation:** Designed a 3-tier inactivity state machine:
  1. *Active Play (23.5 mA):* 133 MHz dual-core MCU, 50 ms scan loop, full OLED brightness (21.3 hours runtime).
  2. *Dimmed Standby (4.8 mA):* 10% OLED brightness after 5 minutes of inactivity (104 hours runtime).
  3. *Deep Dormant Sleep (35 µA):* Crystal oscillator stopped, OLED powered off (`0xAE`), sensors duty-cycled after 10 minutes of inactivity (> 1.5 years standby).
- **Deliverables Produced:**
  - `firmware/include/power_mgr.h`: Power states, thresholds, and battery lookup tables.
  - `firmware/src/power_mgr.cpp`: Voltage sampling, inactivity tracking, and sleep dispatch.
  - `docs/POWER.md`: Full current audit, discharge curves, and TP4056 USB-C charging specifications.
  - `assets/hour16_power_states.svg`: State transition diagram and energy budget breakdown.

## Work Package Deliverables
- [Power Manager Header](../firmware/include/power_mgr.h)
- [Power Manager Source](../firmware/src/power_mgr.cpp)
- [Power Analysis Document](../docs/POWER.md)
- [Power State Machine Diagram](../assets/hour16_power_states.svg)

![Hour 16 Power State Machine](../assets/hour16_power_states.svg)
