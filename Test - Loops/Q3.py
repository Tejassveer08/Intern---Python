for num in range(1, 1000001): # Loop through numbers from 1 to 1,000,000
    power = len(str(num)) # Calculate the number of digits in the number
    if sum(int(d)**power for d in str(num)) == num: # Check if the sum of the digits raised to the power of the number of digits equals the number itself
        print(num)
# This code finds and prints all Armstrong numbers between 1 and 1,000,000.