# GenOpt — SC10 Smart Energy Demand and Appliance Scheduling System

## Team
- Team name: GenOpt
- Project code: SC10
- Team size: 3–4 students

## One-sentence problem
Given hourly load, tariff, and appliance limits, predict demand and choose a lower-cost schedule.

## Product goal
Build an app for a home, lab, or small building that predicts electricity demand and chooses good times to run appliances so that cost and peak load are reduced.

## M1 / M2 plan
- M1: Build an ANN forecast or GA scheduler MVP and compare it with an original non-optimized schedule.
- M2: Combine ANN forecasting with GA scheduling, test tariffs and preferences, and deploy the app.

## Step 1
Step 1 prepares the problem, fields, starter data, baseline, test cases, validation, Product V1 sketch, and Git evidence before the main soft-computing algorithm.

## Repository structure
```text
docs/
  STEP-1.md
  baseline-pseudocode.md
  product-v1-sketch.png
data/
  README.md
  hourly_load.csv
  appliances.csv
  test_cases.csv
  invalid_case.csv
src/
  validate_data.py
notebooks/
app/
results/step1/
report/
requirements.txt
README.md
```

## Run validation
```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python src/validate_data.py
```

Expected valid result:
`STEP 1 DATA CHECK PASSED`

The invalid fixture is deliberately kept separate and should fail validation.
