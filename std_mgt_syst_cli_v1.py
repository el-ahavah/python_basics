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


