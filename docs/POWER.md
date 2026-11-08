# Supreme Chess Set — Power Management & Battery Runtime Analysis

## 1. Subsystem Current Consumption Audit

| Operating Mode | MCU State | Display State | Sensors & Logic | Total Draw (3.3V) | Expected Runtime (500mAh) |
|---|---|---|---|:---:|:---:|
| **Active Play (Move in Progress)** | 133MHz dual-core active, 50ms scan | 100% OLED brightness (64px content) | 30 Hall ICs + 4x shift ICs clocked | **23.5 mA** | **21.3 Hours** |
| **Idle Play (Thinking Phase)** | 48MHz underclocked, 100ms scan | 50% OLED brightness dimming | Shift bus clocked at 10 Hz | **12.2 mA** | **41.0 Hours** |
| **Screen Saver / Dimmed (5 min no moves)** | 12MHz sleep tick, 500ms scan | Display dimmed to 10% | Shift bus duty-cycled 2 Hz | **4.8 mA** | **104 Hours** |
| **Deep Dormant Sleep (10 min inactive)** | RP2040 dormant (XOSC stopped) | OLED power-off (`0xAE`) | Shift registers disabled (CE HIGH) | **0.035 mA (35 µA)** | **> 1.5 Years Standby** |

---

## 2. Battery Discharge Curve & SOC Estimation
The system monitors cell voltage through a precision 100 kΩ / 100 kΩ resistor divider connected to RP2040 ADC0 (GPIO 26):

$$V_{\text{cell}} = 2 \times V_{\text{ADC}} = 2 \times \left( \frac{\text{ADC\_RAW}}{4095} \times 3.3\text{ V} \right)$$

### 3.7V LiPo Open-Circuit Voltage Look-Up Table:
- $\ge 4.18\text{ V}$: 100% Full Charge
- $4.00\text{ V}$: 85%
- $3.85\text{ V}$: 60% (Nominal Plateau)
- $3.70\text{ V}$: 35%
- $3.55\text{ V}$: 15% (Low Battery Warning Icon Flashing)
- $\le 3.40\text{ V}$: 5% (Emergency Cutoff — Graceful Save & Deep Sleep)

---

## 3. Charging Circuitry & Safety
- **Module:** TP4056 USB-C Constant-Current / Constant-Voltage (CC/CV) Linear Charger.
- **Charge Current Program Resistor ($R_{prog}$):** $4.7\text{ k}\Omega$ set to $250\text{ mA}$ charge rate ($0.5\text{C}$ safe rate for 500mAh pouch cell).
- **Charge Time:** Approx. 2.2 hours from 0% to 100%.
- **Battery Protection ICs:** Onboard DW01A dual-MOSFET protection cuts off power if cell voltage drops below 2.4V or discharge current exceeds 2.0A.
