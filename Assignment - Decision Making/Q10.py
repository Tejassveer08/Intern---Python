percentage = float(input("Enter your percentage: ")) # Input a percentage from the user

if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
else:
    grade = 'F'

print("Your Grade:", grade)
