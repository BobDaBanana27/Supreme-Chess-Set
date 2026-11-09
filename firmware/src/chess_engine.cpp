#include "chess_engine.h"

// Helper: Count set bits in an integer bit range
static uint8_t count_bits(uint32_t val, uint8_t start_bit, uint8_t num_bits) {
    uint8_t count = 0;
    for (uint8_t i = 0; i < num_bits; i++) {
        if (val & (1UL << (start_bit + i))) {
            count++;
        }
    }
    return count;
}

void ChessEngine_Init(ChessScoreEngine_t *engine) {
    ChessEngine_Reset(engine);
}

void ChessEngine_Reset(ChessScoreEngine_t *engine) {
    if (!engine) return;

    engine->white.pawns = 0;
    engine->white.knights = 0;
    engine->white.bishops = 0;
    engine->white.rooks = 0;
    engine->white.queen = 0;
    engine->white.king = 0;
    engine->white.total_points = 0;

    engine->black.pawns = 0;
    engine->black.knights = 0;
    engine->black.bishops = 0;
    engine->black.rooks = 0;
    engine->black.queen = 0;
    engine->black.king = 0;
    engine->black.total_points = 0;

    engine->net_delta = 0;
    engine->leader = LEAD_EQUAL;
    engine->status = GAME_ACTIVE;
    engine->move_count = 0;
}

void ChessEngine_UpdateFromBitfields(ChessScoreEngine_t *engine, uint32_t white_tray_bits, uint32_t black_tray_bits) {
    if (!engine) return;

    // --- Tally White Captures (Pieces in White's Capture Tray) ---
    // Bits 0-7: 8 Pawns (Row 1)
    engine->white.pawns = count_bits(white_tray_bits, 0, 8);
    // Row 2 (Bits 8-15) - Organized Hierarchy [King, Queen, R1, R2, N1, N2, B1, B2]:
    // Bit 8: King (0 material points - resignation / checkmate slot)
    engine->white.king = count_bits(white_tray_bits, 8, 1);
    // Bit 9: Queen (9 pts)
    engine->white.queen = count_bits(white_tray_bits, 9, 1);
    // Bits 10-11: 2 Rooks (5 pts each)
    engine->white.rooks = count_bits(white_tray_bits, 10, 2);
    // Bits 12-13: 2 Knights (3 pts each)
    engine->white.knights = count_bits(white_tray_bits, 12, 2);
    // Bits 14-15: 2 Bishops (3 pts each)
    engine->white.bishops = count_bits(white_tray_bits, 14, 2);

    engine->white.total_points = (engine->white.pawns * VAL_PAWN) +
                                 (engine->white.knights * VAL_KNIGHT) +
                                 (engine->white.bishops * VAL_BISHOP) +
                                 (engine->white.rooks * VAL_ROOK) +
                                 (engine->white.queen * VAL_QUEEN) +
                                 (engine->white.king * VAL_KING);

    // --- Tally Black Captures (Pieces in Black's Capture Tray) ---
    // Bits 0-7: 8 Pawns (Row 1)
    engine->black.pawns = count_bits(black_tray_bits, 0, 8);
    // Row 2 (Bits 8-15) - Organized Hierarchy [King, Queen, R1, R2, N1, N2, B1, B2]:
    // Bit 8: King (0 material points)
    engine->black.king = count_bits(black_tray_bits, 8, 1);
    // Bit 9: Queen (9 pts)
    engine->black.queen = count_bits(black_tray_bits, 9, 1);
    // Bits 10-11: 2 Rooks (5 pts each)
    engine->black.rooks = count_bits(black_tray_bits, 10, 2);
    // Bits 12-13: 2 Knights (3 pts each)
    engine->black.knights = count_bits(black_tray_bits, 12, 2);
    // Bits 14-15: 2 Bishops (3 pts each)
    engine->black.bishops = count_bits(black_tray_bits, 14, 2);

    engine->black.total_points = (engine->black.pawns * VAL_PAWN) +
                                 (engine->black.knights * VAL_KNIGHT) +
                                 (engine->black.bishops * VAL_BISHOP) +
                                 (engine->black.rooks * VAL_ROOK) +
                                 (engine->black.queen * VAL_QUEEN) +
                                 (engine->black.king * VAL_KING);

    // Check King Resignation / Travel Stowage Status
    if (engine->white.king && engine->black.king) {
        engine->status = GAME_BOTH_KINGS_STOWED; // All pieces stowed for travel!
    } else if (engine->white.king) {
        engine->status = GAME_BLACK_RESIGNED;    // Black King surrendered to White tray
    } else if (engine->black.king) {
        engine->status = GAME_WHITE_RESIGNED;    // White King surrendered to Black tray
    } else {
        engine->status = GAME_ACTIVE;
    }

    // Calculate Material Balance Delta
    engine->net_delta = (int16_t)engine->white.total_points - (int16_t)engine->black.total_points;

    if (engine->net_delta > 0) {
        engine->leader = LEAD_WHITE;
    } else if (engine->net_delta < 0) {
        engine->leader = LEAD_BLACK;
    } else {
        engine->leader = LEAD_EQUAL;
    }

    engine->move_count++;
}
