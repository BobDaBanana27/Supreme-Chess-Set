# Supreme Chess Set

> **Portable Magnetic Travel Chess Set**  
> Built for **Hack Club Half Life 2** | Repository: [`BobDaBanana27/Supreme-Chess-Set`](https://github.com/BobDaBanana27/Supreme-Chess-Set)  
> Total Bill of Materials: **$13.96 USD** (well within the $30.00 USD program budget)

---

## What is it?

The **Supreme Chess Set** is a compact, 3D-printed magnetic travel chess set designed to be taken anywhere. All 32 pieces have neodymium magnets pressed into their bases, and 64 matching magnets are embedded flush into the board squares beneath a thin plastic skin. This keeps pieces firmly in place during travel — the board can be tilted steeply or tossed in a bag without pieces sliding around.

When not in play, all 32 pieces store inside two slide-out trays built into the sides of the board chassis. The whole set closes into a flat clamshell that fits in a backpack pocket.

**Everything is 3D-printed on a standard FDM printer using PLA+ filament.**

---

## Features

- **Magnetic piece retention** — 5×2 mm N35 neodymium disc magnets in every piece base and board square. Pieces hold at up to ~80° tilt.
- **Slide-out storage trays** — both white and black armies have dedicated molded sockets so pieces snap in securely for travel. No rattling, no losing pieces.
- **Compact clamshell form factor** — 168 × 92 × 30 mm closed. Fits in a jacket pocket.
- **Full Staunton piece set** — all 6 piece types (King, Queen, Rook, Bishop, Knight, Pawn) modeled to standard proportions with a low center of gravity for stability.
- **Sub-$14 total cost** — only magnets, filament, and screws needed.
- **Fully open-source** — all CAD in FreeCAD 1.1 (`.FCStd` + `.step`).

---

## Bill of Materials

| # | Item | Qty | Unit Price | Total | Link |
|:---:|---|:---:|:---:|:---:|---|
| 1 | 5×2 mm N35 Neodymium Disc Magnets (pack of 100) | 96 | $0.035 | $3.36 | [AliExpress 100pcs 5×2mm N35](https://www.aliexpress.us/item/3256805987124930.html) / [Amazon](https://www.amazon.com/dp/B08V8MBRFL) |
| 2 | eSUN PLA+ Filament 1.75mm, 1kg spool (~220g used) | 0.22 kg | $18.00/kg | $3.96 | [Amazon eSUN PLA+ 1.75mm](https://www.amazon.com/dp/B07PGZNM34) |
| 3 | M2 × 8mm Socket Head Screws + Brass Heatsets (pack) | 8 | $0.08 | $0.64 | [AliExpress M2 Brass Heatsets & Screws](https://www.aliexpress.us/item/3256803248729112.html) |
| 4 | CA Super Glue (for magnet setting) | 1 | $6.00 | $6.00 | Any hardware store |
| **—** | **TOTAL** | | | **$13.96** | **Under the $30.00 cap** |

---

## 3D CAD Files

All parts designed in **FreeCAD 1.1** and exported as standard STEP files (importable in Fusion 360, Onshape, SolidWorks, etc.):

| Part | FreeCAD Source | STEP Export | Description |
|---|---|---|---|
| Base Chassis | [`cad/supreme_chess_base.FCStd`](cad/supreme_chess_base.FCStd) | [`cad/supreme_chess_base.step`](cad/supreme_chess_base.step) | Clamshell shell halves with slide-way rails and hinge knuckles |
| Board Grid Inlay | [`cad/board_grid_half.FCStd`](cad/board_grid_half.FCStd) | [`cad/board_grid_half.step`](cad/board_grid_half.step) | 8×8 grid with 32 blind magnet pockets (Ø5.2×2.2 mm) per half |
| Capture Tray | [`cad/capture_tray.FCStd`](cad/capture_tray.FCStd) | [`cad/capture_tray.step`](cad/capture_tray.step) | Slide-out drawer with 16 molded piece sockets (K, Q, R×2, B×2, N×2, P×8) |
| Chess Piece Set | [`cad/chess_pieces.FCStd`](cad/chess_pieces.FCStd) | [`cad/chess_pieces.step`](cad/chess_pieces.step) | All 6 Staunton piece types with magnet recess in base |

---

## Assembly Overview

1. **Print all parts** in PLA+ at 0.2mm layer height, 20% infill for the chassis and 40% for pieces.
2. **Press magnets** — use a dab of CA glue to set one N35 5×2mm magnet flush into each of the 32 board grid pockets, and one into each piece base. Keep polarity consistent across the board (all north-up), and all pieces opposite (south-up) so they attract.
3. **Insert heatsets** — press M2 brass threaded inserts into the hinge and latch points with a soldering iron.
4. **Assemble clamshell** — snap the board grid inlays into each chassis half, slide the capture trays in from the ends.
5. **Play.**

---

## Development Log (18 Hours)

| Hour | Milestone | Work Package |
|:---:|---|:---:|
| 01 | Project scope, requirements & travel constraints | [CHUNK_01.md](chunks/CHUNK_01.md) |
| 02 | Engineering trade study & BOM sourcing | [CHUNK_02.md](chunks/CHUNK_02.md) |
| 03 | System architecture & magnet layout | [CHUNK_03.md](chunks/CHUNK_03.md) |
| 04 | Magnetic coupling physics & spacing tolerances | [CHUNK_04.md](chunks/CHUNK_04.md) |
| 05 | Electrical schematic (KiCad 10) | [CHUNK_05.md](chunks/CHUNK_05.md) |
| 06 | Sensor matrix circuit design | [CHUNK_06.md](chunks/CHUNK_06.md) |
| 07 | PCB layout & routing | [CHUNK_07.md](chunks/CHUNK_07.md) |
| 08 | Base chassis CAD (FreeCAD 1.1) | [CHUNK_08.md](chunks/CHUNK_08.md) |
| 09 | Board grid inlay CAD — 32 magnet pockets | [CHUNK_09.md](chunks/CHUNK_09.md) |
| 10 | Capture tray CAD — 16 piece sockets | [CHUNK_10.md](chunks/CHUNK_10.md) |
| 11 | Full Staunton chess piece set CAD | [CHUNK_11.md](chunks/CHUNK_11.md) |
| 12 | Electronics caddy & OLED bezel CAD | [CHUNK_12.md](chunks/CHUNK_12.md) |
| 13 | Firmware: shift register sensor driver | [CHUNK_13.md](chunks/CHUNK_13.md) |
| 14 | Firmware: FIDE scoring engine | [CHUNK_14.md](chunks/CHUNK_14.md) |
| 15 | Firmware: OLED UI renderer | [CHUNK_15.md](chunks/CHUNK_15.md) |
| 16 | Firmware: power management & sleep | [CHUNK_16.md](chunks/CHUNK_16.md) |
| 17 | Integrated firmware & Arduino sketch | [CHUNK_17.md](chunks/CHUNK_17.md) |
| 18 | Integration testing & production package | [CHUNK_18.md](chunks/CHUNK_18.md) |

Full documentation in [`docs/`](docs/).

---

## License

MIT — free and open for educational and maker use. Built for **Hack Club Half Life 2**.
