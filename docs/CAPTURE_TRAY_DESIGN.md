# Supreme Chess Set — Smart Capture Tray & Sensor Sockets CAD

## 1. Overview & Operational Concept
The smart capture tray is the physical-to-digital interface of the Supreme Chess scoring engine. Rather than relying on unreliable computer vision or battery-hungry optical sensors, the system relies on **positionally deterministic capture slots**:
- Each capture tray slides out horizontally from the player's side of the board.
- The tray contains 16 designated molded pockets specifically dimensioned to hold captured and stowed chess pieces (enabling full 32-piece set storage for travel):
  - **Front Array (Row 1):** 8× Pawn sockets ($\varnothing 13.0\text{ mm}$, 18 mm center pitch, labeled 1 pt each).
  - **Rear Array (Row 2):** 
    - 1× King socket ($\varnothing 15.5\text{ mm}$, labeled **♔ KING / 0 pts** for resignation detection and travel stowage).
    - 1× Queen socket ($\varnothing 15.5\text{ mm}$, labeled 9 pts).
    - 2× Rook sockets ($\varnothing 14.0\text{ mm}$, labeled 5 pts each).
    - 2× Bishop sockets ($\varnothing 14.0\text{ mm}$, labeled 3 pts each).
    - 2× Knight sockets ($\varnothing 14.0\text{ mm}$, labeled 3 pts each).
- Under each socket, the bottom floor is thinned to a 0.8 mm membrane. Directly beneath this membrane sits the sensor carrier PCB (`hardware/sensor_strip.kicad_pcb`).
- When a captured piece is dropped into its designated socket, its embedded base magnet pulls the Hall-effect sensor LOW, instantly tallying points in firmware. When a King is cradled, the display registers checkmate/resignation while adding 0 points.

---

## 2. Retention & Mechanical Tolerances
- **Slide Fit:** The tray incorporates dual $1.2\text{ mm} \times 1.5\text{ mm}$ guide ribs that ride inside the base chassis track with $0.35\text{ mm}$ total running clearance.
- **Detent Lock:** A miniature flexible friction detent at the rear of the tray holds the drawer firmly in both fully extended (during play) and fully closed (during transport) positions.
- **Embossed Labels:** High-contrast engraved glyphs (♛, ♜, ♝, ♞, ♟) and point values (+9, +5, +3, +1) are embossed into the tray deck adjacent to each socket for unambiguous player placement.
