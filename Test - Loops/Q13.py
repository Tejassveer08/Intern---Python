marks = int(input("Enter marks: "))
if marks < 25:
    grade = 'F'
elif marks < 45:
    grade = 'E'
elif marks < 50:
    grade = 'D'
elif marks < 60:
    grade = 'C'
elif marks < 70:
    grade = 'B'
else:
    grade = 'A'
print("Grade:", grade)
