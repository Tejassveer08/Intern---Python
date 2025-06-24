# Get user input for first names
names = tuple(input("Enter first names (comma separated): ").split(',')) # user input for first names
surnames = tuple(input("Enter surnames (comma separated): ").split(',')) # user input for surnames

# Combine name[i] with surname[i] # to create full names
full = tuple(f"{names[i].strip()} {surnames[i].strip()}" for i in range(len(names))) # combine names and surnames

print("Full Names:", full)
