import math

# Initialize result
sum_series = 0

# Loop from 1 to 7 to calculate sum of series
for i in range(1, 8):  # inclusive of 7
    term = i / math.factorial(i)  # calculate i / i! 
    sum_series += term  # add to sum

print("Sum of first 7 terms of the series is:", round(sum_series, 4)) # Output the result rounded to 4 decimal places
