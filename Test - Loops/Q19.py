text = input("Enter a string: ")
vowels = consonants = digits = spaces = 0

for ch in text:
    if ch.lower() in 'aeiou': # Check if the character is a vowel
        vowels += 1 
    elif ch.isalpha(): # Check if the character is a consonant
        consonants += 1
    elif ch.isdigit(): # Check if the character is a digit
        digits += 1
    elif ch.isspace(): # Check if the character is a space
        spaces += 1

print(f"Vowels: {vowels}, Consonants: {consonants}, Digits: {digits}, Spaces: {spaces}")
