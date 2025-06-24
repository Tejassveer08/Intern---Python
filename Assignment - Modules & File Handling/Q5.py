def read_file_with_line_numbers(filename):
    try:
        with open(filename, 'r') as file:
            for idx, line in enumerate(file, start=1):
                print(f"{idx}: {line.strip()}")
    except FileNotFoundError:
        print("❌ Error: File not found.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Use your actual path here (any of the three safe options)
file_path = r"C:\Users\tejas\Downloads\pythoncourse\Assignment - Modules & File Handling\example.txt"

read_file_with_line_numbers(file_path)
