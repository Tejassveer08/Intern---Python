year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): # Function to check if a year is a leap year
    # If the year is divisible by 4 and not divisible by 100, or if it is divisible by 400, it is a leap year
    print("Leap year")  # Print that the year is a leap year
else:
    print("Not a leap year")
