# Chunk 09 — Magnetic Chess Board & Grid Inlay CAD

## Overview & Work Completed
- **3D CAD Modeling:** Created the parametric 4×8 half-board grid insert (160.0 mm × 80.0 mm × 3.5 mm) in FreeCAD 1.1 (`cad/board_grid_half.FCStd`) and generated the editable CAD standard STEP file (`cad/board_grid_half.step`).
- **Blind Magnet Pocket Array:** Modeled 32 inverted blind cylindrical recesses ($\varnothing 5.20\text{ mm} \times 2.20\text{ mm}$) on the bottom face, leaving a continuous 1.30 mm solid top skin. This seals the magnets completely inside the polymer structure while transmitting $\sim 1,150\text{ Gauss}$ to the square surface.
- **Self-Centering Dynamics:** Standardized the polarity rule across the entire set (all board squares installed North-Pole-Up; all pieces South-Pole-Down). This generates an automatic magnetic self-centering snap when a piece is placed within $\pm 3\text{ mm}$ of the square center.
- **Deliverables Produced:**
  - `cad/board_grid_half.FCStd`: Native parametric FreeCAD grid model.
  - `cad/board_grid_half.step`: STEP universal CAD export.
  - `docs/BOARD_DESIGN.md`: Grid tolerances, single-nozzle M600 dual-color printing technique, and retention specs.
  - `assets/hour09_cad_board_grid.svg`: Dimensioned CAD layout showing square matrix and magnet pockets.

## Work Package Deliverables
- [FreeCAD Board Grid Model](../cad/board_grid_half.FCStd)
- [STEP Universal Board File](../cad/board_grid_half.step)
- [Board Grid Design Specification](../docs/BOARD_DESIGN.md)
- [Board Grid Engineering Drawing](../assets/hour09_cad_board_grid.svg)

![Hour 09 Board Grid Drawing](../assets/hour09_cad_board_grid.svg)
