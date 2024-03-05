# Import necessary libraries
import re
from collections import Counter

# Sample data of dress colors
colors_data = """
Monday: Red, Blue, Green, Red, Yellow
Tuesday: Blue, Blue, Green, Red, Red
Wednesday: Green, Green, Green, Yellow, Yellow
Thursday: Red, Red, Red, Yellow, Yellow
Friday: Blue, Blue, Green, Green, Yellow
"""

# Extract colors from the data
colors = re.findall(r'\b\w+\b', colors_data)

# Calculate mean color
mean_color = Counter(colors).most_common(1)[0][0]

# Calculate mode (most frequent color)
mode_color = Counter(colors).most_common(1)[0][0]

# Calculate median color
sorted_colors = sorted(colors)
n = len(sorted_colors)
if n % 2 == 1:
    median_color = sorted_colors[n//2]
else:
    median_color = (sorted_colors[n//2 - 1], sorted_colors[n//2])

# Calculate variance of colors
color_frequencies = Counter(colors)
total_colors = sum(color_frequencies.values())
variance = sum((freq - total_colors/len(color_frequencies))**2 for freq in color_frequencies.values()) / len(color_frequencies)

# Probability of choosing red color at random
probability_red = color_frequencies['Red'] / total_colors

# Save colors and frequencies in a PostgreSQL database
# Code for saving to database goes here

# Recursive searching algorithm
def recursive_search(numbers, target, start=0):
    if start >= len(numbers):
        return False
    if numbers[start] == target:
        return True
    return recursive_search(numbers, target, start+1)

# Generate random 4-digit binary number and convert to base 10
import random
random_binary = ''.join(random.choice('01') for _ in range(4))
random_decimal = int(random_binary, 2)

# Sum of the first 50 Fibonacci sequence
def fibonacci(n):
    a, b = 0, 1
    total = 0
    for _ in range(n):
        total += a
        a, b = b, a + b
    return total

sum_fibonacci = fibonacci(50)
    
