# Program to print all prime numbers from 1 to 300

print("Prime numbers from 1 to 300 are:")

for num in range(2, 301):  # Start from 2 (first prime)
    is_prime = True # Assume num is prime until proven otherwise

    for i in range(2, int(num ** 0.5) + 1):  # Check divisibility up to the square root of num
        if num % i == 0: # If divisible, not a prime
            is_prime = False 
            break  # Not a prime, no need to check further

    if is_prime:
        print(num, end=' ')
