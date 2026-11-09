#pragma once

#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

// Hardware Pin Assignments for RP2040-Zero
#define PIN_SR_LOAD       10  // GPIO 10: 74HC165 Parallel Load (/PL) - Active LOW
#define PIN_SR_CLK        11  // GPIO 11: 74HC165 Shift Clock (CP)
#define PIN_SR_DATA       12  // GPIO 12: 74HC165 Serial Data Input (Q7)
#define PIN_TRAY_W_EN     0   // GPIO 0: White Tray Enable (Active LOW)
#define PIN_TRAY_B_EN     1   // GPIO 1: Black Tray Enable (Active LOW)

#define TOTAL_SLOTS       32  // 16 White slots + 16 Black slots (Full 32-piece set storage)
#define DEBOUNCE_SAMPLES  3   // Number of consecutive matching reads required

// Bitfield definitions (Exact 32-bit mapping for 4x 74HC165 8-bit registers):
// White Tray (16 Bits):
//   Row 1: Bits 0-7: White Pawns 1-8 (1 pt each, pitch 18.0mm, Ø13.0mm)
//   Row 2: Organized Major & Royal Rank (pitch 18.0mm, Left-to-Right):
//     Bit 8:  White King (0 pts / Resignation trigger & Travel Home, Ø15.5mm)
//     Bit 9:  White Queen (9 pts, Ø15.5mm)
//     Bit 10: White Rook 1 (5 pts, Ø14.0mm)
//     Bit 11: White Rook 2 (5 pts, Ø14.0mm)
//     Bit 12: White Knight 1 (3 pts, Ø14.0mm)
//     Bit 13: White Knight 2 (3 pts, Ø14.0mm)
//     Bit 14: White Bishop 1 (3 pts, Ø14.0mm)
//     Bit 15: White Bishop 2 (3 pts, Ø14.0mm)
// Black Tray (16 Bits):
//   Row 1: Bits 16-23: Black Pawns 1-8 (1 pt each, pitch 18.0mm, Ø13.0mm)
//   Row 2: Organized Major & Royal Rank (pitch 18.0mm, Left-to-Right):
//     Bit 24: Black King (0 pts / Resignation trigger & Travel Home, Ø15.5mm)
//     Bit 25: Black Queen (9 pts, Ø15.5mm)
//     Bit 26: Black Rook 1 (5 pts, Ø14.0mm)
//     Bit 27: Black Rook 2 (5 pts, Ø14.0mm)
//     Bit 28: Black Knight 1 (3 pts, Ø14.0mm)
//     Bit 29: Black Knight 2 (3 pts, Ø14.0mm)
//     Bit 30: Black Bishop 1 (3 pts, Ø14.0mm)
//     Bit 31: Black Bishop 2 (3 pts, Ø14.0mm)

typedef struct {
    uint32_t raw_state;        // Current raw un-debounced reading
    uint32_t debounced_state;  // Stable filtered bitfield
    uint32_t changed_mask;     // Bits that changed since last update
    uint8_t  history_index;
    uint32_t history[DEBOUNCE_SAMPLES];
} SensorMatrix_t;

void SensorMatrix_Init(SensorMatrix_t *sm);
bool SensorMatrix_Scan(SensorMatrix_t *sm);
bool SensorMatrix_IsPiecePresent(const SensorMatrix_t *sm, uint8_t slot_index);
uint32_t SensorMatrix_GetWhiteBitfield(const SensorMatrix_t *sm);
uint32_t SensorMatrix_GetBlackBitfield(const SensorMatrix_t *sm);

#ifdef __cplusplus
}
#endif
