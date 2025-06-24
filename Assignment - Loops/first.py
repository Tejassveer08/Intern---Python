# Program to find factorial of a number

num = int(input("Enter a number: ")) # Take number input from the user
factorial = 1 # Initialize factorial to 1

# Loop from 1 to num and multiply
for i in range(1, num + 1): # inclusive of num
    factorial *= i # multiply factorial by i

print(f"Factorial of {num} is {factorial}")
