#include "display_ui.h"
#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

static Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

void DisplayUI_Init(DisplayUI_t *ui) {
    if (!ui) return;

    ui->current_mode = UI_MODE_SCOREBOARD;
    ui->battery_millivolts = 4100;
    ui->dirty_flag = true;

    Wire.setSDA(4); // RP2040 GPIO 4
    Wire.setSCL(5); // RP2040 GPIO 5
    Wire.begin();

    if (display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
        display.clearDisplay();
        display.setTextSize(1);
        display.setTextColor(SSD1306_WHITE);
        display.setCursor(10, 10);
        display.println(F("SUPREME CHESS"));
        display.setCursor(10, 26);
        display.println(F("Hack Club Edition"));
        display.setCursor(10, 42);
        display.println(F("System Ready..."));
        display.display();
        delay(800);
    }
}

void DisplayUI_SetMode(DisplayUI_t *ui, UIMode_t mode) {
    if (!ui) return;
    ui->current_mode = mode;
    ui->dirty_flag = true;
}

void DisplayUI_NextMode(DisplayUI_t *ui) {
    if (!ui) return;
    ui->current_mode = (UIMode_t)((ui->current_mode + 1) % 3);
    ui->dirty_flag = true;
}

void DisplayUI_SetBattery(DisplayUI_t *ui, uint16_t mv) {
    if (!ui) return;
    ui->battery_millivolts = mv;
}

static void render_scoreboard(const DisplayUI_t *ui, const ChessScoreEngine_t *engine) {
    display.clearDisplay();

    // Top Header: Scores
    display.setTextSize(1);
    display.setCursor(4, 2);
    display.print(F("WHITE: "));
    display.setTextSize(2);
    display.setCursor(46, 0);
    display.print(engine->white.total_points);

    display.setTextSize(1);
    display.setCursor(76, 2);
    display.print(F("BLK: "));
    display.setTextSize(2);
    display.setCursor(104, 0);
    display.print(engine->black.total_points);

    // Separator Line
    display.drawFastHLine(0, 17, SCREEN_WIDTH, SSD1306_WHITE);

    // Middle: Net Lead Status or Game Over Banner
    display.setTextSize(1);
    display.setCursor(10, 22);
    if (engine->status == GAME_BLACK_RESIGNED) {
        display.print(F("BLK RESIGNED! W WINS"));
    } else if (engine->status == GAME_WHITE_RESIGNED) {
        display.print(F("WHT RESIGNED! B WINS"));
    } else if (engine->status == GAME_BOTH_KINGS_STOWED) {
        display.print(F("ALL STOWED (TRAVEL)"));
    } else if (engine->leader == LEAD_WHITE) {
        display.print(F("WHITE ADVANTAGE: +"));
        display.print(engine->net_delta);
    } else if (engine->leader == LEAD_BLACK) {
        display.print(F("BLACK ADVANTAGE: +"));
        display.print(-engine->net_delta);
    } else {
        display.print(F("MATERIAL PARITY (0)"));
    }

    // Dynamic Material Advantage Gauge Bar (X: 14 to 114, Y: 34 to 46)
    display.drawRect(14, 34, 100, 12, SSD1306_WHITE);
    display.drawFastVLine(64, 34, 12, SSD1306_WHITE); // Center zero mark

    int bar_offset = engine->net_delta * 4; // 4 pixels per point of lead
    if (bar_offset > 48) bar_offset = 48;
    if (bar_offset < -48) bar_offset = -48;

    if (bar_offset > 0) {
        // White lead extends right from center
        display.fillRect(65, 36, bar_offset, 8, SSD1306_WHITE);
    } else if (bar_offset < 0) {
        // Black lead extends left from center
        display.fillRect(64 + bar_offset, 36, -bar_offset, 8, SSD1306_WHITE);
    }

    // Bottom Status Bar
    display.setTextSize(1);
    display.setCursor(4, 52);
    display.print(F("W:"));
    if (engine->white.king) display.print(F(" K"));
    if (engine->white.queen) display.print(F(" Q"));
    if (engine->white.rooks) { display.print(F(" R")); display.print(engine->white.rooks); }
    if (engine->white.knights) { display.print(F(" N")); display.print(engine->white.knights); }
    if (engine->white.pawns) { display.print(F(" P")); display.print(engine->white.pawns); }

    display.setCursor(96, 52);
    display.print(ui->battery_millivolts / 1000.0, 1);
    display.print(F("V"));

    display.display();
}

static void render_piece_details(const ChessScoreEngine_t *engine) {
    display.clearDisplay();
    display.setTextSize(1);
    display.setCursor(0, 0);
    display.println(F("CAPTURED PIECE ROSTER"));
    display.drawFastHLine(0, 10, SCREEN_WIDTH, SSD1306_WHITE);

    display.setCursor(0, 14);
    display.printf("White: K:%d Q:%d R:%d", engine->white.king, engine->white.queen, engine->white.rooks);
    display.setCursor(0, 26);
    display.printf("       B:%d N:%d P:%d", engine->white.bishops, engine->white.knights, engine->white.pawns);

    display.setCursor(0, 40);
    display.printf("Black: K:%d Q:%d R:%d", engine->black.king, engine->black.queen, engine->black.rooks);
    display.setCursor(0, 52);
    display.printf("       B:%d N:%d P:%d", engine->black.bishops, engine->black.knights, engine->black.pawns);

    display.display();
}

static void render_battery_stats(const DisplayUI_t *ui, const ChessScoreEngine_t *engine) {
    display.clearDisplay();
    display.setTextSize(1);
    display.setCursor(16, 0);
    display.println(F("HARDWARE DIAGNOSTICS"));
    display.drawFastHLine(0, 10, SCREEN_WIDTH, SSD1306_WHITE);

    uint8_t pct = 0;
    if (ui->battery_millivolts >= 4200) pct = 100;
    else if (ui->battery_millivolts >= 3700) pct = (ui->battery_millivolts - 3700) / 5;
    else pct = 0;

    display.setCursor(0, 14);
    display.printf("Batt: %umV (%u%%)", ui->battery_millivolts, pct);

    uint16_t mins_left = (pct * 131) / 100; // ~21.8 hrs at 100%
    display.setCursor(0, 26);
    display.printf("Est: %uh %02um left", mins_left / 60, mins_left % 60);

    display.setCursor(0, 40);
    display.printf("W-bits: 0x%04X", (uint16_t)(engine->raw_bits & 0xFFFF));
    display.setCursor(0, 52);
    display.printf("B-bits: 0x%04X", (uint16_t)((engine->raw_bits >> 16) & 0xFFFF));

    display.display();
}

void DisplayUI_Render(DisplayUI_t *ui, const ChessScoreEngine_t *engine) {
    if (!ui || !engine) return;

    switch (ui->current_mode) {
        case UI_MODE_SCOREBOARD:
            render_scoreboard(ui, engine);
            break;
        case UI_MODE_DETAIL_PIECES:
            render_piece_details(engine);
            break;
        case UI_MODE_BATTERY_STATS:
            render_battery_stats(ui, engine);
            break;
    }
    ui->dirty_flag = false;
}
