#pragma once

#include <stdint.h>
#include <stdbool.h>
#include "chess_engine.h"

#ifdef __cplusplus
extern "C" {
#endif

#define SCREEN_WIDTH   128
#define SCREEN_HEIGHT  64
#define OLED_RESET     -1
#define SCREEN_ADDRESS 0x3C  // Standard I2C address for SSD1306 0.96"

typedef enum {
    UI_MODE_SCOREBOARD = 0,     // Main screen: Scores, Net Lead, Dynamic Bar
    UI_MODE_DETAIL_PIECES,      // Captured piece roster (K, Q, R, B, N, P counts)
    UI_MODE_BATTERY_STATS       // Battery voltage, runtime estimate, sensor raw
} UIMode_t;

typedef struct {
    UIMode_t current_mode;
    uint16_t battery_millivolts;
    bool     dirty_flag;
} DisplayUI_t;

void DisplayUI_Init(DisplayUI_t *ui);
void DisplayUI_SetMode(DisplayUI_t *ui, UIMode_t mode);
void DisplayUI_NextMode(DisplayUI_t *ui);
void DisplayUI_Render(DisplayUI_t *ui, const ChessScoreEngine_t *engine);
void DisplayUI_SetBattery(DisplayUI_t *ui, uint16_t mv);

#ifdef __cplusplus
}
#endif
