# Input basic salary
basic = float(input("Enter Ramesh's basic salary: "))

# Dearness Allowance = 40%, House Rent Allowance = 20%
da = 0.40 * basic
hra = 0.20 * basic

gross_salary = basic + da + hra
print("Gross Salary = ₹", round(gross_salary, 2))
