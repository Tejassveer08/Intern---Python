year = int(input("Enter a year: "))  # Input a year from the user
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap Year")  # If the year is divisible by 4 and not by 100, or divisible by 400, print "Leap Year"
else:
    print("Not a Leap Year")
    