def is_leap_year(year):
    try:
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) # Function to check if a year is a leap year
    except Exception as e: # If an error occurs, print the error message
        print("Invalid year:", e) # Handle any exceptions that may occur

year = int(input("Enter a year: ")) # Input a year to check if it is a leap year
print("Leap Year" if is_leap_year(year) else "Not a Leap Year")# This code checks if the input year is a leap year and prints the result.
