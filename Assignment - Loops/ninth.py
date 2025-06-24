# Total number of rows in the pattern
rows = 4

# Counter to keep track of numbers
num = 1

# Loop through each row
for i in range(1, rows + 1): #  # Loop from 1 to rows (inclusive)
    # For each row, print leading spaces for centering
    
    print("  " * (rows - i), end='') # Print leading spaces for centering

    # Print numbers with spacing
    for j in range(i): # Loop through each column in the row
        print(f"{num} ", end=' ')  # Print the number followed by a space
        num += 1 # Increment the number for the next column

    print()  # Move to the next line
