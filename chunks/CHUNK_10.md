# Chunk 10 — Smart Capture Tray & Molded Piece Slots CAD

## Overview & Work Completed
- **Core Invention CAD:** Parametrically modeled the smart slide-out capture drawer in FreeCAD 1.1 (`cad/capture_tray.FCStd`) and generated the STEP universal CAD file (`cad/capture_tray.step`).
- **Precision 8×2 Symmetrical Matrix:** Designed a perfectly balanced 8-column $\times$ 2-row layout on an exact 18.0 mm pitch (matching the chessboard square pitch), centered across the 156.0 mm drawer body with equal 15.0 mm left and right margins ($x = [15, 33, 51, 69, 87, 105, 123, 141]\text{ mm}$):
  - Row 1 ($y = 22.0\text{ mm}$): 8× Pawn sockets ($\varnothing 13.0\text{ mm} \times 4.8\text{ mm}$ deep).
  - Row 2 ($y = 58.0\text{ mm}$): 8× Classical tournament rank sockets aligned column-by-column with Row 1:
    - Rooks: $\varnothing 14.0\text{ mm}$ (Cols 0 & 7)
    - Knights: $\varnothing 14.0\text{ mm}$ (Cols 1 & 6)
    - Bishops: $\varnothing 14.0\text{ mm}$ (Cols 2 & 5)
    - Queen: $\varnothing 15.5\text{ mm}$ (Col 3)
    - King: $\varnothing 15.5\text{ mm}$ (Col 4, labeled 0 pts / resignation trigger & travel home)
- **White vs Black Symmetrical Geometry:** Because Queen and King share identical 15.5 mm diameters, and Rooks, Knights, and Bishops share 14.0 mm diameters, Row 2 is completely palindromic (`[14, 14, 14, 15.5, 15.5, 14, 14, 14] mm`). Both White and Black capture trays are 100% physically interchangeable and geometrically even.
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
