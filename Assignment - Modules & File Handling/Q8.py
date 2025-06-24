import os 

def get_file_location(filename):
    try:
        file_location = os.path.abspath(filename)  # Get the absolute path of the file
        print(f"The file is located at: {file_location}")  # Print the file location
    except Exception as e:  # Handle any exceptions that occur during the process
        print("Error:", e)  # Print any error that occurs
        
get_file_location(r"C:\Users\tejas\Downloads\pythoncourse\Assignment - Modules & File Handling\example.txt")  # Call the function with the file path