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
