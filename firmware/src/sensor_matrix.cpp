#include "sensor_matrix.h"
#include <Arduino.h>

void SensorMatrix_Init(SensorMatrix_t *sm) {
    if (!sm) return;

    sm->raw_state = 0;
    sm->debounced_state = 0;
    sm->changed_mask = 0;
    sm->history_index = 0;
    for (int i = 0; i < DEBOUNCE_SAMPLES; i++) {
        sm->history[i] = 0;
    }

    pinMode(PIN_SR_LOAD, OUTPUT);
    pinMode(PIN_SR_CLK, OUTPUT);
    pinMode(PIN_SR_DATA, INPUT);
    pinMode(PIN_TRAY_W_EN, OUTPUT);
    pinMode(PIN_TRAY_B_EN, OUTPUT);

    digitalWrite(PIN_SR_LOAD, HIGH);
    digitalWrite(PIN_SR_CLK, LOW);
    digitalWrite(PIN_TRAY_W_EN, LOW); // Active
    digitalWrite(PIN_TRAY_B_EN, LOW); // Active
}

bool SensorMatrix_Scan(SensorMatrix_t *sm) {
    if (!sm) return false;

    // Step 1: Strobe Parallel Load (/PL) to asynchronously latch all 30 hall inputs
    digitalWrite(PIN_SR_LOAD, LOW);
    delayMicroseconds(2);
    digitalWrite(PIN_SR_LOAD, HIGH);
    delayMicroseconds(1);

    // Step 2: Read out 32 bits from cascaded shift register chain
    uint32_t raw_bits = 0;
    for (int i = 0; i < 32; i++) {
        // Read current serial data bit
        int bit_val = digitalRead(PIN_SR_DATA);
        if (bit_val) {
            raw_bits |= (1UL << (31 - i));
        }

        // Pulse clock HIGH then LOW
        digitalWrite(PIN_SR_CLK, HIGH);
        delayMicroseconds(1);
        digitalWrite(PIN_SR_CLK, LOW);
        delayMicroseconds(1);
    }

    // Step 3: Invert bits because Hall sensors pull LOW (0) when magnet is detected
    uint32_t active_high_pieces = ~raw_bits;
    sm->raw_state = active_high_pieces;

    // Step 4: 3-Sample Temporal Debounce Filter
    sm->history[sm->history_index] = active_high_pieces;
    sm->history_index = (sm->history_index + 1) % DEBOUNCE_SAMPLES;

    uint32_t stable_state = sm->history[0];
    for (int i = 1; i < DEBOUNCE_SAMPLES; i++) {
        stable_state &= sm->history[i];
    }

    // Check if stable state differs from previous debounced state
    if (stable_state != sm->debounced_state) {
        sm->changed_mask = stable_state ^ sm->debounced_state;
        sm->debounced_state = stable_state;
        return true; // Game state change detected
    }

    sm->changed_mask = 0;
    return false; // No change
}

bool SensorMatrix_IsPiecePresent(const SensorMatrix_t *sm, uint8_t slot_index) {
    if (!sm || slot_index >= 32) return false;
    return (sm->debounced_state & (1UL << slot_index)) != 0;
}

uint32_t SensorMatrix_GetWhiteBitfield(const SensorMatrix_t *sm) {
    if (!sm) return 0;
    return sm->debounced_state & 0x7FFF; // Lowest 15 bits
}

uint32_t SensorMatrix_GetBlackBitfield(const SensorMatrix_t *sm) {
    if (!sm) return 0;
    return (sm->debounced_state >> 16) & 0x7FFF; // Upper 15 bits
}
