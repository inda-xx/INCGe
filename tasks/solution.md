# Solution

Certainly! Here's a solution for the task "Analyze and Manipulate Temperatures Using Arrays and Loops". 

```python
# Initialize an Array
weeklyTemperatures = [68, 70, 75, 72, 69, 74, 73]

# 2. Calculate Average Temperature
def calculate_average_temperature(temperatures):
    total_temperature = 0
    for temperature in temperatures:
        total_temperature += temperature
    average_temperature = total_temperature / len(temperatures)
    print(f"The average temperature for the week is {average_temperature:.2f} degrees.")

calculate_average_temperature(weeklyTemperatures)

# 3. Identify Temperature Trends
def identify_temperature_trends(temperatures):
    for i in range(1, len(temperatures)):
        if temperatures[i] > temperatures[i - 1]:
            print(f"Day {i+1}: Increasing trend")
        elif temperatures[i] < temperatures[i - 1]:
            print(f"Day {i+1}: Decreasing trend")
        else:
            print(f"Day {i+1}: Constant")

identify_temperature_trends(weeklyTemperatures)

# 4. Detect and Print Extremes
def detect_temperature_extremes(temperatures):
    highest_temperature = max(temperatures)
    lowest_temperature = min(temperatures)
    print(f"The highest temperature was {highest_temperature} degrees, and the lowest was {lowest_temperature} degrees.")

detect_temperature_extremes(weeklyTemperatures)

# 5. Heatwave Detection
def detect_heatwave(temperatures):
    heatwave = False
    consecutive_days = 0
    for temperature in temperatures:
        if temperature > 70:
            consecutive_days += 1
            if consecutive_days >= 3:
                heatwave = True
        else:
            consecutive_days = 0
    if heatwave:
        print("Heatwave detected!")
    else:
        print("No heatwave detected.")

detect_heatwave(weeklyTemperatures)

# 6. Adjust Temperatures
def adjust_temperatures(temperatures):
    adjusted_temperatures = []
    for temperature in temperatures:
        adjusted_temperatures.append(temperature - 2)
    print("Adjusted temperatures for the week:", adjusted_temperatures)

adjust_temperatures(weeklyTemperatures)
```

### Explanation of the Solution:

1. **Initialize an Array**: We initialize an array named `weeklyTemperatures` with hardcoded temperature values.

2. **Calculate Average Temperature**: The `calculate_average_temperature` function iterates over each temperature in the `weeklyTemperatures` array, calculates the sum, and divides by the number of days to get the average temperature.

3. **Identify Temperature Trends**: The `identify_temperature_trends` function uses a `for` loop, starting from the second temperature, to compare each day's temperature with the previous day's temperature. Depending on whether it's higher, lower, or the same, it prints the trend.

4. **Detect and Print Extremes**: The `detect_temperature_extremes` function finds the highest and lowest temperatures using Python's built-in `max()` and `min()` functions and prints them.

5. **Heatwave Detection**: The `detect_heatwave` function checks for any sequence of three or more consecutive days with temperatures above 70 degrees using a simple logic within a loop.

6. **Adjust Temperatures**: The `adjust_temperatures` function creates a new list with each temperature adjusted down by 2 degrees and prints this list.

This structured solution effectively uses loops for array traversal and performs multiple operations to analyze and manipulate the data.