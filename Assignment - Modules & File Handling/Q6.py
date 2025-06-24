def sort_student_records(filename):
    try:
        with open(filename, 'r') as file:
            records = [line.strip().split(',') for line in file]
            records.sort(key=lambda x: x[0])  # sort by name
        for name, age in records:
            print(f"Name: {name}, Age: {age}")
    except Exception as e:
        print("Error:", e)

sort_student_records(r"C:\Users\tejas\Downloads\pythoncourse\Assignment - Modules & File Handling\students.txt")
