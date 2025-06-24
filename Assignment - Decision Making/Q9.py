hours = float(input("Enter hours worked this week: ")) # Input hours worked
rate = float(input("Enter hourly wage: ")) # Input hourly wage
pay = 0 # Initialize pay variable

if hours <= 40: # If hours worked is less than or equal to 40
    pay = hours * rate # Calculate pay for regular hours
elif hours <= 60: # If hours worked is between 41 and 60
    pay = 40 * rate + (hours - 40) * rate * 1.5 # Calculate pay for regular hours and overtime at 1.5x rate
else: # If hours worked is greater than 60
    pay = 40 * rate + 20 * rate * 1.5 + (hours - 60) * rate * 2 # Calculate pay for regular hours, overtime at 1.5x rate, and double overtime at

print("Weekly Pay: ₹", round(pay, 2))
