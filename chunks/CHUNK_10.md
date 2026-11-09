# Chunk 10 — Smart Capture Tray & Molded Piece Slots CAD

## Overview & Work Completed
- **Core Invention CAD:** Parametrically modeled the smart slide-out capture drawer in FreeCAD 1.1 (`cad/capture_tray.FCStd`) and generated the STEP universal CAD file (`cad/capture_tray.step`).
- **Organized 8×2 Socket Matrix:** Designed a balanced 8-column $\times$ 2-row layout on an exact 18.0 mm pitch (matching the chessboard square pitch), centered across the 156.0 mm drawer body with equal 15.0 mm left and right margins ($x = [15, 33, 51, 69, 87, 105, 123, 141]\text{ mm}$):
  - Row 2 (Back Row, $y = 58.0\text{ mm}$): Major & Royal pieces ordered left-to-right by hierarchy and diameter:
    - King: $\varnothing 15.5\text{ mm}$ (Col 0, largest hole, labeled 0 pts / resignation trigger & travel home)
    - Queen: $\varnothing 15.5\text{ mm}$ (Col 1, largest hole, labeled +9 pts)
    - Rooks: $\varnothing 14.0\text{ mm}$ (Cols 2 & 3, labeled +5 pts each)
    - Knights: $\varnothing 14.0\text{ mm}$ (Cols 4 & 5, labeled +3 pts each)
    - Bishops: $\varnothing 14.0\text{ mm}$ (Cols 6 & 7, labeled +3 pts each)
  - Row 1 (Front Row, $y = 22.0\text{ mm}$): 8× Pawn sockets ($\varnothing 13.0\text{ mm} \times 4.8\text{ mm}$ deep, labeled +1 pt each).
- **Hole Size Hierarchy:** Sockets strictly follow piece proportions with 1.0 mm slip clearance: King & Queen ($\varnothing 15.5\text{ mm}$), Rooks, Knights, Bishops ($\varnothing 14.0\text{ mm}$), and Pawns ($\varnothing 13.0\text{ mm}$).
- **Sensor Alignment & Floor Membrane:** Sunk dual underneath PCB pockets ($148\text{ mm} \times 20\text{ mm} \times 2.2\text{ mm}$) centered under Row 1 and Row 2, maintaining a uniform 0.80 mm floor membrane directly above the SOT-23 Hall sensors on `hardware/sensor_strip.kicad_pcb`.
- **Slide & Detent Features:** Integrated dual $1.2\text{ mm} \times 1.5\text{ mm}$ slide guide ribs and an ergonomic front pull tab.
- **Deliverables Produced:**
  - `cad/capture_tray.FCStd`: Fully editable native FreeCAD model.
  - `cad/capture_tray.step`: Universal neutral STEP export.
  - `cad/capture_tray_white.step` & `cad/capture_tray_black.step`: Dedicated player-specific models.
  - `docs/CAPTURE_TRAY_DESIGN.md`: Socket geometry, retention detents, and operational guide.
  - `assets/hour10_cad_capture_tray.svg`: Orthographic drawer plan and cross-sectional assembly drawing.

## Work Package Deliverables
- [FreeCAD Capture Tray Model](../cad/capture_tray.FCStd)
- [STEP Universal Tray File](../cad/capture_tray.step)
- [Capture Tray Design Specification](../docs/CAPTURE_TRAY_DESIGN.md)
- [Capture Tray Engineering Drawing](../assets/hour10_cad_capture_tray.svg)

![Hour 10 Capture Tray Drawing](../assets/hour10_cad_capture_tray.svg)
