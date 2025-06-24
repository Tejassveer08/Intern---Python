marks = []
for i in range(1, 6):
    m = float(input(f"Enter marks for subject {i} (out of 100): "))
    marks.append(m)

total = sum(marks)
percentage = (total / 500) * 100

print("Total Marks:", total)
print("Percentage:", round(percentage, 2), "%")
