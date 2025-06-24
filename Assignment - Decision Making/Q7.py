a = float(input("Enter first angle: ")) # in degrees
b = float(input("Enter second angle: ")) # in degrees
c = float(input("Enter third angle: "))  # in degrees

if a + b + c == 180:   #angle sum property of triangle
    print("Triangle is valid") 
else:
    print("Triangle is not valid") 
