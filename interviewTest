Here's a Python program that addresses the requirements:

```python
import re
import random
from collections import Counter
import psycopg2

# Function to get the mean color
def mean_color(colors):
    return sum(colors) / len(colors)

# Function to get the mode (most frequent) color
def mode_color(colors):
    return max(colors, key=colors.count)

# Function to get the median color
def median_color(colors):
    sorted_colors = sorted(colors)
    n = len(sorted_colors)
    if n % 2 == 0:
        return (sorted_colors[n//2 - 1] + sorted_colors[n//2]) / 2
    else:
        return sorted_colors[n//2]

# Function to calculate variance
def variance(colors):
    mean = mean_color(colors)
    return sum((x - mean) ** 2 for x in colors) / len(colors)

# Function to calculate the probability of choosing red
def probability_of_red(colors):
    total_count = len(colors)
    red_count = colors.count('red')
    return red_count / total_count

# Function to save colors and their frequencies to PostgreSQL database
def save_to_database(colors):
    conn = psycopg2.connect("dbname=test user=postgres password=your_password")
    cur = conn.cursor()
    for color, count in colors.items():
        cur.execute("INSERT INTO colors (color, frequency) VALUES (%s, %s)", (color, count))
    conn.commit()
    conn.close()

# Recursive searching algorithm
def recursive_search(numbers, target):
    if not numbers:
        return False
    mid = len(numbers) // 2
    if numbers[mid] == target:
        return True
    elif numbers[mid] < target:
        return recursive_search(numbers[mid+1:], target)
    else:
        return recursive_search(numbers[:mid], target)

# Function to generate random 4-digit number of 0s and 1s and convert to base 10
def generate_and_convert():
    binary_num = ''.join(random.choices(['0', '1'], k=4))
    decimal_num = int(binary_num, 2)
    return binary_num, decimal_num

# Function to calculate the sum of the first 50 Fibonacci sequence
def fibonacci_sum():
    fib = [0, 1]
    for i in range(2, 51):
        fib.append(fib[i-1] + fib[i-2])
    return sum(fib)

# Sample usage
colors = ['red', 'blue', 'green', 'red', 'yellow', 'red', 'blue', 'red', 'green']
colors_counter = Counter(colors)

mean = mean_color(colors)
mode = mode_color(colors)
median = median_color(colors)
variance_val = variance(colors)
prob_red = probability_of_red(colors)

print("Mean color:", mean)
print("Mode color:", mode)
print("Median color:", median)
print("Variance of colors:", variance_val)
print("Probability of choosing red:", prob_red)

# Save colors and their frequencies to PostgreSQL database
save_to_database(colors_counter)

# Sample recursive search
numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 13
print("Is", target, "in the list?", recursive_search(numbers, target))

# Sample generate and convert
binary, decimal = generate_and_convert()
print("Random 4-digit binary number:", binary)
print("Converted to base 10:", decimal)

# Sum of the first 50 Fibonacci sequence
fib_sum = fibonacci_sum()
print("Sum of the first 50 Fibonacci sequence:", fib_sum)
``
