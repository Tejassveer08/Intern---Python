def multiply(f, i):
    try:
        return f * i
    except Exception as e:
        print("Error:", e)
        

f = float(input("Enter a float: "))
i = int(input("Enter an integer: "))
result = multiply(f, i)
print("Product:", result)


