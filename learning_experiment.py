students = [
    {"id": 1, "name": "John", "grade": "B"},
    {"id": 2, "name": "Mary", "grade": "C"},
    {"id": 3, "name": "Peter", "grade": "A"}
]

for student in students:
    if student["id"] == 2:
        student["grade"] = "A"
    
    if student["id"] == 3:
        student["grade"] = "B"

print(students)

# 1. Find the student whose ID is 3.
# 2. Change that student's grade to B.
# 3. Print the updated list.
# 4. Confirm that the other students' grades remain unchanged.
# Additional challenge: What happens if you search for student ID 5, which doesn't exist?