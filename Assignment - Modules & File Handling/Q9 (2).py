import os

def merge_copy_split(file1, file2, merged_file, destination_dir):
    try:
        # Step 1: Merge contents of file1 and file2
        with open(merged_file, 'w') as mf:
            for fname in [file1, file2]:
                with open(fname, 'r') as f:
                    mf.write(f.read())
                    mf.write('\n')  # Optional: separate file contents

        print(f"✅ Files merged into: {merged_file}")

        # Step 2: Manually copy merged_file to destination
        # Make sure destination directory exists
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        # Read from source merged file
        with open(merged_file, 'r') as src, open(f"{destination_dir}/merged_copy.txt", 'w') as dst: # Destination file name
            dst.write(src.read()) # Copy contents

        print(f"✅ Merged file manually copied to: {destination_dir}/merged_copy.txt") 

        # Step 3: Split merged file line by line
        with open(merged_file, 'r') as f: # Read from source merged file
            lines = f.readlines() # Read all lines
        
        for idx, line in enumerate(lines): # Iterate over lines
            split_filename = os.path.join(destination_dir, f"split_line_{idx+1}.txt") # Create a unique filename for each line
            with open(split_filename, 'w') as sf: # Open the file for writing
                sf.write(line.strip() + '\n') # Write the line to the file

        print(f"✅ Merged file split into {len(lines)} files at: {destination_dir}") 

    except Exception as e: # Handle any exceptions
        print("❌ Error:", e)

# Sample usage
merge_copy_split(
    file1="file1.txt", 
    file2="file2.txt", 
    merged_file="merged.txt",
    destination_dir="output" # Directory where the merged and split files will be saved
)
