num = input("Enter a 4-digit number: ")

if len(num) == 4 and num.isdigit():
    first = int(num[0])
    last = int(num[-1])
    print("Sum of first and last digit:", first + last)
else:
    print("Invalid input.")
