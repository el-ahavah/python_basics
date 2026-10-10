students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 42},
    {"name": "Charlie", "score": 91},
    {"name": "David", "score": 68},
    {"name": "Esther", "score": 95},
    {"name": "Frank", "score": 35}
]


# 1. Calculate average score
def calculate_average(students):

    if not students:
        return 0

    total = 0

    for student in students:
        total += student["score"]

    return total / len(students)


# 2. Count passed and failed students
def count_results(students):

    passed = 0
    failed = 0

    for student in students:

        if student["score"] >= 50:
            passed += 1
        else:
            failed += 1

    return {"passed": passed, "failed": failed}


# 3. Search for a student
def search_student(students, name):

    for student in students:

        if student["name"].lower() == name.lower():
            return student

    return None


# 4. Find highest-scoring student
def highest_scoring_student(students):

    if not students:
        return None

    highest = students[0]

    for student in students:

        if student["score"] > highest["score"]:
            highest = student

    return highest


# 5. Rank students
def rank_students(students):

    return sorted(
        students,
        key=lambda student: student["score"],
        reverse=True
    )


# MAIN PROGRAM

print("STUDENT PERFORMANCE ANALYSIS")
print("----------------------------")

average = calculate_average(students)

print("Average Score:", round(average, 2))


results = count_results(students)

print("Passed:", results["passed"])
print("Failed:", results["failed"])


top_student = highest_scoring_student(students)

print("\nHighest Scoring Student:")
print(top_student["name"], "-", top_student["score"])


print("\nStudent Rankings:")

rankings = rank_students(students)

for position, student in enumerate(rankings, start=1):
    print(
        f"{position}. {student['name']} - {student['score']}"
    )


print("\nSearch for a Student")

name = input("Enter student name: ")

student = search_student(students, name)

if student:
    print("Student Found:", student)
else:
    print("Student not found.")