import os 

def append_text(filename, new_text):
    try: 
        before = os.path.getsize(filename)
        with open(filename, 'a') as file:  # Open the file in append mode
                file.write(new_text + '\n')  # Append the new text with a newline
        after = os.path.getsize(filename)
        print (f"file size before : {before} bytes")
        print (f"file size after : {after} bytes")
    except Exception as e:  # Handle any exceptions that occur during the process
        print("Error:", e)  # Print any error that occurs

append_text(r"C:\Users\tejas\Downloads\pythoncourse\Assignment - Modules & File Handling\example.txt", "This is a new line of text.")  # Call the function with the file path and text to append