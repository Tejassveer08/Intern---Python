items = []
prices = []

for i in range(5):
    item = input(f"Enter item {i + 1}: ")  # user input for item
    item_prices = list(map(int,input("Enter 3 prices (comma separated): ").split(',')))  # user input for price
    items.append(item)  # add item to list
    prices.append(item_prices)  # add price to list

budget = int(input("Enter your budget: "))  # user input for budget
print("Best offers under budget:")

for i in range(5):
    best_price = min(prices[i])  # find the best price for each item
    if best_price <= budget:  # check if best price is within budget
        print(f"{items[i]}: {best_price}")  # print item and its best price
    else:
        print(f"{items[i]}: No offers under budget")  # print if no offers under budget