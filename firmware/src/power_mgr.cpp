#include "power_mgr.h"
#include <Arduino.h>

void PowerMgr_Init(PowerMgr_t *pwr) {
    if (!pwr) return;

    pwr->millivolts = 4100;
    pwr->percentage = 90;
    pwr->state = PWR_ACTIVE;
    pwr->last_activity_time = millis();
    pwr->low_batt_warning = false;

    analogReadResolution(12);
    pinMode(PIN_BAT_ADC, INPUT);
}

static uint8_t mv_to_percent(uint16_t mv) {
    if (mv >= 4180) return 100;
    if (mv <= 3400) return 0;
    return (uint8_t)(((uint32_t)(mv - 3400) * 100) / (4180 - 3400));
}

void PowerMgr_ReportActivity(PowerMgr_t *pwr, uint32_t current_time_ms) {
    if (!pwr) return;
    pwr->last_activity_time = current_time_ms;
    pwr->state = PWR_ACTIVE;
}

void PowerMgr_Update(PowerMgr_t *pwr, uint32_t current_time_ms) {
    if (!pwr) return;

    // Read 12-bit ADC on GP26 (16-sample average)
    uint32_t raw_sum = 0;
    for (int i = 0; i < 16; i++) {
        raw_sum += analogRead(PIN_BAT_ADC);
    }
    uint32_t raw_avg = raw_sum / 16;

    // Calculate battery millivolts
    uint32_t measured_mv = (raw_avg * ADC_REF_VOLTAGE * DIVIDER_RATIO) / ADC_RESOLUTION;
    pwr->millivolts = (uint16_t)measured_mv;
    pwr->percentage = mv_to_percent(pwr->millivolts);

    if (pwr->millivolts < BATTERY_LOW_MV) {
        pwr->low_batt_warning = true;
    } else {
        pwr->low_batt_warning = false;
    }

    // Critical low battery shutdown
    if (pwr->millivolts <= BATTERY_SHUTDOWN_MV) {
        PowerMgr_EnterDormantSleep(pwr);
        return;
    }

    // Inactivity state machine
    uint32_t inactive_duration = current_time_ms - pwr->last_activity_time;
    if (inactive_duration > INACTIVITY_SLEEP_MS) {
        PowerMgr_EnterDormantSleep(pwr);
    } else if (inactive_duration > INACTIVITY_DIM_MS) {
        pwr->state = PWR_DIMMED;
    } else {
        pwr->state = PWR_ACTIVE;
    }
}

void PowerMgr_EnterDormantSleep(PowerMgr_t *pwr) {
    if (!pwr) return;
    pwr->state = PWR_DORMANT_SLEEP;

    // Turn off OLED display and sensors
    // In Arduino RP2040, sleep_ms or deep sleep can be invoked
    // System wakes up when player presses SW2 or drops piece triggering interrupt
}
