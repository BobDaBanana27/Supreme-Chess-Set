# Supreme Chess Set — Engineering Requirements & Scope Specification

## 1. Project Overview & Vision
The **Supreme Chess Set** is a tournament-regulation miniature magnetic travel chess set engineered for portable, on-the-go play with a built-in automated capture scoring engine. Unlike traditional sets that require manual calculation or complex high-overhead computer vision cameras, the Supreme Chess Set incorporates dedicated, custom-molded capture slots with embedded micro Hall-effect sensors. 

When captured pieces are placed in their home slots within the slide-out capture trays, the embedded microcontroller automatically identifies the captured pieces, tallies the point totals, calculates live material advantages, and renders real-time game status to an integrated 0.96" OLED display.

The complete system is engineered under strict cost constraints to remain **strictly under $30.00 USD total BOM** while meeting Hack Club submission guidelines for editable CAD, open-source PCB, and clean firmware.

---

## 2. Core Functional Requirements (FR)

### FR-01: Magnetic Retention & Portability
- **Board Footprint:** 160 mm × 160 mm playing surface (folded travel dimensions 168 mm × 90 mm × 28 mm).
- **Square Pitch:** 18 mm × 18 mm square grid (8×8 standard chess layout).
- **Magnetic Retention:** N35 Neodymium disc magnets (5 mm dia × 2 mm thk) embedded flush beneath every square and in the base of each chess piece, providing 45–60 gf of retention force. Pieces must remain firmly seated at an 80° tilt and withstand moderate vibration during travel (train, plane, car).
- **Hinge & Latch:** Interlocking clamshell hinge with recessed magnetic catch closures to prevent accidental opening during transit.

### FR-02: Automated Piece Capture Detection
- **Dedicated Capture Trays:** Dual slide-out side drawers (White capture tray and Black capture tray), each featuring 15 molded, labeled piece sockets (8× Pawn, 2× Rook, 2× Knight, 2× Bishop, 1× Queen).
- **Sensor Modality:** Miniature unipolar digital Hall-effect sensors (AH49E / A3144 compatible or surface-mount Hall ICs) mounted directly under each socket base.
- **Trigger Reliability:** Sensor actuation distance calibrated to 2.5 mm ± 0.5 mm to ensure reliable detection of seated pieces while preventing cross-talk from neighboring slots.
- **Latency & Debounce:** Microcontroller reads all 30 piece slots every 50 ms with a software debounce filter (3 consecutive matching readings) to eliminate false transitions during piece insertion or removal.

### FR-03: Real-Time Scoring & Display Engine
- **Point Values (FIDE Standard):**
  - Pawn: 1 point
  - Knight: 3 points
  - Bishop: 3 points
  - Rook: 5 points
  - Queen: 9 points
  - King: Objective piece (tracked on board; optional surrender cradle).
- **Display System:** 0.96-inch 128×64 I2C monochrome OLED display (SSD1306 controller).
- **UI Information Density:**
  - White captured material point tally.
  - Black captured material point tally.
  - Live Material Balance (e.g., `White: +3` or `Black: +2` or `Equal`).
  - Graphical visual material bar indicator.
  - Turn indicator / optional Blitz chess clock timer (5 min + 3 sec delay).

### FR-04: Electrical & Power Subsystem
- **Microcontroller:** RP2040-Zero or Raspberry Pi Pico (Dual ARM Cortex-M0+, 133 MHz, 2MB Flash, USB-C native).
- **I/O Multiplexing:** 2× 74HC165 8-bit parallel-in serial-out shift registers or 74HC4067 multiplexers to read 30 digital sensor lines using only 4 MCU pins (Data, Clock, Latch, Enable).
- **Power Source:** 3.7V 500 mAh LiPo rechargeable battery (602040 form factor) with onboard TP4056 USB-C charging IC and DW01A battery protection circuit.
- **Runtime:** Continuous play runtime > 10 hours on a single charge; low-power standby mode when inactive for > 10 minutes.
- **Budget Target:** Bill of Materials (BOM) strictly under $30.00 USD at single-unit prototype quantities.

---

## 3. Physical & Mechanical Constraints

| Parameter | Specification | Tolerance |
|---|---|---|
| Outer Enclosure Dimensions (Folded) | 168 mm (L) × 92 mm (W) × 30 mm (H) | ± 0.5 mm |
| Playing Board Dimensions (Unfolded) | 168 mm (L) × 184 mm (W) × 15 mm (H) | ± 0.5 mm |
| Chess Square Size | 18 mm × 18 mm | ± 0.2 mm |
| King Height / Base Dia | 32 mm height / 14 mm diameter | ± 0.3 mm |
| Pawn Height / Base Dia | 18 mm height / 12 mm diameter | ± 0.3 mm |
| Magnet Dimensions | 5 mm diameter × 2 mm height (N35) | ± 0.05 mm |
| Total Product Weight | < 320 grams (including battery & pieces) | ± 15 g |

---

## 4. User Stories & Acceptance Criteria

- **US-01: Commute Travel Play**  
  *As a traveling chess enthusiast*, I want a portable magnetic board that folds into a pocketable form factor and holds pieces tightly, so I can play without pieces flying off when traveling on the subway or plane.  
  *Acceptance:* Invert board to 80° with pieces placed; zero pieces dislodge.

- **US-02: Instant Material Tracking**  
  *As an amateur player*, I want to know the material advantage at a glance without having to calculate points in my head, so I can evaluate endgame trades accurately.  
  *Acceptance:* Dropping a captured Queen into slot increases score by 9 within 150 ms and updates display material lead.

- **US-03: Low-Cost Self-Fabrication**  
  *As a Hack Club builder*, I want all parts to cost less than $30 and be 3D printable on standard FDM printers (PLA/PETG) without requiring exotic tools.  
  *Acceptance:* Verified BOM total ≤ $30.00 USD, 3D models exportable to standard `.step` and `.stl`.
