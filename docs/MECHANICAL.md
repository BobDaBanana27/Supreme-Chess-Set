# Supreme Chess Set — Mechanical Enclosure Architecture

## 1. Design Strategy & Dimensions
The enclosure is engineered as an interlocking two-piece folding clamshell with internal slide-out capture drawers. When folded for travel, the entire assembly measures:
- **Length:** 168.0 mm
- **Width:** 92.0 mm
- **Thickness / Height:** 30.0 mm (15.0 mm per half)
- **Weight:** ~245 grams (with pieces and electronics installed)

When unfolded on a table, the two halves form a seamless **168.0 mm × 184.0 mm** playing arena with an embedded 160.0 mm × 160.0 mm 8×8 square grid (18.0 mm square pitch).

---

## 2. Structural Features
1. **Drawer Slide-Ways:** Integrated 158 mm × 84 mm × 7.5 mm internal channels with dual-lip retention tracks allow both capture drawers to slide smoothly out from the player sides without binding.
2. **Hinge Geometry:** Precision knuckles with a 3.0 mm stainless steel pivot rod (or 3D printed pin) permit a full 180° flat fold with zero center-gap when deployed.
3. **Magnetic Latch Recesses:** Four corner pockets sized at $\varnothing 5.2\text{ mm} \times 2.2\text{ mm}$ house pairs of 5×2 mm N35 magnets to provide positive tactile closure when folded shut.
4. **Electronics Bay:** Recessed cavity in the master chassis half provides secure mounting for the RP2040-Zero MCU, TP4056 USB-C charging module, 500mAh LiPo battery, and side-mounted OLED viewing window.
5. **Printability:** All surfaces feature $\ge 45^\circ$ self-supporting overhangs or bridgeable spans ($< 8\text{ mm}$), allowing clean FDM printing with zero support material required.

---

## 3. Recommended FDM 3D Print Settings

| Parameter | Specification | Notes |
|---|---|---|
| **Material** | PLA+ / PETG | Matte black for chassis, walnut/ivory for board squares |
| **Layer Height** | 0.20 mm | 0.12 mm for chess piece detail |
| **Perimeters / Walls** | 3 (1.2 mm total wall) | Ensures structural rigidity |
| **Top / Bottom Solid Layers** | 4 / 4 | Prevents magnet cavity read-through |
| **Infill Density & Pattern** | 20% Gyroid | Isotropic rigidity, vibration damping |
| **Nozzle Diameter** | 0.40 mm standard | Standard E3D / Bambu style |
