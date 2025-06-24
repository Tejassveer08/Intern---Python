age = int(input("Enter age: "))
sex = input("Enter sex (M/F): ").upper()
marital_status = input("Married? (Y/N): ").upper()

if sex == 'F':
    print("Urban areas only")
elif sex == 'M' and 20 <= age <= 40:
    print("Can work anywhere")
elif sex == 'M' and 40 < age <= 60:
    print("Urban areas only")
else:
    print("ERROR")
