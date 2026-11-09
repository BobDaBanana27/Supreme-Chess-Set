# Chunk 14 — Firmware Scoring Engine & Chess Point Rules

## Overview & Work Completed
- **Rules & Valuations Engine:** Built the core point evaluation engine (`firmware/include/chess_engine.h` and `firmware/src/chess_engine.cpp`) implementing official FIDE piece values: Pawn = 1, Knight = 3, Bishop = 3, Rook = 5, Queen = 9.
- **Bitfield Deconstruction:** Created bitfield isolation algorithms extracting piece counts across each 15-bit capture tray reading (Pawns: bits 0–7, Knights: bits 8–9, Bishops: bits 10–11, Rooks: bits 12–13, Queen: bit 14).
- **Material Balance & Lead Calculation:** Programmed net delta arithmetic ($\Delta = \text{Score}_{\text{White}} - \text{Score}_{\text{Black}}$) to classify lead states (`LEAD_WHITE`, `LEAD_BLACK`, `LEAD_EQUAL`) and feed the graphical OLED balance bar.
- **Deliverables Produced:**
  - `firmware/include/chess_engine.h`: Structs and definitions for player tallies and lead states.
  - `firmware/src/chess_engine.cpp`: Real-time piece counting, point multiplication, and delta logic.
  - `assets/hour14_scoring_engine.svg`: Scoring engine architecture and material advantage diagram.

## Work Package Deliverables
- [Scoring Engine Header](../firmware/include/chess_engine.h)
- [Scoring Engine Source](../firmware/src/chess_engine.cpp)
- [Scoring Engine Flow & Math Diagram](../assets/hour14_scoring_engine.svg)

![Hour 14 Scoring Engine](../assets/hour14_scoring_engine.svg)
