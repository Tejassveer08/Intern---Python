quantity = int(input("Enter quantity: ")) # Get user input for quantity
cost = quantity * 100 # Calculate total cost based on quantity
if cost > 1000: # Check if total cost exceeds 1000
    cost *= 0.9  # Apply 10% discount 
print("Total cost:", cost) # Print the final total cost after applying any discounts
