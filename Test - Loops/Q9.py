# Function to check if a number is palindrome
def is_palindrome(n): 
    return str(n) == str(n)[::-1] # Check if the string representation of n is equal to its reverse

# Iterate from 1,000,000 down to 1
for num in range(1000000, 0, -1): # Loop through numbers from 1,000,000 down to 1
    if is_palindrome(num): # Check if the number is a palindrome
        print(num) 
 