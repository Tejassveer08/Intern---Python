# Initialize name list
names = ['Alice', 'Bob', 'Charlie']

# Function to add and auto-display names
def add_name(new_name): 
    names.append(new_name) 
    return names

# Add a new name
print("Updated names:", add_name("David"))
