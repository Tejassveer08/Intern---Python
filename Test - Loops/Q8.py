nums = [] #dictionary to store numbers
while True: # Loop to continuously accept user input
    val = input("Enter a number or 'q' to quit: ") # Get user input
    if val.lower() == 'q': # Check if user wants to quit
        break # If user input is 'q', exit the loop
    nums.append(int(val)) # Append the input number to the list after converting it to an integer
average = sum(nums) / len(nums) # Calculate the average of the numbers in the list
product = 1  # Initialize product to 1 for multiplication
for n in nums: # Loop through each number in the list
    product *= n # Multiply each number to get the product
print("Average:", average) # Print the average of the numbers
print("Product:", product) # Print the product of the numbers
