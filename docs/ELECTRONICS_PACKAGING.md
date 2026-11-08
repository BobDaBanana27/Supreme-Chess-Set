# Supreme Chess Set — Electronics Caddy & Packaging Specification

## 1. Overview & Mechanical Enclosure Caddy
The electronics bay occupies the side spine of the master chassis half, shielded by the dedicated 3D-printed snap-fit bezel (`cad/electronics_bezel.FCStd` / `.step`).
- **Bezel Dimensions:** 76.0 mm × 46.0 mm × 8.0 mm.
- **OLED Window:** A precision 26.0 mm × 15.0 mm beveled window aligns with the active viewing area of the 0.96" SSD1306 monochrome OLED screen.
- **Button Interface:** Two $\varnothing 4.5\text{ mm}$ cylindrical bores guide spring-loaded button plungers directly over SMD tactile switches SW2 (Mode / Clock) and SW3 (Reset / New Game).
- **USB-C Interface Port:** A 10.0 mm × 4.0 mm strain-relief port accommodates any standard USB-C cable connector housing without interfering with travel closure.

---

## 2. Battery Retention & Thermal Dissipation
- **LiPo Cell Retention:** The 500mAh 602040 LiPo cell sits inside an insulated bottom cradle padded with 0.5 mm silicone thermal tape.
- **Ventilation & Charge Thermals:** During 250mA charging via the TP4056 module, heat generation is under $350\text{ mW}$. Passive conduction through the bottom chassis maintains battery temperature $< 34^\circ\text{C}$ (well below the $45^\circ\text{C}$ safe charging limit).
- **Wiring Conduits:** Internal $2.5\text{ mm} \times 2.0\text{ mm}$ wire tracks route the flexible 6-conductor FFC jumper cable from the motherboard across to the slide-out capture trays.
