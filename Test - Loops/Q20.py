full_name = input("Enter full name: ").split() # Split the input into parts
 
# If full name has 3+ parts, abbreviate all except last
if len(full_name) >= 2: # Check if full name has at least 2 parts
    abbrev = ''.join([name[0].upper() + '.' for name in full_name[:-1]]) # the abbreviation of all parts except the last
    print(abbrev + full_name[-1]) # Print the abbreviation followed by the last part of the name
else:
    print(full_name[0]) # If full name has only 1 part, print it as is
