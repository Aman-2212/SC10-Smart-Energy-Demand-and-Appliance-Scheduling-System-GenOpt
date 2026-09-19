# Step 1 Project Contract — GenOpt

## Team and responsibilities
## Team and responsibilities

- Member 1: Aman Bhati — Project Lead / Development
- Member 2: Aditya Sharma — Team Member
- Member 3: Srishti — Testing / Documentation

## One-sentence problem
Given hourly load, tariff, and appliance limits, predict demand and choose a lower-cost schedule.

## User of the product
A home, lab, or small-building user planning appliance times and electricity use.

## Inputs and units
See `data/README.md` and the data dictionary in the SC10 Beginner Step 1 Guide.

## Outputs and units
- `forecast_load_kw`
- appliance start slots
- `daily_cost`
- `peak_load_kw`

## Baseline method
Use the appliance start times entered by the user without optimization. For every hour, add the power of all running appliances. Calculate hourly cost as load_kW × tariff_per_kWh. Add hourly costs for daily cost. The largest hourly load is peak load.

## Soft Computing method for M1
An ANN forecast or GA scheduler MVP, compared with an original non-optimized schedule.

## Advanced method for M2
Combine ANN forecasting with GA scheduling, test tariffs and preferences, and deploy the app.

## Dataset/scenario sources
Step 1 uses a small simulated fixture. Final real source URLs, licences, and assumptions must be documented before the later data pipeline.

## Five mandatory test cases
See `data/test_cases.csv`:
1. Flat tariff and normal appliances.
2. High tariff from 18:00 to 22:00.
3. Appliance allowed only 10:00 to 12:00.
4. Two high-power appliances at same time.
5. Duration longer than allowed window.

## Product V1 screen sketch
See `docs/product-v1-sketch.png`.

## Risks and assumptions
- Step 1 data is simulated and must not be presented as real measurements.
- Appliance power ratings and windows are starter assumptions.
- Missing required fields should be rejected.
- Final data sources and licences are still to be documented.

## Step 1 completion evidence
- Repository URL: [paste GitHub URL]
- Validation PASS screenshot: `results/step1/`
- Expected FAIL screenshot: `results/step1/`
- Git history: [paste/record after team commits]
