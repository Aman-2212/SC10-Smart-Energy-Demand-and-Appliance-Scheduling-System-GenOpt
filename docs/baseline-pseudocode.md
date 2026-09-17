# Baseline Pseudocode

READ one valid input row

IF the row is invalid:
    SHOW a clear error
ELSE:
    APPLY the simple rules in order
    CALCULATE the baseline output
    PRINT the output and the rule that was used
    SAVE the result for later comparison

## Baseline rules
1. Use appliance start times entered by the user without optimization.
2. For every hour, add the power of all running appliances.
3. hourly_cost = load_kw × tariff_per_kwh
4. daily_cost = sum(hourly_cost)
5. peak_load_kw = maximum hourly load
