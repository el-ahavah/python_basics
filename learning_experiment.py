students = [
    {"id": 1, "name": "John", "grade": "B"},
    {"id": 2, "name": "Mary", "grade": "C"},
    {"id": 3, "name": "Peter", "grade": "A"}
]

# Set the target ID to search for (this does not exist in the list)
search_id = 99
student_found = False

for student in students:
    if student["id"] == search_id:
        student["grade"] = "A"
        student_found = True
        break  # Stop searching once found

# Handle the case where the ID does not exist
if not student_found:
    print(f"Error: Student with ID {search_id} does not exist.")

print("\nCurrent students list:")
print(students)
