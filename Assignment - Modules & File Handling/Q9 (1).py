def generate_sample_files():
    try:
        # Create file1.txt
        with open("file1.txt", 'w') as f1:
            f1.write("This is the first file.\nIt has some sample lines.\nEnd of file1.")

        # Create file2.txt
        with open("file2.txt", 'w') as f2:
            f2.write("Welcome to the second file.\nHere's more sample text.\nEnd of file2.")

        print("✅ file1.txt and file2.txt created successfully.")

        # Merge file1 and file2 into merged.txt
        with open("merged.txt", 'w') as merged:
            for file in ["file1.txt", "file2.txt"]:
                with open(file, 'r') as f:
                    merged.write(f.read() + "\n")  # Add a newline for separation

        print("✅ merged.txt created with content from both files.")

    except Exception as e:
        print("❌ Error generating sample files:", e)

# Run the function
generate_sample_files()
