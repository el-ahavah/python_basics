# ==========================================
# Student Management System - CLI v1
# ==========================================

students = []


# ------------------------------------------
# Helper Functions
# ------------------------------------------

def find_student(name):
    """Find and return a student by name."""

    for student in students:
        if student["name"].lower() == name.lower():
            return student

    return None


def calculate_average(scores):
    """Calculate the average of a list of scores."""

    if not scores:
        return 0

    return sum(scores) / len(scores)


def get_scores():
    """Ask the user for comma-separated scores."""

    while True:
        scores_input = input("Scores (example: 70, 80, 90): ")

        try:
            scores = [
                float(score.strip())
                for score in scores_input.split(",")
            ]

            if not scores:
                print("Please enter at least one score.")
                continue

            if any(score < 0 or score > 100 for score in scores):
                print("Scores must be between 0 and 100.")
                continue

            return scores

        except ValueError:
            print("Invalid scores. Enter numbers separated by commas.")


# ------------------------------------------
# 1. ADD STUDENT
# ------------------------------------------

def add_student():
    print("\n===== ADD STUDENT =====")

    name = input("Name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    if find_student(name):
        print("A student with that name already exists.")
        return

    while True:
        try:
            age = int(input("Age: "))

            if age <= 0:
                print("Age must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid age.")

    scores = get_scores()

    student = {
        "name": name,
        "age": age,
        "scores": scores
    }

    students.append(student)

    print(f"{name} added successfully.")


# ------------------------------------------
# 2. REMOVE STUDENT
# ------------------------------------------

def remove_student():
    print("\n===== REMOVE STUDENT =====")

    name = input("Enter student name: ").strip()

    student = find_student(name)

    if student:
        students.remove(student)
        print("Student removed.")
    else:
        print("Student not found.")


# ------------------------------------------
# 3. SEARCH STUDENT
# ------------------------------------------

def search_student():
    print("\n===== SEARCH STUDENT =====")

    name = input("Enter name: ").strip()

    student = find_student(name)

    if student:
        average = calculate_average(student["scores"])

        print("\nStudent found.")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Scores: {student['scores']}")
        print(f"Average: {average:.1f}")

    else:
        print("Student not found.")


# ------------------------------------------
# 4. UPDATE STUDENT
# ------------------------------------------

def update_student():
    print("\n===== UPDATE STUDENT =====")

    name = input("Enter student name: ").strip()

    student = find_student(name)

    if not student:
        print("Student not found.")
        return

    print("\nWhat do you want to update?")
    print("1. Name")
    print("2. Age")
    print("3. Scores")

    choice = input("Choose an option: ").strip()

    if choice == "1":

        new_name = input("Enter new name: ").strip()

        if not new_name:
            print("Name cannot be empty.")
            return

        existing_student = find_student(new_name)

        if existing_student and existing_student is not student:
            print("A student with that name already exists.")
            return

        student["name"] = new_name

        print("Name updated successfully.")

    elif choice == "2":

        while True:
            try:
                new_age = int(input("Enter new age: "))

                if new_age <= 0:
                    print("Age must be greater than 0.")
                    continue

                student["age"] = new_age
                print("Age updated successfully.")
                break

            except ValueError:
                print("Please enter a valid age.")

    elif choice == "3":

        student["scores"] = get_scores()

        print("Scores updated successfully.")

    else:
        print("Invalid option.")

