cp = float(input("Enter the cost price of the product: "))
sp = float(input("Enter the selling price of the product: "))

if sp > cp:
    print("Profit", sp - cp)
elif sp < cp:
    print("Loss", cp - sp)
else:
    print("No Profit No Loss")
