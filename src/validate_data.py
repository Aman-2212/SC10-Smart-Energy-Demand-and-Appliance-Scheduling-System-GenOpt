import pandas as pd

LOAD = "data/hourly_load.csv"
APPS = "data/appliances.csv"

load = pd.read_csv(LOAD)
apps = pd.read_csv(APPS)

required_load = ["hour", "historical_load_kw", "temperature_c", "tariff_per_kwh"]
required_apps = [
    "appliance_id", "appliance_name", "power_kw", "duration_slots",
    "earliest_start", "latest_finish", "interruptible", "priority"
]

missing_load = [c for c in required_load if c not in load.columns]
missing_apps = [c for c in required_apps if c not in apps.columns]

assert not missing_load, f"Missing load columns: {missing_load}"
assert not missing_apps, f"Missing appliance columns: {missing_apps}"
assert len(load) == 24, "hourly_load.csv must contain exactly 24 rows"
assert load["hour"].between(0, 23).all(), "hour must be 0..23"
assert (load["historical_load_kw"] >= 0).all(), "historical_load_kw cannot be negative"
assert (load["tariff_per_kwh"] >= 0).all(), "tariff_per_kwh cannot be negative"
assert (apps["power_kw"] > 0).all(), "power_kw must be positive"
assert apps["duration_slots"].between(1, 24).all(), "duration_slots must be 1..24"
assert apps["earliest_start"].between(0, 23).all(), "earliest_start must be 0..23"
assert apps["latest_finish"].between(1, 24).all(), "latest_finish must be 1..24"
assert (apps["earliest_start"] < apps["latest_finish"]).all(), "start must be before finish"
assert apps["appliance_id"].is_unique, "appliance_id must be unique"
assert apps["interruptible"].isin(["yes", "no"]).all(), "interruptible must be yes/no"
assert apps["priority"].isin(["low", "medium", "high"]).all(), "priority must be low/medium/high"

print("STEP 1 DATA CHECK PASSED")
