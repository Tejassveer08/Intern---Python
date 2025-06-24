# Program to take inputs and count positives, negatives, and zeros

positive = negative = zero = 0

while True:
    num = int(input("Enter a number: "))

    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

    # Ask if the user wants to continue
    choice = input("Do you want to enter another number? (y/n): ").lower()
    if choice != 'y':
        break

print(f"Positive numbers: {positive}")
print(f"Negative numbers: {negative}")
print(f"Zeros: {zero}")
