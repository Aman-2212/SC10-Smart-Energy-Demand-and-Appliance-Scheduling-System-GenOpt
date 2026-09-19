# Data README — GenOpt SC10

## Scope
Step 1 uses a small starter fixture. The final 10,000+ load records/scheduling scenarios are planned for Step 2.

## Files
- `hourly_load.csv`: 24 one-hour records for a starter day.
- `appliances.csv`: appliance power, duration, allowed start window, and scheduling rule.
- `test_cases.csv`: the five mandatory Step 1 cases.
- `invalid_case.csv`: deliberately invalid/impossible example kept separate from valid data.

## Field meanings and units

| Field | Meaning | Unit/type | Starter rule |
|---|---|---|---|
| hour | Hour of load record | 0–23 | Exactly 24 rows |
| historical_load_kw | Earlier electricity demand | kW | 0 or more |
| temperature_c | Weather input | °C | Simulated Step 1 value |
| tariff_per_kwh | Electricity price | currency/kWh | 0 or more |
| appliance_id | Appliance name/code | text | APP-01, APP-02, ... |
| power_kw | Appliance power | kW | Positive |
| duration_slots | Hours required | whole number | 1–24 |
| earliest_start | Earliest allowed start | hour | 0–23 |
| latest_finish | Latest allowed finish | hour | 0–23; start before finish |
| interruptible | Whether load can be shifted | yes/no | yes/no |
| priority | Scheduling priority | category | low/medium/high |

## Missing values
For Step 1, required fields should not be missing. Invalid/missing values should be rejected by validation rather than silently filled.

## Assumptions
- Step 1 values are a small simulated fixture, not claimed as real-world measurements.
- Appliance ratings and scheduling windows are project assumptions for the starter fixture.
- Final source URLs, licences, and documented assumptions must be added before the later data pipeline.

## Mandatory test cases
1. Flat tariff and normal appliances — baseline schedule should calculate.
2. High tariff from 18:00 to 22:00 — flexible load should move later/earlier.
3. Appliance allowed only 10:00 to 12:00 — window must be respected.
4. Two high-power appliances at same time — peak warning expected.
5. Duration longer than allowed window — impossible schedule must be reported.
