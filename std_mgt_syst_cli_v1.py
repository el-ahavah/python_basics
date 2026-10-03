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


