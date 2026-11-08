#include <Arduino.h>
#include "sensor_matrix.h"
#include "chess_engine.h"
#include "display_ui.h"
#include "power_mgr.h"

static SensorMatrix_t     sensor_matrix;
static ChessScoreEngine_t chess_engine;
static DisplayUI_t        display_ui;
static PowerMgr_t         power_mgr;

static uint32_t last_scan_time = 0;

#define PIN_BTN_MODE   2
#define PIN_BTN_RESET  3

void setup() {
    Serial.begin(115200);

    SensorMatrix_Init(&sensor_matrix);
    ChessEngine_Init(&chess_engine);
    DisplayUI_Init(&display_ui);
    PowerMgr_Init(&power_mgr);

    pinMode(PIN_BTN_MODE, INPUT_PULLUP);
    pinMode(PIN_BTN_RESET, INPUT_PULLUP);

    last_scan_time = millis();
}

void loop() {
    uint32_t now = millis();

    // 1. Periodically update battery voltage & check sleep timeout
    PowerMgr_Update(&power_mgr, now);
    DisplayUI_SetBattery(&display_ui, power_mgr.millivolts);

    // 2. Scan Capture Sensor Matrix every 50ms
    if (now - last_scan_time >= 50) {
        last_scan_time = now;
        bool changed = SensorMatrix_Scan(&sensor_matrix);

        if (changed) {
            PowerMgr_ReportActivity(&power_mgr, now);
            uint32_t w_bits = SensorMatrix_GetWhiteBitfield(&sensor_matrix);
            uint32_t b_bits = SensorMatrix_GetBlackBitfield(&sensor_matrix);
            ChessEngine_UpdateFromBitfields(&chess_engine, w_bits, b_bits);
            DisplayUI_Render(&display_ui, &chess_engine);
        }
    }

    // 3. Handle Navigation Buttons
    static bool btn_mode_last = HIGH;
    bool btn_mode_now = digitalRead(PIN_BTN_MODE);
    if (btn_mode_last == HIGH && btn_mode_now == LOW) {
        PowerMgr_ReportActivity(&power_mgr, now);
        DisplayUI_NextMode(&display_ui);
        DisplayUI_Render(&display_ui, &chess_engine);
        delay(150);
    }
    btn_mode_last = btn_mode_now;

    static bool btn_reset_last = HIGH;
    bool btn_reset_now = digitalRead(PIN_BTN_RESET);
    if (btn_reset_last == HIGH && btn_reset_now == LOW) {
        PowerMgr_ReportActivity(&power_mgr, now);
        ChessEngine_Reset(&chess_engine);
        DisplayUI_Render(&display_ui, &chess_engine);
        delay(150);
    }
    btn_reset_last = btn_reset_now;
}
