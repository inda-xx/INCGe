# Solution

To solve the problem of analyzing a week's worth of hourly temperature readings, we'll develop a Python program. The solution involves iterating over a 2D array and using logic to calculate the average temperature, find the highest and lowest temperatures, calculate the daily temperature range, and identify temperature spikes. We'll encapsulate these functionalities in separate functions to keep the code organized and modular.

### Solution Implementation

```python
def calculate_average_temperature(temperatures):
    total_temp = 0
    count = 0
    for daily_temps in temperatures:
        total_temp += sum(daily_temps)
        count += len(daily_temps)
    return total_temp / count

def find_highest_and_lowest_temperatures(temperatures):
    highest = float('-inf')
    highest_day = highest_hour = -1
    lowest = float('inf')
    lowest_day = lowest_hour = -1

    for day in range(7):
        for hour in range(24):
            temp = temperatures[day][hour]
            if temp > highest:
                highest = temp
                highest_day = day
                highest_hour = hour
            if temp < lowest:
                lowest = temp
                lowest_day = day
                lowest_hour = hour

    return highest, highest_day, highest_hour, lowest, lowest_day, lowest_hour

def calculate_daily_temperature_ranges(temperatures):
    daily_ranges = []
    for day in temperatures:
        daily_ranges.append(max(day) - min(day))
    return daily_ranges

def find_temperature_spikes(temperatures):
    spikes = []
    for day in range(7):
        for hour in range(24):
            current_temp = temperatures[day][hour]
            previous_temp = temperatures[day][hour - 1] if hour - 1 >= 0 else None
            next_temp = temperatures[day][hour + 1] if hour + 1 < 24 else None

            if previous_temp is not None and next_temp is not None:
                if current_temp >= previous_temp + 5 and current_temp >= next_temp + 5:
                    spikes.append((day, hour))

    return spikes

def format_day_hour(day, hour):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    hour_text = f"{hour % 12 if hour % 12 != 0 else 12} {'AM' if hour < 12 else 'PM'}"
    return f"{days[day]} at {hour_text}"

def main(temperatures):
    if not temperatures or len(temperatures) != 7 or any(len(day) != 24 for day in temperatures):
        raise ValueError("Input must be a 7x24 matrix.")

    # Calculate average temperature
    avg_temp = calculate_average_temperature(temperatures)
    print(f"Average Temperature for the Week: {avg_temp:.1f}°C")

    # Find highest and lowest temperatures
    highest, high_day, high_hour, lowest, low_day, low_hour = find_highest_and_lowest_temperatures(temperatures)
    print(f"Highest Temperature: {highest}°C on {format_day_hour(high_day, high_hour)}")
    print(f"Lowest Temperature: {lowest}°C on {format_day_hour(low_day, low_hour)}")

    # Calculate daily temperature ranges
    daily_ranges = calculate_daily_temperature_ranges(temperatures)
    print("Daily Temperature Ranges:")
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for i, temp_range in enumerate(daily_ranges):
        print(f"    {days[i]}: {temp_range}°C")

    # Detect unusual temperature spikes
    spikes = find_temperature_spikes(temperatures)
    if spikes:
        print("Unusual Temperature Spikes Detected at:")
        for day, hour in spikes:
            print(f"    {format_day_hour(day, hour)}")
    else:
        print("No Unusual Temperature Spikes Detected")

# Example usage:
temperatures = [
    [13, 15, 11, 19, 20, 14, 23, 22, 21, 25, 18, 17, 23, 26, 24, 22, 21, 19, 20, 18, 15, 13, 12, 14],
    [10, 11, 12, 11, 15, 14, 13, 18, 17, 16, 19, 22, 21, 23, 22, 20, 19, 17, 15, 14, 13, 12, 11, 10],
    [14, 12, 14, 16, 17, 14, 13, 19, 20, 22, 21, 19, 23, 25, 27, 26, 24, 23, 21, 20, 18, 16, 15, 14],
    [13, 12, 11, 10, 12, 15, 14, 16, 18, 17, 19, 21, 22, 23, 25, 24, 23, 22, 20, 19, 18, 17, 16, 15],
    [10, 9, 10, 8, 7, 10, 15, 18, 20, 19, 23, 29, 30, 32, 31, 30, 28, 25, 23, 20, 18, 15, 12, 10],
    [9, 8, 7, 10, 12, 13, 11, 10, 9, 12, 15, 17, 20, 24, 21, 20, 19, 17, 15, 13, 12, 11, 10, 9],
    [10, 12, 14, 16, 15, 13, 14, 16, 15, 18, 20, 21, 23, 25, 27, 29, 28, 26, 24, 21, 17, 15, 14, 16]
]

main(temperatures)
```

### Explanation of the Solution

1. **Calculating the Average Temperature**: We iterate over the 2D array, summing up all temperatures and dividing by the total number of readings (168) to get the average temperature for the week.

2. **Finding the Highest and Lowest Temperatures**: We iterate through all temperatures, keeping track of the highest and lowest values, as well as their respective days and hours.

3. **Calculating Daily Temperature Ranges**: For each day, we compute the difference between the maximum and minimum temperatures.

4. **Detecting Temperature Spikes**: A spike is defined as a current temperature that is at least 5 degrees warmer than both the previous and next hour. We check each valid position in the 2D array, ensuring not to go out of bounds.

5. **Formatted Output**: Helper functions are used to format the day and hour data into more readable text, encapsulating formatting logic.

This solution is modular, efficient with time complexity O(n) where n is the number of temperature readings, and provides clear outputs. Each function performs a specific task, making it easier to maintain and extend the code. Additionally, input validation is included to ensure the input is a valid 7x24 array.