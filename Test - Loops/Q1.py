a, b = 1, 2 # Initialize the first two Fibonacci numbers
while a <= 4000000: # Loop until the 6th Fibonacci number is reached
    if a % 2 != 0: # Check if the number is odd
        print(a, end=', ') # Print the odd Fibonacci number
    a, b = b, a + b # Update the Fibonacci numbers for the next iteration
print() # Print a newline at the end
