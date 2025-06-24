def analyse_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        words = content.split()
        letters = sum(c.isalpha() for c in content)
        digits = sum(c.isdigit() for c in content)
        specials = sum(not c.isalnum() and not c.isspace() for c in content)
        spaces = sum(c.isspace() for c in content)
        
        print(f"Words: {len(words)}")
        print(f"alphabets {letters}")
        print(f"digits {digits}")
        print(f"special characters {specials}")
        print(f"white spaces {spaces}")
        
    except Exception as e:
        print(f"Error reading file {filename}: {e}")

analyse_file(r"C:\Users\tejas\Downloads\pythoncourse\Assignment - Modules & File Handling\example.txt")