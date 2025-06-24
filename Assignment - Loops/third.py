# Program to print all Armstrong numbers from 1 to 500

print("Armstrong numbers between 1 and 500 are:") # Armstrong numbers are equal to the sum of the cubes of their digits

for num in range(1, 501): # Loop through numbers from 1 to 500
    # Convert number to string to extract digits
    digits = [int(d) for d in str(num)] # Extract digits from number
    
    # Calculate sum of cubes of digits 
    sum_of_cubes = sum(d ** 3 for d in digits) # Calculate sum of cubes of digits
    
    if sum_of_cubes == num: # Check if sum of cubes is equal to the number
        print(num) # Print the Armstrong number if condition is met
