alphabets = [chr(65 + i) for i in range(10)] # Generate first 10 uppercase letters A-J
k = 0 
for i in range(1, 5):  # 4 rows
    print(" " * (5 - i), end='') # Print leading spaces for centering
    for j in range(i):  # Loop through each column in the row
        if k < 10: # Ensure we don't exceed the length of alphabets
            print(alphabets[k], end=' ') # Print the letter followed by a space
            k += 1 
    print()
