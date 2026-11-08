#pragma once

#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

// FIDE Standard Piece Valuations
#define VAL_PAWN    1
#define VAL_KNIGHT  3
#define VAL_BISHOP  3
#define VAL_ROOK    5
#define VAL_QUEEN   9
#define VAL_KING    0   // King has 0 material points (Objective piece / Resignation slot)

typedef enum {
    LEAD_EQUAL = 0,
    LEAD_WHITE,
    LEAD_BLACK
} LeadSide_t;

typedef enum {
    GAME_ACTIVE = 0,
    GAME_WHITE_RESIGNED,    // White King placed in capture tray
    GAME_BLACK_RESIGNED,    // Black King placed in capture tray
    GAME_BOTH_KINGS_STOWED  // Both Kings stowed for travel portability
} GameStatus_t;

typedef struct {
    uint8_t pawns;
    uint8_t knights;
    uint8_t bishops;
    uint8_t rooks;
    uint8_t queen;
    uint8_t king;          // King presence in tray (1 = in tray, 0 = on board)
    uint16_t total_points;
} PlayerScore_t;

typedef struct {
    PlayerScore_t white;        // Material captured by White (Black pieces in White tray)
    PlayerScore_t black;        // Material captured by Black (White pieces in Black tray)
    int16_t       net_delta;    // Positive = White lead, Negative = Black lead
    LeadSide_t    leader;
    GameStatus_t  status;       // Live play, resignation / checkmate, or all stowed
    uint32_t      move_count;   // Number of capture events logged
} ChessScoreEngine_t;

void ChessEngine_Init(ChessScoreEngine_t *engine);
void ChessEngine_UpdateFromBitfields(ChessScoreEngine_t *engine, uint32_t white_tray_bits, uint32_t black_tray_bits);
void ChessEngine_Reset(ChessScoreEngine_t *engine);

#ifdef __cplusplus
}
#endif
