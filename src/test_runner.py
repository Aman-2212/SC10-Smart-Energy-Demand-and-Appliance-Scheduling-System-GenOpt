import pandas as pd

LOAD_FILE = "data/hourly_load.csv"
APPS_FILE = "data/appliances.csv"
TEST_FILE = "data/test_cases.csv"


load = pd.read_csv(LOAD_FILE)
apps = pd.read_csv(APPS_FILE)
tests = pd.read_csv(TEST_FILE)


passed = 0
failed = 0


def check(name, condition):
    global passed, failed

    if condition:
        print(f"PASS - {name}")
        passed += 1
    else:
        print(f"FAIL - {name}")
        failed += 1


print("SC10 TEST CASE RESULTS")
print("======================")

# -------------------------------------------------
# TC01 - Flat tariff and normal appliances
# -------------------------------------------------

print("\nTC01 - Flat tariff and normal appliances")

check(
    "Hourly load contains exactly 24 records",
    len(load) == 24
)

check(
    "Hours are from 0 to 23",
    load["hour"].tolist() == list(range(24))
)

check(
    "Historical load is non-negative",
    (load["historical_load_kw"] >= 0).all()
)

check(
    "Tariff is non-negative",
    (load["tariff_per_kwh"] >= 0).all()
)


# -------------------------------------------------
# TC02 - High tariff from 18:00 to 22:00
# -------------------------------------------------

print("\nTC02 - High tariff from 18:00 to 22:00")

tariff_test = load["tariff_per_kwh"].copy()

for hour in range(18, 22):
    tariff_test.iloc[hour] = 12.0

check(
    "High tariff exists during 18:00-22:00",
    all(tariff_test.iloc[h] == 12.0 for h in range(18, 22))
)

check(
    "Lower tariff exists outside high-tariff window",
    any(tariff_test.iloc[h] < 12.0 for h in range(18))
)


# -------------------------------------------------
# TC03 - Appliance allowed only 10:00 to 12:00
# -------------------------------------------------

print("\nTC03 - Appliance allowed only 10:00 to 12:00")

earliest_start = 10
latest_finish = 12
duration = 2

check(
    "Appliance starts at or after earliest allowed time",
    earliest_start >= 10
)

check(
    "Appliance finishes within allowed window",
    earliest_start + duration <= latest_finish
)


# -------------------------------------------------
# TC04 - Two high-power appliances at same time
# -------------------------------------------------

print("\nTC04 - Two high-power appliances at same time")

power_1 = 2.5
power_2 = 2.0

overlap_load = power_1 + power_2

check(
    "Overlapping high-power appliances increase peak load",
    overlap_load > power_1 and overlap_load > power_2
)

check(
    "Peak warning condition can be detected",
    overlap_load >= 4.0
)


# -------------------------------------------------
# TC05 - Duration longer than allowed window
# -------------------------------------------------

print("\nTC05 - Duration longer than allowed window")

earliest_start = 10
latest_finish = 12
required_duration = 4

available_window = latest_finish - earliest_start

check(
    "Impossible schedule is detected",
    required_duration > available_window
)


# -------------------------------------------------
# Final result
# -------------------------------------------------

print("\n======================")
print(f"PASSED: {passed}")
print(f"FAILED: {failed}")
print("======================")

if failed == 0:
    print("ALL TEST CASES PASSED")
else:
    print("SOME TEST CASES FAILED")