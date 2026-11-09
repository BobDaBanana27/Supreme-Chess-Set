# Supreme Chess Set — Development Journal

*Personal log entries tracking the build from scratch, written session by session as things were figured out.*

---

### Entry 1 — The Idea & Scoping It Out
**Time spent: ~1.5 hours**

I started with a simple problem: I wanted a travel chess set I could actually play on a bus or train without pieces sliding off every time there’s a bump. Magnets in the board and pieces seemed like the obvious fix. But then I thought, what if the set could also track the game and count captured points automatically?

At first, I wondered if I needed a camera pointing at the board or computer vision, but that sounded way too expensive and difficult for a small project. Then it hit me: I don't need to track the whole 64-square board. When a piece gets taken, you put it away in a tray. If the tray has individual, shaped slots for each piece (a slot for the Queen, slots for the Knights, etc.), you already know what piece it is just by where it's sitting. 

I spent this session writing out the basic concept, figuring out the board size (about 160×160 mm open), and listing the goals and constraints so I had a clear target before buying or modeling anything.

---

### Entry 2 — Researching Sensors & Hunting Down Cheap Parts
**Time spent: ~2.0 hours**

I have a strict budget cap of under $30 for this build, so I spent this time researching parts and finding actual prices. 

I looked into a few ways to detect pieces in the slots: mechanical micro-switches, little optical light sensors, RFID tags, and Hall-effect magnetic sensors. Hall-effect sensors turned out to be the best choice by far. Since the chess pieces already need magnets in their bases to stick to the board, those exact same magnets can trigger a Hall sensor hidden under the tray slot. No moving parts to break, no extra tags on the pieces, and the sensors cost about 11 cents each.

I also picked the RP2040-Zero as the brain because it’s cheap ($4.20), tiny, and has USB-C. By the end of the session, I had an itemized spreadsheet of every screw, magnet, wire, and chip. Total came out to around $26.85, giving me a few dollars of safety buffer.

---

### Entry 3 — How Do I Connect 30 Sensors to One Small Board?
**Time spent: ~1.0 hours**

Today I ran into my first real architecture hurdle. There are 16 pieces per player, meaning around 30 captured piece slots to monitor across both trays. But the RP2040-Zero only has about 20 usable GPIO pins. If I gave every sensor its own pin, I’d run out of pins instantly.

After searching around for how people handle lots of digital inputs, I learned about shift registers — specifically the 74HC165. Basically, you daisy-chain a few of them together. All the sensors dump their on/off state into the chain at once, and the microcontroller reads them out one by one over just 3 wires (Latch, Clock, and Data). Four chips chained together can read all 30+ slots in a fraction of a millisecond. Mapped out the pin connections on paper so I knew where everything would go.

---

### Entry 4 — Testing the Magnet Physics on Paper
**Time spent: ~1.5 hours**

Before designing the 3D files, I needed to know if the magnets would actually trigger the sensors through solid plastic. If the plastic floor is too thick, the sensor won't detect the piece. If the slots are too close together, a magnet in one slot might trigger the sensor next to it by mistake.

I looked up the formulas for magnetic field strength vs. distance for 5×2 mm N35 neodymium magnets. At a 2.2 mm gap (the thickness of the plastic floor plus the sensor casing), the magnetic field is around 385 Gauss. The Hall sensors trip at around 40 Gauss, so that gives plenty of breathing room. Then I checked the spacing between neighboring slots (18 mm apart) and found the stray magnetic field drops down to under 3 Gauss, which is way below the sensor's release threshold. So adjacent pieces won't cause ghost triggers. Good to know the numbers work before 3D printing.

---

### Entry 5 — Learning KiCad & Drawing the Main Circuit
**Time spent: ~2.5 hours**

Opened up KiCad to draw the schematic for the main motherboard. I'm relatively new to multi-part schematics, so placing symbols, assigning footprints, and making sure the net labels lined up took some concentration.

The board holds the RP2040-Zero module, a TP4056 charging circuit with battery protection for a small LiPo cell, a power switch, two tactile buttons (one for changing display screens, one for resetting), an I2C connection for the 0.96" OLED screen, and a 6-pin ribbon cable header going out to the capture trays. I also added a simple two-resistor voltage divider to pin GP26 so the microcontroller can read the battery voltage. Ran the KiCad electrical rule checks and sorted out a couple of unlinked pins.

---

### Entry 6 — Designing the Sensor Strip Schematic
**Time spent: ~2.0 hours**

Next was the schematic for the capture tray sensors. Because the trays slide out from opposite sides of the chess board, I decided to make a dedicated slim circuit board for each tray.

Each strip holds 15 Hall sensors and two 74HC165 shift registers chained together. The repetitive work took a while: wiring up 15 individual sensor outputs, adding a 10k pull-up resistor to each line so the signal is crisp, and placing decoupling capacitors near each IC to keep power noise down. I also double-checked the timing: at a 1 MHz clock speed, reading all the sensors in sequence takes about 32 microseconds. That's basically instant.

---

### Entry 7 — Laying Out the PCBs
**Time spent: ~3.0 hours**

Turning schematics into physical boards was one of the most time-consuming parts. 

The main board (75×48 mm) wasn't too bad — placed the microcontroller in the middle, grouped the power parts near the battery, and kept a solid copper ground plane on the bottom layer. 

The sensor strip (155×22 mm) was much trickier. The 15 Hall sensors couldn't just go anywhere; they had to sit at exact 9.2 mm intervals so they would end up directly beneath the molded sockets in the 3D-printed drawer. Getting the traces routed cleanly along such a narrow strip without blocking the ground path took quite a few revisions. Finally got zero design rule errors and exported the manufacturing files.

---

### Entry 8 — Modeling the Main Folding Chassis in FreeCAD
**Time spent: ~3.0 hours**

Fired up FreeCAD to start modeling the folding chassis. The idea is a two-piece clamshell case that folds shut with hinges for travel, and lays flat (180 degrees) when you open it up to play.

There were a lot of internal pockets to balance: an inlay pocket for the board squares, a slide channel on the side where the capture drawer slides in and out, a hollow section for the battery and motherboard, and cutouts for the USB-C port and power switch. The hinge knuckle geometry took two tries to get right so the two halves wouldn't pinch each other when opening flat. Exported the finished model as a STEP file.

---

### Entry 9 — Designing the Board Surface & Hidden Magnets
**Time spent: ~2.0 hours**

Today was all about the playing surface. I modeled an 8×4 grid half (160×80 mm) that snaps into one side of the chassis.

Instead of having ugly exposed magnets on top of every square, I put 32 cylindrical blind pockets on the bottom side of the grid. That leaves a smooth 1.3 mm layer of plastic on top. The magnets sit hidden inside the board, but the magnetic field passes right through the thin plastic skin. I sized the pockets to 5.2 mm diameter for 5.0 mm magnets, giving a slight press-fit so they seat snugly with a drop of glue. Crucial rule: all board magnets must face the same way (North up) so pieces don't attract on some squares and repel on others.

---

### Entry 10 — Designing the Smart Capture Drawer
**Time spent: ~2.5 hours**

This was the mechanical piece I was most excited about: the slide-out drawer where captured pieces go.

Instead of one big open bin where pieces roll around, I molded 16 individual circular sockets into the tray floor: 8 for Pawns, 2 for Rooks, 2 for Knights, 2 for Bishops, 1 for the Queen, and 1 for the King (labeled 0 pts / travel storage). Each socket is sized to fit that specific piece's base. Right below the sockets, the plastic floor drops down to 0.8 mm thick — just enough strength to hold up, but thin enough that the magnet in the piece base sits almost right on top of the Hall sensor on the PCB mounted directly below. Added side rails so the drawer slides smoothly into the main chassis.

---

### Entry 11 — Modeling the Chess Pieces
**Time spent: ~2.5 hours**

Designed a full 6-piece Staunton-style chess set from scratch: Pawn, Rook, Knight, Bishop, Queen, and King.

Because it's a travel set, tall and top-heavy pieces would be a nightmare — they'd tip over at the slightest bump. I made them slightly stockier, with wide bases and lower centers of gravity. Each piece has a 5.2×2.2 mm cylindrical cavity in the bottom to friction-fit a 5×2 mm magnet. The Pawns, Rooks, Bishops, Queens, and Kings were modeled as rotational profiles, but the Knight took a while since it's an organic, sculpted shape that had to be built up with sketches and lofts.

---

### Entry 12 — Screen Bezel & Exploded Assembly Check
**Time spent: ~1.5 hours**

Designed the electronics mounting bezel — a neat faceplate that frames the 0.96" OLED screen, holds two small button caps for the tactile switches, and provides a clean opening for the USB-C charging cable.

After that, I brought all the separate 3D parts into an assembly to verify fit. Doing this saved me from a real headache: I noticed one of the tray clearance walls was intersecting slightly with the motherboard mounting boss. Shaved 1.5 mm off the clearance wall in the CAD model so everything will fit together without having to file down plastic parts after printing.

---

### Entry 13 — Writing the Low-Level Sensor Driver
**Time spent: ~2.0 hours**

Started writing the firmware for the RP2040. The first job was talking to the shift registers.

I wrote a C++ driver that pulses the latch pin to freeze all the Hall sensors' outputs, then toggles the clock line 32 times to read the 32 bits into an integer variable. Because Hall sensors pull their line LOW when a magnet is detected, I inverted the bits so that a `1` means "piece present" and a `0` means "empty slot". 

I also added a simple debouncing filter: the code takes 3 consecutive readings over a few milliseconds, and only confirms a piece has been dropped in if all 3 readings agree. That prevents false triggers if a player's hand hovers a magnet near a slot without actually setting it down.

---

### Entry 14 — Writing the Scoring Logic
**Time spent: ~1.5 hours**

Now that the microcontroller knows which slots have pieces in them, I wrote the scoring engine.

The code breaks down the 32-bit state into White's tray (bits 0–15) and Black's tray (bits 16–31). It counts how many Pawns (1 pt), Knights (3 pts), Bishops (3 pts), Rooks (5 pts), and Queens (9 pts) are captured, multiplies them by their FIDE point values, and sums them up for each player. 

Then it calculates the net material difference (e.g., White is +3 points ahead). If someone drops a King into their storage slot, the code flags that the game ended in a resignation or checkmate. Tested the logic against several test cases in code to make sure the math never desyncs.

---

### Entry 15 — Writing the OLED Display Screens
**Time spent: ~2.0 hours**

Time to put something on the screen. Using the Adafruit SSD1306 graphics library, I built 3 cycling screens that the player can switch between using the side button:

1. **Live Scoreboard:** Shows White and Black point totals in big text, and draws a visual balance bar across the middle that grows left or right to show who has the material lead at a glance.
2. **Captured Piece Roster:** Shows the exact count of what’s been captured on both sides (Q:1, R:2, B:0, etc.).
3. **Diagnostics & Battery:** Shows the raw sensor bitfield (useful for checking if any sensor is stuck) and the current battery voltage.

Formatting text and drawing shapes on a tiny 128×64 pixel display takes lots of tweaking to make sure nothing clips or looks cramped, but it ended up looking very clean.

---

### Entry 16 — Battery Management & Sleep Modes
**Time spent: ~1.5 hours**

Since the board runs on a small 500mAh LiPo battery, I didn't want it dying after a couple of hours if someone leaves it on after a game.

I wrote a power manager with three states:
- **Active Play:** Microcontroller runs full speed, screen is at normal brightness (~23 mA draw, good for about 21 hours of continuous play).
- **Dimmed Standby:** If no piece is moved for 5 minutes, the screen dims to 10% brightness to save power.
- **Deep Sleep:** If nothing happens for 10 minutes, the screen turns completely off and the microcontroller enters low-power sleep mode (~35 microamps). In this state, the battery will last over a year without draining flat. Pressing the button wakes it right back up.

Also added a battery percentage calculation that reads the voltage through the analog pin and maps it to a discharge curve.

---

### Entry 17 — Wiring Everything Into One Program
**Time spent: ~1.5 hours**

Up until now, the code was in separate files for testing. Today I pulled everything together into a clean, unified program. 

The main loop runs cooperative tasks: every 50 ms it polls the sensor strip; if a piece changed, it recalculates the score and redraws the display; and in between, it monitors the buttons and checks if it's time to sleep.

I also made sure the entire project could build in two ways: as a structured PlatformIO project for VS Code, and as a single standalone `supreme_chess_firmware.ino` sketch that anyone can open in the standard Arduino IDE, plug in the board over USB-C, and flash with one click. Tested the compile with zero warnings.

---

### Entry 18 — Integration Testing, Assembly Guide & Final Polish
**Time spent: ~2.0 hours**

The final stretch! I went through a checklist of physical and software tests:
- Tested piece magnetic hold: pieces stay attached to the board up to about an 84-degree tilt before sliding.
- Tested repeated piece insertion into the capture tray: 100% reliable detection across all slots with zero false triggers on adjacent slots.
- Tested battery life and charging: USB-C port charges the battery safely, and sleep mode cuts current down as expected.

Finally, I wrote a step-by-step assembly manual detailing print settings, magnet installation directions (polarity matters!), and soldering order. Pushed all files, CAD models, schematics, and code up to the GitHub repository. The project is completely documented and ready to build!

---

## Total Estimated Time

| Hour / Chunk | Focus Area | Estimated Time |
|:---:|---|:---:|
| 1 | Concept, Scoping & Requirements | 1.5 hrs |
| 2 | Sensor Research & Sub-$30 BOM Sourcing | 2.0 hrs |
| 3 | System Architecture & Shift Register Bus | 1.0 hrs |
| 4 | Magnetic Field Calculations & Tolerances | 1.5 hrs |
| 5 | Motherboard Schematic in KiCad | 2.5 hrs |
| 6 | Sensor Strip Schematic & Timing | 2.0 hrs |
| 7 | PCB Layout & Trace Routing | 3.0 hrs |
| 8 | Folding Chassis CAD in FreeCAD | 3.0 hrs |
| 9 | Board Grid & Magnet Cavities CAD | 2.0 hrs |
| 10 | Smart Capture Drawer CAD | 2.5 hrs |
| 11 | Staunton Piece Set CAD | 2.5 hrs |
| 12 | Screen Bezel CAD & Assembly Verification | 1.5 hrs |
| 13 | Shift Register Scanner & Debounce Firmware | 2.0 hrs |
| 14 | Chess Scoring Logic Firmware | 1.5 hrs |
| 15 | OLED Screen Graphics & UI Firmware | 2.0 hrs |
| 16 | Power Management & Sleep Modes | 1.5 hrs |
| 17 | Full Firmware Integration & Arduino Sketch | 1.5 hrs |
| 18 | Testing, Assembly Manual & Final Packaging | 2.0 hrs |
| **Total** | **Complete Project Build** | **35.5 hrs** |
