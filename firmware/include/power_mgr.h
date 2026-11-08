#pragma once

#include <stdint.h>
#include <stdbool.h>

#ifdef __cplusplus
extern "C" {
#endif

#define PIN_BAT_ADC          26     // GPIO 26 / ADC0
#define ADC_REF_VOLTAGE      3300   // 3.3V in millivolts
#define ADC_RESOLUTION       4095   // 12-bit ADC on RP2040
#define DIVIDER_RATIO        2      // 100k / 100k equal divider

#define BATTERY_FULL_MV      4200   // 4.20V
#define BATTERY_LOW_MV       3500   // 3.50V (Warning trigger)
#define BATTERY_SHUTDOWN_MV  3350   // 3.35V (Deep sleep cut-off)

#define INACTIVITY_DIM_MS    300000 // 5 minutes to dim
#define INACTIVITY_SLEEP_MS  600000 // 10 minutes to deep dormant sleep

typedef enum {
    PWR_ACTIVE = 0,
    PWR_DIMMED,
    PWR_DORMANT_SLEEP
} PowerState_t;

typedef struct {
    uint16_t     millivolts;
    uint8_t      percentage;
    PowerState_t state;
    uint32_t     last_activity_time;
    bool         low_batt_warning;
} PowerMgr_t;

void PowerMgr_Init(PowerMgr_t *pwr);
void PowerMgr_Update(PowerMgr_t *pwr, uint32_t current_time_ms);
void PowerMgr_ReportActivity(PowerMgr_t *pwr, uint32_t current_time_ms);
void PowerMgr_EnterDormantSleep(PowerMgr_t *pwr);

#ifdef __cplusplus
}
#endif
