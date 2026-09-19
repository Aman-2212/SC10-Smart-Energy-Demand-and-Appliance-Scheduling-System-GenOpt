import pandas as pd

FILE = "data/invalid_case.csv"

df = pd.read_csv(FILE)

required_columns = [
    "hour",
    "historical_load_kw",
    "temperature_c",
    "tariff_per_kwh"
]

errors = []

# Check required columns
for col in required_columns:
    if col not in df.columns:
        errors.append(f"Missing column: {col}")

# Check empty values
if df[required_columns].isnull().any().any():
    errors.append("Missing values found")

# Check hour range
if "hour" in df.columns:
    if not df["hour"].between(0, 23).all():
        errors.append("Invalid hour value")

# Check load
if "historical_load_kw" in df.columns:
    if (df["historical_load_kw"] < 0).any():
        errors.append("Negative load value")

if errors:
    print("STEP 1 DATA CHECK FAILED")
    print("-------------------------")
    for error in errors:
        print("ERROR:", error)
else:
    print("STEP 1 DATA CHECK PASSED")