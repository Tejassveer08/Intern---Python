
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
radius = float(input("Enter radius of circle: "))

# Rectangle
rect_area = length * breadth
rect_perimeter = 2 * (length + breadth)

# Circle
circle_area = 3.14 * radius * radius
circle_circum = 2 * 3.14 * radius

print("Rectangle - Area:", rect_area, ", Perimeter:", rect_perimeter)
print("Circle - Area:", round(circle_area, 2), ", Circumference:", round(circle_circum, 2))
