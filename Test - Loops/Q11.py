ages = [int(input(f"Enter age of person {i+1}: ")) for i in range(3)] # Get ages of three people from user input
print("Oldest:", max(ages)) # Print the age of the oldest person
print("Youngest:", min(ages)) # Print the age of the youngest person
