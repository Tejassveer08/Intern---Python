# Create a sample list of numbers
numbers = [10, 15, 20, 25, 30]

# Logic:
# - Even index => increment value by 1
# - Odd index  => increment value by 2

for i in range(len(numbers)): # Iterate over the list with index
    if i % 2 == 0:  # even index
        numbers[i] += 1 # increment by 1
    else:  # odd index
        numbers[i] += 2 # increment by 2

print("Updated list:", numbers) # Output: [11, 17, 21, 27, 31]
