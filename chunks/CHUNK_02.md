# Chunk 02 — System Trade Study & Sub-$30 BOM Engineering

## Overview & Work Completed
- **Engineering Trade Study:** Conducted comprehensive quantitative evaluation of capture-sensing modalities (comparing digital Hall ICs, reed switches, microswitches, optical IR, and RFID). Digital Hall-effect sensors achieved the highest weighted score (9.45/10) due to solid-state zero wear, low cost ($0.11/ea), compact TO-92/SOT-23 packaging, and the key ability to detect the magnets already embedded in the chess piece bases.
- **Microcontroller Selection:** Selected the RP2040-Zero for its native USB-C UF2 flashing, 264KB SRAM (enabling double-buffered display rendering), dual ARM cores, and $4.20 price point.
- **Bill of Materials (BOM) Optimization:** Built a line-by-line itemized BOM strictly fulfilling the Hack Club requirement of remaining under $30.00 USD. Sourced parts total exactly **$26.85 USD**, maintaining an unallocated buffer of **$3.15 USD (10.5%)**. Every item is linked directly to live distributor catalog listings on LCSC, AliExpress, Amazon, and JLCPCB with part numbers.
- **Deliverables Produced:**
  - `docs/TRADE_STUDY.md`: Five-way sensor trade study, MCU benchmark, and display interface comparison.
  - `docs/BOM.md`: Markdown itemized BOM with direct clickable product links and distributor allocations.
  - `docs/BOM.csv`: Machine-readable CSV BOM with URLs and part numbers.
  - `assets/hour02_trade_study_bom.svg`: Visual trade study scorecard and budget distribution diagram.

## Work Package Deliverables
- [Engineering Trade Study](../docs/TRADE_STUDY.md)
- [Itemized Bill of Materials (Markdown)](../docs/BOM.md)
- [Bill of Materials (CSV)](../docs/BOM.csv)
- [Trade Study & BOM Chart](../assets/hour02_trade_study_bom.svg)

![Hour 02 Trade Study & Budget Breakdown](../assets/hour02_trade_study_bom.svg)
