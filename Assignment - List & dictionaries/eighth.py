words = {
    "apple": "A fruit",
    "python": "A programming language",
    "ocean": "A large body of water",
    "moon": "Earth's natural satellite",
}

length_diffs = {key: abs(len(words) - len(key)) for key in words} # calculate the difference in length between the dictionary and each key

max_diff_key = max(length_diffs, key=length_diffs.get) # find the key with the maximum difference
print("Word with maximum length difference:", max_diff_key)