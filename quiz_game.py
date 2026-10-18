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
