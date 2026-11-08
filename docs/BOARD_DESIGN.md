# Supreme Chess Set — Magnetic Board Grid Inlay Design

## 1. Grid Architecture & Inlay Fit
The chess playing surface is split into two symmetrical 4×8 tile halves (160.0 mm × 80.0 mm × 3.5 mm). When the folding chassis opens, the two halves form a continuous 160.0 mm × 160.0 mm tournament travel square grid.
- **Square Pitch:** 18.0 mm × 18.0 mm.
- **Tactile Tile Boundaries:** 0.5 mm wide × 0.4 mm deep V-grooves delineate each square, preventing piece drift during turbulent commutes.
- **Perimeter Lip:** 4.0 mm border for flush snapping into the base chassis frame.

---

## 2. Magnet Cavities & Polarity Standard
Underneath every square, an inverted blind pocket ($\varnothing 5.20\text{ mm} \times 2.20\text{ mm}$) houses a 5×2 mm N35 Neodymium magnet.
- **Top Skin Thickness:** 1.30 mm of solid printed polymer seals the top of the magnet pocket. This provides an elegant, smooth playing surface while ensuring maximum magnetic flux penetration ($B \approx 1,150\text{ Gauss}$ at board surface).
- **Polarity Convention:**
  - **Board Squares:** All 64 magnets are installed with **NORTH POLE FACING UP**.
  - **Chess Pieces:** All 32 chess pieces are assembled with **SOUTH POLE FACING DOWN**.
  - **Self-Centering Action:** This strictly enforced polarity rule creates an automatic self-centering magnetic snap when a piece lands within $\pm 3\text{ mm}$ of square center, while guaranteeing uniform attractive force across all 64 squares.

---

## 3. Dual-Color Fabrication Techniques
To achieve contrasting dark and light squares without requiring multi-filament AMS/MMU systems:
1. **Option A (Single Nozzle Manual M600 Filament Change):** The dark squares are embossed with a 0.6 mm surface relief. The slicer is configured to pause (`M600`) at $Z = 2.90\text{ mm}$ to switch from white/cream PLA to dark walnut/black PLA.
2. **Option B (Tile Inlay Press-Fit):** Separate light and dark 17.8 mm tile caps snap directly over the magnet recesses.
