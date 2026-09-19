import pandas as pd

LOAD = "data/hourly_load.csv"
APPS = "data/appliances.csv"

load = pd.read_csv(LOAD)
apps = pd.read_csv(APPS)

hourly_load = load["historical_load_kw"].copy()
schedule = {}

for _, app in apps.iterrows():
    app_id = app["appliance_id"]
    power = float(app["power_kw"])
    duration = int(app["duration_slots"])
    earliest = int(app["earliest_start"])
    latest_finish = int(app["latest_finish"])
    interruptible = app["interruptible"]

    best_start = None
    best_cost = float("inf")

    max_start = latest_finish - duration

    if max_start < earliest:
        print(f"IMPOSSIBLE: {app_id}")
        continue

    for start in range(earliest, max_start + 1):
        temp_load = hourly_load.copy()

        for hour in range(start, start + duration):
            temp_load.iloc[hour] += power

        cost = sum(
            temp_load.iloc[h] * float(load.iloc[h]["tariff_per_kwh"])
            for h in range(24)
        )

        if cost < best_cost:
            best_cost = cost
            best_start = start

    schedule[app_id] = best_start

    for hour in range(best_start, best_start + duration):
        hourly_load.iloc[hour] += power


daily_cost = sum(
    hourly_load.iloc[h] * float(load.iloc[h]["tariff_per_kwh"])
    for h in range(24)
)

peak_load = hourly_load.max()

print("OPTIMIZED SCHEDULE")
print("------------------")

print("\nAppliance start times:")

for app_id, start in schedule.items():
    print(f"{app_id}: {start}:00")

print(f"\nDaily cost: {daily_cost:.2f}")
print(f"Peak load: {peak_load:.2f} kW")

print("\nHourly load:")

for hour, value in enumerate(hourly_load):
    print(f"Hour {hour:02d}: {value:.2f} kW")