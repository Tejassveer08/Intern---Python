num = input("Enter a 5-digit number: ")

if len(num) == 5 and num.isdigit():
    print("Reversed number:", num[::-1])
else:
    print("Invalid input.")
