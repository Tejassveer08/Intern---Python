num_people = int(input("Enter number of people: ")) # user input for number of people
adults = {} # dictionary to store adults' names
cities_chosen = [] # list to store cities chosen by adults

for _ in range(num_people):
    name = input("Enter name: ") # user input for name
    age = int(input("Enter age: ")) # user input for age
    sex = input("Enter sex: ")  # user input for gender
    location = input("Enter current location: ") # user input for current location

    if age > 18: # check if age is greater than 18
        print(f"Welcome {name}!")
        city = input("Choose a city to live: ") # user input for city choice
        adults[name] = city # store name and city in dictionary
        cities_chosen.append(city) # store city in list

# Display final list
print("\nCity choices by adults:")
for person, city in adults.items(): # iterate through dictionary
    print(f"{person} chose {city}") # print name and city
