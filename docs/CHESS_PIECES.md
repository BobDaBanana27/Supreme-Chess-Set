# Supreme Chess Set — Magnetic Piece Set CAD & Ergonomics

## 1. Proportions & Travel Dimensions
The chess pieces adhere strictly to classical Staunton proportions, miniaturized for travel play on an 18.0 mm square grid:

| Piece | Base Diameter | Total Height | Head / Top Architectural Profile | Overhang Optimization |
|---|:---:|:---:|---|---|
| **Pawn (♟)** | 12.0 mm | 19.5 mm | Stepped plinth, waisted stem, 45° astragal collar, spherical ball head | 45° transition collar under head eliminates underhang |
| **Rook (♜)** | 13.5 mm | 23.5 mm | Medieval castle tower, masonry belt, 45° corbel cornice, hollow well, 4 crenellations | Vertical embrasure slots + 45° conical well floor |
| **Knight (♞)** | 13.5 mm | 25.5 mm | Sculpted horse head with 4-tier serrated mane, dual ears, nostrils, eye sockets, jaw contour | Steep 55° throat & 50° snout; zero horizontal overhangs |
| **Bishop (♝)** | 13.5 mm | 28.5 mm | Slender concave stem, double collar rings, teardrop mitre cap, finial ball | 45° upward-angled mitre cleft prints support-free |
| **Queen (♛)** | 14.5 mm | 30.5 mm | Royal stepped pedestal, double astragals, flared coronet with 8-point scalloped rim, inner dome & pearl | 45° outward flare with 45° radial V-notches |
| **King (♚)** | 14.5 mm | 34.0 mm | Imperial multi-tier pedestal, column rings, bell capital, imperial dome, heraldic Formée cross | Formée cross arms have 45° upward facets from post |

---

## 2. Zero-Support FDM 3D Printing Geometry
All 6 pieces are designed for **100% support-free FDM 3D printing**. Every contour strictly obeys mechanical overhang rules:
1. **The 45° Rule ($dr \le dz$):** Every upward-expanding taper, collar, cornice, and flare maintains a slope of $\ge 45^\circ$ from the horizontal. No surface droops or requires support structures.
2. **Support-Free Base Magnet Cavity:** The underside features an inverted blind cylindrical bore ($\varnothing 5.20\text{ mm} \times 1.80\text{ mm}$) capped with a **45° conical roof** reaching $z = 2.60\text{ mm}$. The 3D printer bridges each concentric circle progressively to a single point with zero sagging. When a standard 5×2 mm N35 magnet is pressed in, it seats flush against the cylindrical shoulder.
3. **Knight Throat & Chin Geometry:** Traditional horse heads fail without support because the chin hangs horizontally. Here, the jawline slopes back at $53^\circ$ and the throat drops at $82^\circ$, enabling clean layer stacking without support material. The ear separation notch is cut vertically.
4. **Bishop Mitre Cleft:** The traditional vertical slit in a bishop's hat creates an unbridgeable overhang at the top. Here, the cleft is sliced at a **$45^\circ$ upward diagonal angle**, allowing the slicer to step layers continuously across the cut.
5. **Rook Battlements:** The 4 crenellations are created via perpendicular vertical cutouts ($0^\circ$ overhang), while the central well floor slopes upward at $45^\circ$.
6. **King Heraldic Formée Cross:** Standard horizontal crossbars require supports underneath the arms. The King's cross features **45° under-slopes** radiating outward from the vertical post, forming an elegant heraldic cross that prints cleanly from the build plate.

---

## 3. Printing Recommendations
- **Support Material:** **DISABLED (0% Support).**
- **Layer Height:** 0.12 mm (0.16 mm initial layer for bed adhesion).
- **Infill:** 100% solid infill on base discs (height 0 to 5 mm) to concentrate magnet mass at the bottom ($CG = 4.2\text{ mm}$), 25% gyroid on upper stems.
- **Cooling Fan:** 100% after layer 3 to ensure crisp detail on fine features (ears, crown petals, cross).
- **Filament:** eSUN PLA+ or PETG (Ivory White for White army, Galaxy/Matte Black for Black army).
