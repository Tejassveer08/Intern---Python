# Start with the widest row having 7 characters
widths = [7, 5, 3, 1]

for row in range(len(widths)):
    n = widths[row]  # Number of characters to print on this row

    # Print leading spaces to center-align (spaces = (max_width - n) // 2)
    spaces = (7 - n) // 2 
    print(' ' * spaces, end='') # Print leading spaces

    # Print alternating 1s and 0s starting with 1
    for i in range(n): 
        print('1' if i % 2 == 0 else '0', end='')

    print()  # Move to next line
