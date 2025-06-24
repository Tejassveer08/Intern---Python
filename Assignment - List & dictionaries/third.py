# List of subjects
subjects = ['Math', 'Science', 'English']

# Assign random marks to 5 students in each subject
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
import random

# Store marks as a dictionary of dictionaries
marks = {sub: {s: random.randint(50, 100) for s in students} for sub in subjects} # Dictionary comprehension to create marks for each subject

# Determine toppers
toppers = {} #dictionary to hold toppers for each subject
for subject, record in marks.items(): # Iterate over each subject and its marks
    # Find the student with the maximum marks in the subject
    topper = max(record, key=record.get)
    toppers[subject] = topper

print("Toppers in each subject:")
print(toppers)
