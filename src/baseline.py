import pandas as pd

LOAD = "data/hourly_load.csv"
APPS = "data/appliances.csv"

load = pd.read_csv(LOAD)
apps = pd.read_csv(APPS)

# Baseline: use the appliance start times as given,
# without optimization.
hourly_load = load["historical_load_kw"].copy()

for _, app in apps.iterrows():
    start = int(app["earliest_start"])
    duration = int(app["duration_slots"])
    power = float(app["power_kw"])

    for hour in range(start, min(start + duration, 24)):
        hourly_load.iloc[hour] += power

# Cost for each hour
hourly_cost = hourly_load * load["tariff_per_kwh"]

daily_cost = hourly_cost.sum()
peak_load_kw = hourly_load.max()

print("BASELINE SCHEDULE")
print("-----------------")
print(f"Daily cost: {daily_cost:.2f}")
print(f"Peak load: {peak_load_kw:.2f} kW")

print("\nHourly load:")
for hour, value in enumerate(hourly_load):
    print(f"Hour {hour:02d}: {value:.2f} kW")