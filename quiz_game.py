"""A beginner-friendly command-line quiz game called BrainQuest."""


def welcome_player():
    """Welcome the player and return a non-empty name."""
    print("\nWelcome to BrainQuest!")
    print("Answer five questions and earn one point for each correct answer.")
    print("Type A, B, C, or D to answer. Press Ctrl+C to leave at any time.")

    while True:
        player_name = input("\nWhat is your name? ").strip()
        if player_name:
            print(f"Hello, {player_name}! Let's play.")
            return player_name
        print("Please enter your name so we know what to call you.")


def choose_category():
    """Display the topics and return the selected category."""
    categories = {"1": "Python basics", "2": "General knowledge", "3": "Science"}
    print("\nChoose a quiz topic:")
    for number, category in categories.items():
        print(f"{number}. {category}")

    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice in categories:
            return categories[choice]
        print("That option is not available. Please choose 1, 2, or 3.")


def get_questions(category):
    """Return the five questions for the selected category."""
    # Each category contains a list of question dictionaries.
    # Each question stores its text, four options, and the correct letter.
    questions = {
        "Python basics": [
            {
                "question": "Which Python type stores key-value pairs?",
                "options": {"A": "List", "B": "Dictionary", "C": "String", "D": "Tuple"},
                "answer": "B",
            },
            {
                "question": "Which keyword starts a function definition?",
                "options": {"A": "for", "B": "return", "C": "def", "D": "if"},
                "answer": "C",
            },
            {
                "question": "What does len([10, 20, 30]) return?",
                "options": {"A": "3", "B": "2", "C": "30", "D": "60"},
                "answer": "A",
            },
            {
                "question": "What is the index of the first item in a Python list?",
                "options": {"A": "1", "B": "-1", "C": "2", "D": "0"},
                "answer": "D",
            },
            {
                "question": "Which method converts a string to lowercase?",
                "options": {"A": "upper()", "B": "lower()", "C": "split()", "D": "strip()"},
                "answer": "B",
            },
        ],
        "General knowledge": [
            {
                "question": "What is the capital city of Nigeria?",
                "options": {"A": "Lagos", "B": "Kano", "C": "Abuja", "D": "Ibadan"},
                "answer": "C",
            },
            {
                "question": "Which is the largest ocean on Earth?",
                "options": {"A": "Pacific", "B": "Atlantic", "C": "Indian", "D": "Arctic"},
                "answer": "A",
            },
            {
                "question": "How many sides does a triangle have?",
                "options": {"A": "4", "B": "6", "C": "5", "D": "3"},
                "answer": "D",
            },
            {
                "question": "How many minutes are in one hour?",
                "options": {"A": "30", "B": "60", "C": "90", "D": "100"},
                "answer": "B",
            },
            {
                "question": "On which continent is Nigeria located?",
                "options": {"A": "Asia", "B": "Europe", "C": "Africa", "D": "South America"},
                "answer": "C",
            },
        ],
        "Science": [
            {
                "question": "Which planet is known as the Red Planet?",
                "options": {"A": "Venus", "B": "Mars", "C": "Earth", "D": "Jupiter"},
                "answer": "B",
            },
            {
                "question": "What is the chemical formula for water?",
                "options": {"A": "CO2", "B": "O2", "C": "NaCl", "D": "H2O"},
                "answer": "D",
            },
            {
                "question": "Which gas do plants absorb during photosynthesis?",
                "options": {"A": "Carbon dioxide", "B": "Oxygen", "C": "Helium", "D": "Hydrogen"},
                "answer": "A",
            },
            {
                "question": "Which organ pumps blood around the human body?",
                "options": {"A": "Lungs", "B": "Brain", "C": "Heart", "D": "Stomach"},
                "answer": "C",
            },
            {
                "question": "What force keeps us on the ground?",
                "options": {"A": "Magnetism", "B": "Gravity", "C": "Friction", "D": "Electricity"},
                "answer": "B",
            },
        ],
    }
    return questions[category]


def ask_question(question, question_number, total_questions):
    """Show a question and return a valid uppercase answer letter."""
    print(f"\nQuestion {question_number} of {total_questions}")
    print(question["question"])
    for letter, option in question["options"].items():
        print(f"{letter}. {option}")

    while True:
        answer = input("Your answer (A, B, C, or D): ").strip().upper()
        if answer in question["options"]:
            return answer
        print("Please type A, B, C, or D. Lowercase letters work too.")
