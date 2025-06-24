data = {
    'apple': 'fruit',
    'carrot': 'vegetable',
    'dog': 'animal'
}

# Print each key N times, where N is its position (1-based)
for i, key in enumerate(data.keys(), start=1): # enumerate starts counting from 1
    print((key + ' ') * i)  
