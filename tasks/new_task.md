### Task Description

**Exercise 1: Dynamic Temperature Analysis**

**Subject:** Arrays

**Difficulty:** Medium

**Skills:** Loops

---

**Objective:**

Enhance your understanding of arrays and loops by analyzing and processing a dataset of temperature readings. This exercise focuses on iterating through arrays and applying logic to solve real-world problems.

---

**Problem Statement:**

In this exercise, you are tasked with developing a program that processes a week's worth of hourly temperature readings. Your program should analyze the data to determine and display the following information:

1. The average temperature for the week.
2. The highest and lowest temperatures recorded, along with their respective days and hours.
3. The temperature range for each day (i.e., the difference between the highest and lowest temperature of a day).
4. Any unusual temperature spikes: Define a spike as an instance where the temperature is at least 5 degrees higher than the two surrounding readings (the hour before and after).

Consider the week starts on Monday at 12:00 AM and ends on Sunday at 11:59 PM. The input is provided as a 2D array where each row corresponds to a day, and each column corresponds to an hourly reading (168 readings total for a week).

**Constraints:**

- Assume the temperature readings are provided in a 7x24 integer array.
- Temperatures can range from -30 to 50 degrees Celsius.
- You must use loops to navigate through the array and process the readings.

---

**Example Input:**

```python
temperatures = [
    [13, 15, 11, ..., 14],  # Monday readings
    [10, 9, 12, ..., 11],   # Tuesday readings
    ...,
    [17, 14, 15, ..., 16]   # Sunday readings
]
```

**Output Example:**

```plaintext
Average Temperature for the Week: 12.5°C
Highest Temperature: 30°C on Thursday at 2 PM
Lowest Temperature: -5°C on Saturday at 5 AM
Daily Temperature Ranges:
    Monday: 5°C
    ...
    Sunday: 4°C
Unusual Temperature Spikes Detected at:
    Thursday 3 PM, Friday 11 AM
```

---

**Instructions:**

1. Initialize a 2D array to represent the temperature data for each day of the week.
2. Implement loop constructs to traverse through this array and calculate required results.
3. Include input validation to ensure that all temperature readings fall within the specified range.
4. Use encapsulated functions to calculate the average temperature, detect spikes, and determine temperature ranges.
5. Test your program with different data sets to validate correctness and handle edge cases effectively.

---

**Notes:**

- Focus on writing clean and efficient code with comments explaining your logic.
- Make use of built-in functions for any repetitive tasks where appropriate.
- Consider the scalability of your program; how might you adapt this for larger datasets or different input formats in the future?

This exercise not only tests your understanding of arrays and loops but should also help you think critically about data processing and analysis scenarios common in domains such as meteorology and environmental science.