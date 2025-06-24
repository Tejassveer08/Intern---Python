ram = int(input("Enter Ram's age: "))  # Input Ram's age from the user
shyam = int(input("Enter Shyam's age: "))  # Input Shyam's age from the user
ajay = int(input("Enter Ajay's age: "))  # Input Ajay's age from the user
youngest = min(ram, shyam, ajay)  # Find the youngest age among Ram, Shyam, and Ajay

if youngest == ram:  # Check if Ram's age is greater than Shyam's
    print("Ram is the youngest")  # If Ram is the youngest, print "Ram is the youngest"
elif youngest == shyam:  # Check if Shyam's age is greater than Ram's
    print("Shyam is the youngest")
else:  # If neither Ram nor Shyam is the youngest, then Ajay must be the youngest
    print("Ajay is the youngest")