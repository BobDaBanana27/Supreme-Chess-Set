# Supreme Chess Set — Smart Capture Tray & Sensor Sockets CAD

## 1. Overview & Operational Concept
The smart capture tray is the physical-to-digital interface of the Supreme Chess scoring engine. Rather than relying on unreliable computer vision or battery-hungry optical sensors, the system relies on **positionally deterministic capture slots**:
- Each player has a dedicated slide-out capture tray for their color army (one for White, one for Black).
- The tray contains 16 designated molded pockets arranged in a perfectly balanced **8-column $\times$ 2-row matrix** on an exact **18.0 mm pitch** (directly matching the 18.0 mm grid pitch of the chessboard squares):
  - **Rear Array (Row 2, $y = 58.0\text{ mm}$):** 8× Major & Royal sockets organized left-to-right by hierarchy and diameter:
    - Col 0 ($x = 15.0\text{ mm}$): King ($\varnothing 15.5\text{ mm}$, largest hole, labeled **♔ KING / 0 pts** for checkmate/resignation detection and travel stowage)
    - Col 1 ($x = 33.0\text{ mm}$): Queen ($\varnothing 15.5\text{ mm}$, largest hole, labeled **♛ QUEEN / +9 pts**)
    - Col 2 ($x = 51.0\text{ mm}$): Rook 1 ($\varnothing 14.0\text{ mm}$, labeled **♜ ROOK / +5 pts**)
    - Col 3 ($x = 69.0\text{ mm}$): Rook 2 ($\varnothing 14.0\text{ mm}$, labeled **♜ ROOK / +5 pts**)
    - Col 4 ($x = 87.0\text{ mm}$): Knight 1 ($\varnothing 14.0\text{ mm}$, labeled **♞ KNIGHT / +3 pts**)
    - Col 5 ($x = 105.0\text{ mm}$): Knight 2 ($\varnothing 14.0\text{ mm}$, labeled **♞ KNIGHT / +3 pts**)
    - Col 6 ($x = 123.0\text{ mm}$): Bishop 1 ($\varnothing 14.0\text{ mm}$, labeled **♝ BISHOP / +3 pts**)
    - Col 7 ($x = 141.0\text{ mm}$): Bishop 2 ($\varnothing 14.0\text{ mm}$, labeled **♝ BISHOP / +3 pts**)
  - **Front Array (Row 1, $y = 22.0\text{ mm}$):** 8× Pawn sockets, column-for-column aligned with Row 2:
    - Cols 0–7 ($x = [15.0, 33.0, 51.0, 69.0, 87.0, 105.0, 123.0, 141.0]\text{ mm}$): 8× Pawns ($\varnothing 13.0\text{ mm} \times 4.8\text{ mm}$ deep, smallest holes, labeled **♟ PAWN / +1 pt** each).
- **Even Centering & Margins:** Total tray length is $156.0\text{ mm}$. With 8 columns across a span of $7 \times 18.0\text{ mm} = 126.0\text{ mm}$, the left and right margins are both exactly $(156.0 - 126.0) / 2 = 15.0\text{ mm}$.
- **Hole Size Hierarchy:**
  - King & Queen: $\varnothing 15.5\text{ mm}$ (largest holes)
  - Rooks, Knights, Bishops: $\varnothing 14.0\text{ mm}$ (medium holes)
  - Pawns: $\varnothing 13.0\text{ mm}$ (smallest holes)
- Under each socket, the bottom floor is thinned to a 0.8 mm membrane. Directly beneath this membrane sits the sensor carrier PCB (`hardware/sensor_strip.kicad_pcb`).
- When a captured piece is dropped into its designated socket, its embedded base magnet pulls the Hall-effect sensor LOW, instantly tallying points in firmware. When a King is cradled, the display registers checkmate/resignation while adding 0 points.

---

## 2. Retention & Mechanical Tolerances
- **Slide Fit:** The tray incorporates dual $1.2\text{ mm} \times 1.5\text{ mm}$ guide ribs that ride inside the base chassis track with $0.35\text{ mm}$ total running clearance.
- **Detent Lock:** A miniature flexible friction detent at the rear of the tray holds the drawer firmly in both fully extended (during play) and fully closed (during transport) positions.
- **Embossed Labels:** High-contrast engraved glyphs (♛, ♚, ♜, ♝, ♞, ♟) and point values (+9, 0, +5, +3, +1) are embossed into the tray deck adjacent to each socket for unambiguous player placement.
