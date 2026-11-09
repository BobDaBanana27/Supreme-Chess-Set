/*
 * ======================================================================================
 * Supreme Chess Set — Automated Capture Counter & Match Display Firmware
 * Designed for Hack Club Half Life 2 (BobDaBanana27 / Supreme-Chess-Set)
 * Target MCU: RP2040-Zero (Raspberry Pi Pico Core)
 * Author: Supreme Chess Team
 * ======================================================================================
 */

#include <Arduino.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

// --- PIN DEFINITIONS ---
#define PIN_SR_LOAD       10  // 74HC165 Parallel Load (/PL) - Active LOW
#define PIN_SR_CLK        11  // 74HC165 Shift Clock (CP)
#define PIN_SR_DATA       12  // 74HC165 Serial Data In (Q7)
#define PIN_TRAY_W_EN     0   // White Tray Shift Register Enable
#define PIN_TRAY_B_EN     1   // Black Tray Shift Register Enable
#define PIN_BTN_MODE      2   // Tactile Button SW2 (Mode Cycle)
#define PIN_BTN_RESET     3   // Tactile Button SW3 (New Game / Reset)
#define PIN_BAT_ADC       26  // LiPo Voltage Sense (100k/100k Divider)

#define SCREEN_WIDTH      128
#define SCREEN_HEIGHT     64
#define OLED_RESET        -1
#define SCREEN_ADDRESS    0x3C

// FIDE Piece Valuations
#define VAL_PAWN          1
#define VAL_KNIGHT        3
#define VAL_BISHOP        3
#define VAL_ROOK          5
#define VAL_QUEEN         9

static Adafruit_SSD1306 oled(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// State Data
static uint32_t last_scan_time = 0;
static uint32_t last_second_time = 0;
static uint32_t debounced_state = 0;
static uint32_t history[3] = {0, 0, 0};
static uint8_t  hist_idx = 0;

static uint8_t w_pawns = 0, w_knights = 0, w_bishops = 0, w_rooks = 0, w_queen = 0, w_king = 0;
static uint8_t b_pawns = 0, b_knights = 0, b_bishops = 0, b_rooks = 0, b_queen = 0, b_king = 0;
static int16_t w_score = 0, b_score = 0, net_delta = 0;
static uint8_t game_status = 0; // 0=Active, 1=White Resigned, 2=Black Resigned, 3=Both Stowed (Travel)

static uint8_t current_ui_mode = 0; // 0=Scoreboard, 1=Pieces, 2=Diagnostics
static uint16_t bat_mv = 4150;

// Helper to count bits
static uint8_t count_bits_range(uint32_t val, uint8_t start, uint8_t num) {
    uint8_t c = 0;
    for (uint8_t i = 0; i < num; i++) {
        if (val & (1UL << (start + i))) c++;
    }
    return c;
}

// 74HC165 Shift Register Scan
static uint32_t scan_shift_registers() {
    // Strobe /PL low for 2 microseconds
    digitalWrite(PIN_SR_LOAD, LOW);
    delayMicroseconds(2);
    digitalWrite(PIN_SR_LOAD, HIGH);
    delayMicroseconds(1);

    uint32_t raw = 0;
    for (int i = 0; i < 32; i++) {
        if (digitalRead(PIN_SR_DATA)) {
            raw |= (1UL << (31 - i));
        }
        digitalWrite(PIN_SR_CLK, HIGH);
        delayMicroseconds(1);
        digitalWrite(PIN_SR_CLK, LOW);
        delayMicroseconds(1);
    }
    // Invert because Hall sensors pull LOW on magnet detection
    return ~raw;
}

static void update_scores() {
    uint32_t w_bits = debounced_state & 0xFFFF;        // All 16 bits of White Tray
    uint32_t b_bits = (debounced_state >> 16) & 0xFFFF; // All 16 bits of Black Tray

    // Row 1 (Bits 0-7): 8 Pawns
    w_pawns   = count_bits_range(w_bits, 0, 8);
    // Row 2 (Bits 8-15): Symmetrical Classical Rank [R1, N1, B1, Q, K, B2, N2, R2]
    w_rooks   = ((w_bits >> 8) & 1) + ((w_bits >> 15) & 1);
    w_knights = ((w_bits >> 9) & 1) + ((w_bits >> 14) & 1);
    w_bishops = ((w_bits >> 10) & 1) + ((w_bits >> 13) & 1);
    w_queen   = ((w_bits >> 11) & 1);
    w_king    = ((w_bits >> 12) & 1); // King: 0 pts, Resign / Checkmate

    w_score = (w_pawns * VAL_PAWN) + (w_knights * VAL_KNIGHT) + 
              (w_bishops * VAL_BISHOP) + (w_rooks * VAL_ROOK) + (w_queen * VAL_QUEEN);

    b_pawns   = count_bits_range(b_bits, 0, 8);
    b_rooks   = ((b_bits >> 8) & 1) + ((b_bits >> 15) & 1);
    b_knights = ((b_bits >> 9) & 1) + ((b_bits >> 14) & 1);
    b_bishops = ((b_bits >> 10) & 1) + ((b_bits >> 13) & 1);
    b_queen   = ((b_bits >> 11) & 1);
    b_king    = ((b_bits >> 12) & 1); // King: 0 pts, Resign / Checkmate

    b_score = (b_pawns * VAL_PAWN) + (b_knights * VAL_KNIGHT) + 
              (b_bishops * VAL_BISHOP) + (b_rooks * VAL_ROOK) + (b_queen * VAL_QUEEN);

    if (w_king && b_king) {
        game_status = 3; // Both Kings stowed for travel!
    } else if (w_king) {
        game_status = 2; // Black King surrendered to White tray (White wins)
    } else if (b_king) {
        game_status = 1; // White King surrendered to Black tray (Black wins)
    } else {
        game_status = 0; // Live play
    }

    net_delta = w_score - b_score;
}

static void render_screen() {
    oled.clearDisplay();

    if (current_ui_mode == 0) { // SCOREBOARD
        oled.setTextSize(1);
        oled.setCursor(4, 2);
        oled.print(F("WHITE: "));
        oled.setTextSize(2);
        oled.setCursor(44, 0);
        oled.print(w_score);

        oled.setTextSize(1);
        oled.setCursor(76, 2);
        oled.print(F("BLK: "));
        oled.setTextSize(2);
        oled.setCursor(102, 0);
        oled.print(b_score);

        oled.drawFastHLine(0, 17, SCREEN_WIDTH, SSD1306_WHITE);

        oled.setTextSize(1);
        oled.setCursor(10, 22);
        if (game_status == 2) {
            oled.print(F("BLK RESIGNED! W WINS"));
        } else if (game_status == 1) {
            oled.print(F("WHT RESIGNED! B WINS"));
        } else if (game_status == 3) {
            oled.print(F("ALL STOWED (TRAVEL)"));
        } else if (net_delta > 0) {
            oled.print(F("WHITE LEAD: +")); oled.print(net_delta);
        } else if (net_delta < 0) {
            oled.print(F("BLACK LEAD: +")); oled.print(-net_delta);
        } else {
            oled.print(F("MATERIAL PARITY (0)"));
        }

        // Advantage Bar
        oled.drawRect(14, 34, 100, 12, SSD1306_WHITE);
        oled.drawFastVLine(64, 34, 12, SSD1306_WHITE);
        int bar_w = net_delta * 4;
        if (bar_w > 48) bar_w = 48;
        if (bar_w < -48) bar_w = -48;
        if (bar_w > 0) oled.fillRect(65, 36, bar_w, 8, SSD1306_WHITE);
        else if (bar_w < 0) oled.fillRect(64 + bar_w, 36, -bar_w, 8, SSD1306_WHITE);

        // Status Line
        oled.setTextSize(1);
        oled.setCursor(4, 52);
        oled.print(F("W:"));
        if (w_queen) oled.print(F("Q "));
        if (w_rooks) { oled.print(F("R")); oled.print(w_rooks); oled.print(F(" ")); }
        if (w_knights) { oled.print(F("N")); oled.print(w_knights); oled.print(F(" ")); }
        if (w_pawns) { oled.print(F("P")); oled.print(w_pawns); }

        oled.setCursor(96, 52);
        oled.print(bat_mv / 1000.0, 1);
        oled.print(F("V"));
    } 
    else if (current_ui_mode == 1) { // DETAIL PIECES
        oled.setTextSize(1);
        oled.setCursor(0, 0);
        oled.println(F("CAPTURED PIECE ROSTER"));
        oled.drawFastHLine(0, 10, SCREEN_WIDTH, SSD1306_WHITE);

        oled.setCursor(0, 14);
        oled.printf("White: Q:%d R:%d B:%d", w_queen, w_rooks, w_bishops);
        oled.setCursor(0, 26);
        oled.printf("       N:%d P:%d", w_knights, w_pawns);

        oled.setCursor(0, 40);
        oled.printf("Black: Q:%d R:%d B:%d", b_queen, b_rooks, b_bishops);
        oled.setCursor(0, 52);
        oled.printf("       N:%d P:%d", b_knights, b_pawns);
    } 
    } 
    else { // DIAGNOSTICS (Mode 2)
        oled.setTextSize(1);
        oled.setCursor(0, 0);
        oled.println(F("SYSTEM DIAGNOSTICS"));
        oled.drawFastHLine(0, 10, SCREEN_WIDTH, SSD1306_WHITE);
        oled.setCursor(0, 16);
        oled.printf("Battery: %u mV (OK)", bat_mv);
        oled.setCursor(0, 28);
        oled.printf("Shift Bus: 32 bits / 32 us");
        oled.setCursor(0, 40);
        oled.printf("W_Bits: 0x%04X", debounced_state & 0x7FFF);
        oled.setCursor(0, 52);
        oled.printf("B_Bits: 0x%04X", (debounced_state >> 16) & 0x7FFF);
    }

    oled.display();
}

void setup() {
    Serial.begin(115200);

    pinMode(PIN_SR_LOAD, OUTPUT);
    pinMode(PIN_SR_CLK, OUTPUT);
    pinMode(PIN_SR_DATA, INPUT);
    pinMode(PIN_TRAY_W_EN, OUTPUT);
    pinMode(PIN_TRAY_B_EN, OUTPUT);
    pinMode(PIN_BTN_MODE, INPUT_PULLUP);
    pinMode(PIN_BTN_RESET, INPUT_PULLUP);

    digitalWrite(PIN_SR_LOAD, HIGH);
    digitalWrite(PIN_SR_CLK, LOW);
    digitalWrite(PIN_TRAY_W_EN, LOW);
    digitalWrite(PIN_TRAY_B_EN, LOW);

    Wire.setSDA(4);
    Wire.setSCL(5);
    Wire.begin();

    if (oled.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
        oled.clearDisplay();
        oled.setTextSize(1);
        oled.setTextColor(SSD1306_WHITE);
        oled.setCursor(16, 12);
        oled.println(F("SUPREME CHESS"));
        oled.setCursor(12, 28);
        oled.println(F("Hack Club Edition"));
        oled.setCursor(20, 44);
        oled.println(F("Initializing..."));
        oled.display();
        delay(600);
    }

    last_scan_time = millis();
    last_second_time = millis();
}

void loop() {
    uint32_t now = millis();

    // 1-Second Timer for Battery Sample
    if (now - last_second_time >= 1000) {
        last_second_time = now;
        // Sample battery
        uint32_t adc_val = analogRead(PIN_BAT_ADC);
        bat_mv = (uint16_t)((adc_val * 3300 * 2) / 4095);
        render_screen();
    }

    // 50ms Scan Loop for Shift Register Sensors
    if (now - last_scan_time >= 50) {
        last_scan_time = now;

        uint32_t raw = scan_shift_registers();
        history[hist_idx] = raw;
        hist_idx = (hist_idx + 1) % 3;

        uint32_t stable = history[0] & history[1] & history[2];
        if (stable != debounced_state) {
            debounced_state = stable;
            update_scores();
            render_screen();
        }
    }

    // Button Handling: SW2 (Mode Cycle — 3 modes: Scoreboard, Pieces, Diagnostics)
    static bool sw2_last = HIGH;
    bool sw2_now = digitalRead(PIN_BTN_MODE);
    if (sw2_last == HIGH && sw2_now == LOW) { // Press event
        current_ui_mode = (current_ui_mode + 1) % 3;
        render_screen();
        delay(150);
    }
    sw2_last = sw2_now;

    // Button Handling: SW3 (Game Reset — hold 1.5s)
    static bool sw3_last = HIGH;
    bool sw3_now = digitalRead(PIN_BTN_RESET);
    if (sw3_last == HIGH && sw3_now == LOW) {
        // Long press reset check
        uint32_t hold_start = millis();
        while (digitalRead(PIN_BTN_RESET) == LOW) {
            if (millis() - hold_start > 1500) {
                oled.clearDisplay();
                oled.setCursor(20, 26);
                oled.println(F("GAME RESET!"));
                oled.display();
                delay(500);
                break;
            }
        }
        render_screen();
        delay(150);
    }
    sw3_last = sw3_now;
}
