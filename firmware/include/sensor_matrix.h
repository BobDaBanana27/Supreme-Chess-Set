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
//   Bits 0-7: White Pawns 1-8 (1 pt each)
//   Bits 8-9: White Knights 1-2 (3 pts each)
//   Bits 10-11: White Bishops 1-2 (3 pts each)
//   Bits 12-13: White Rooks 1-2 (5 pts each)
//   Bit 14: White Queen (9 pts)
//   Bit 15: White King (0 pts / Checkmate or Resignation trigger & Travel Home)
// Black Tray (16 Bits):
//   Bits 16-23: Black Pawns 1-8 (1 pt each)
//   Bits 24-25: Black Knights 1-2 (3 pts each)
//   Bits 26-27: Black Bishops 1-2 (3 pts each)
//   Bits 28-29: Black Rooks 1-2 (5 pts each)
//   Bit 30: Black Queen (9 pts)
//   Bit 31: Black King (0 pts / Checkmate or Resignation trigger & Travel Home)

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
