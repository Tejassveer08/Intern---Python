# Sample list of tuples
foods = [
    ('burger', 'fries'),
    ('pizza', 'burger'),
    ('salad', 'juice')
]

# Assign categories manually
category_dict = {
    'burger': 'Fast Food',
    'fries': 'Fast Food',
    'pizza': 'Italian',
    'salad': 'Healthy',
    'juice': 'Beverage'
}

# Get unique food items from all tuples
unique_items = set(item for tup in foods for item in tup)

# Group items by category
categorized = {} # dictionary to hold categorized items
for item in unique_items: # iterate through unique items
    category = category_dict.get(item, 'Unknown') # get category from dictionary, default to 'Unknown'
    # If category not in categorized, initialize it
    if category not in categorized: 
        categorized[category] = [] # initialize list for category
    categorized[category].append(item) # append item to the category list

# Display categorized lists
for cat, items in categorized.items(): # iterate through categorized dictionary
    print(f"{cat}: {items}")
