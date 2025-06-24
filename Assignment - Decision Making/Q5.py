num = input("Enter a 5 digit number: ")  # Input a number from the user
if num == num[::-1]:  # Check if the number is a palindrome by comparing it to its reverse
    print("Palindrome")  # If the number is a palindrome, print "Palindrome"
else:
    print("Not a palindrome")  # If the number is not a palindrome, print "Not a palindrome"