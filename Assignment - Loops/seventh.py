# Total number of rows
rows = 7

for i in range(rows):
    # LEFT side: Always print from A up to G - i
    for j in range(7 - i): # Loop through each column
        print(chr(65 + j), end=' ') # Print the letter corresponding to the ASCII value of 'A' + j

    # Print spaces: 2*i - 1 gaps (each gap is '  ')
    print('  ' * (2 * i - 1), end='')

    # RIGHT side: If it's the first row (i == 0), skip first char to avoid duplicating 'G'
    start = 7 - i - 2 if i == 0 else 7 - i - 1

    for j in range(start, -1, -1):
        print(chr(65 + j), end=' ')

    print()
