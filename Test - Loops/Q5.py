total = 0
for i in range(10): # Loop to get 10 numbers from the user
    total += int(input(f"Enter number {i+1}: ")) # Add each number to the total
print("Average:", total / 10)
