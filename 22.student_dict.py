def add_student(students_dict, student_id, name, age, grade):
    students_dict[student_id] ={"name": name, "age": age, "grade": grade}

# Initialize an empty dictionary for students
students = {}

# Add students dynamically
while True:
    student_id = input("Enter student ID (Type 'exit' to stop): ")
    if student_id == 'exit':
        break

    try:
        student_id = int(student_id)
    except ValueError:
        print("Please enter a numeric student ID or 'exit' to stop.")
        continue

    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")

    add_student(students, student_id, name, age, grade)

# Display all students
print("\nAll students:")
for student_id, student_details in students.items():
    print(f"Student {student_id}: {student_details}")

