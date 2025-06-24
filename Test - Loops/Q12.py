held = int(input("Classes held: ")) # Get the number of classes held from user input
attended = int(input("Classes attended: ")) # Get the number of classes attended from user input
percent = (attended / held) * 100   # Calculate attendance percentage
print(f"Attendance: {percent:.2f}%") # Print attendance percentage formatted to two decimal places
if percent >= 75: # Check if attendance percentage is 75% or more
    print("Allowed to sit for exam.")  # If attendance percentage is 75% or more, print message
else:
    cause = input("Do you have a medical cause? (Y/N): ") # If attendance percentage is less than 75%, ask if there is a medical cause
    print("Allowed." if cause.upper() == 'Y' else "Not allowed.") # Print message based on medical cause input
