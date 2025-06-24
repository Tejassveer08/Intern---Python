# Fixed list of items and their prices
items = ['Pen', 'Notebook', 'Bag', 'Shoes', 'Water Bottle'] # list of items
prices = [10, 40, 500, 800, 60] # list of prices corresponding to items

# Get user's budget
budget = int(input("Enter your budget: ")) # input budget from user, integer type

# Return items within the budget
print("Items within your budget:") # print header
for i in range(len(items)): # Iterate over the list with index
    # Check if the price of the item is within the budget
    if prices[i] <= budget: # if price is less than or equal to budget
        print(f"{items[i]} - Rs.{prices[i]}") # print item and its price
