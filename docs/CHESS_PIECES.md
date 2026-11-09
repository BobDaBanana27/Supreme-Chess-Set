# Supreme Chess Set — Magnetic Piece Set CAD & FDM Printability Specification

## 1. Proportions & Dimensions
The chess pieces adhere strictly to classical Staunton tournament proportions, miniaturized for travel play on an 18.0 mm square grid:

| Piece | Base Diameter | Total Height | Architectural Profile | Bambu A1 / P1S Support-Free Engineering |
|---|:---:|:---:|---|---|
| **Pawn (♟)** | 12.0 mm | 19.5 mm | Stepped plinth, waisted stem, 45° astragal collar, spherical ball head | 45° transition collar under head eliminates horizontal sphere underhang |
| **Rook (♜)** | 13.5 mm | 23.5 mm | Medieval castle tower, masonry belt, 59° flared corbel parapet, hollow well, 4 crenellations | Vertical embrasure slots (0° overhang) + 45° conical interior well floor |
| **Knight (♞)** | 13.5 mm | 25.8 mm | Fully sculpted horse with 4-tier serrated mane crest, dual upright pointed ears, eye sockets, nostrils, tapered snout | Throat and chin maintain $\ge 57^\circ$ slope from horizontal; zero chin sagging or stringing |
| **Bishop (♝)** | 13.5 mm | 28.5 mm | Slender concave stem, double collar rings, teardrop mitre cap, finial ball | 60° upward-angled V-groove cleft (30° from vertical) prints cleanly without drooping |
| **Queen (♛)** | 14.5 mm | 30.5 mm | Royal stepped pedestal, double astragals, flared coronet with 8-point scalloped rim, inner dome & pearl | 50° interior conical floor; 45° radial V-notches produce self-supporting crown petals |
| **King (♚)** | 14.5 mm | 36.5 mm | Imperial multi-tier pedestal, column rings, bell capital, imperial dome, Imperial Orb & Royal Cross Medallion | **Zero cantilevered horizontal crossbars.** Vertical teardrop medallion with embossed heraldic cross prints with continuous layer stacking |

---

## 2. Bambu Lab A1 / P1S Zero-Support Printability Audit

### Why Traditional King Crosses Fail Without Supports:
On high-speed FDM printers (Bambu A1, A1 Mini, P1S, X1C) using a standard 0.4 mm nozzle:
- A traditional miniature cross has horizontal arms that cantilever out in mid-air at the very top of a tall, thin piece ($z = 33\text{ mm}$).
- Because the arms are tiny (span ~6 mm, thickness ~1.2 mm), bed movement (especially on bed-slingers like the A1) combined with short layer times causes the corners of horizontal crossbars to curl upwards, catch on the nozzle, and droop or snap off completely.

### The Solution: Imperial Orb & Royal Cross Medallion:
1. **Continuous Solid Geometry:** The King's dome transitions into an **Imperial Orb** ($\varnothing 4.0\text{ mm}$ sphere), which anchors a vertical **Royal Teardrop Medallion** ($5.5\text{ mm}$ tall × $4.8\text{ mm}$ wide × $1.8\text{ mm}$ thick).
2. **Embossed Heraldic Relief:** The cross motif is embossed as a sharp $0.3\text{ mm}$ raised relief on both front and back faces of the medallion. In FDM printing, vertical wall reliefs print with razor-sharp fidelity and require **0% support**.
3. **Mechanical Durability:** Unlike fragile cantilevered crossbars that snap off when thrown into a travel bag, the solid medallion finial is structurally robust and travel-proof.

---

### Additional Piece Printability Checks:
- **Knight Chin Overhang:** Many 3D-printed knights have horizontal chins ($>50^\circ$ overhang) that sag and leave rough layer artifacts. The Supreme Chess knight has a redesigned throat-and-jaw profile where every segment has an angle of **$\ge 57^\circ$ from the horizontal** ($<33^\circ$ overhang). It prints with clean, smooth perimeters without a single support tree.
- **Bishop Mitre Cleft:** Slits cut completely through a bishop's hat create an acute overhanging ceiling that droops. The mitre cleft is modeled as a **$60^\circ$ self-supporting V-groove** (30° from vertical), giving deep visual contrast with zero drooping.
- **Rook Crenellations:** The 4 embrasure slots are cut vertically ($0^\circ$ overhang), while the interior tower floor is a $45^\circ$ inverted cone, eliminating the need to bridge across the center.
- **Support-Free Base Magnet Cavity:** The bottom magnet recess ($\varnothing 5.20\text{ mm} \times 1.80\text{ mm}$) has a **$45^\circ$ conical ceiling** reaching $z = 2.60\text{ mm}$. Slicers bridge concentric circles cleanly to a center point. Standard 5×2 mm N35 magnets press flush into the cylindrical portion.

---

## 3. Recommended Slicer Profiles (Bambu Studio / OrcaSlicer)

- **Printer Compatibility:** Bambu Lab A1, A1 Mini, P1P, P1S, X1-Carbon, Prusa MK3/MK4, Voron.
- **Supports:** **DISABLED (0% Supports).**
- **Layer Height:** 0.12 mm High Quality (0.16 mm initial layer).
- **Wall Loops:** 3 (provides solid perimeters for crisp details).
- **Top / Bottom Shell Layers:** 5 top, 4 bottom.
- **Infill:** 100% solid infill from $z = 0$ to $5\text{ mm}$ (concentrates magnet mass at the bottom, lowering $CG$ to $4.2\text{ mm}$), 25% gyroid infill above.
- **Printing Speed:** Outer wall 60–80 mm/s; Inner wall 100–120 mm/s.
- **Minimum Layer Time:** 4.0 seconds (ensures tips of ears and finials cool adequately).
- **Filament:** PLA+, Tough PLA, or PETG.
