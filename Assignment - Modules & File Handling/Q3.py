def prime_factors(n):
    try:
        i = 2 # Start with the smallest prime factor
        factors = [] 
        while i * i <= n: # Check for factors up to the square root of n
            if n % i == 0: # If i is a factor of n
                factors.append(i) # Add it to the list of factors
                n //= i # Divide n by i to reduce it
            else: 
                i += 1 # Move to the next potential factor
        if n > 1: # If n is still greater than 1, it is a prime factor
            factors.append(n) # Add it to the list of factors
        return factors # Return the list of prime factors
    except Exception as e: # Handle any exceptions that occur during the process
        print("Error:", e) # Print any error that occurs

num = int(input("Enter a number: ")) # Input a number to find its prime factors
print("Prime factors:", prime_factors(num)) # This code finds and prints the prime factors of the input number.
