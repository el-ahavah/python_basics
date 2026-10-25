"""A beginner-friendly command-line word analyser."""


"""def clean_text(text):
    """Return lowercase words, treating punctuation as word separators."""
    cleaned_text = ""
    for character in text.lower():
        if character.isalnum():
            cleaned_text += character
        else:
            cleaned_text += " "
    return cleaned_text.split()
"""

def clean_text(text):
    """Return lowercase words, treating punctuation as word separators."""
    cleaned_characters = []

    for character in text.lower():
        if character.isalnum():
            cleaned_characters.append(character)
        else:
            cleaned_characters.append(" ")

    cleaned_text = "".join(cleaned_characters)
    return cleaned_text.split()

def count_words(words):
    """Return the total number of words, including duplicates.

    An empty list returns 0.
    """
    return len(words)


def count_unique_words(words):
    """Return how many different words appear."""
    return len(set(words))


def count_word_frequency(words):
    """Return a dictionary mapping each word to its occurrence count."""
    frequencies = {}
    for word in words:
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


def find_most_common_word(frequencies):
    """Return the most frequent word, or None for an empty dictionary.

    When counts tie, return the first word added to the dictionary.
    """
    most_common_word = None
    highest_count = 0
    for word, count in frequencies.items():
        if count > highest_count:
            most_common_word = word
            highest_count = count
    return most_common_word


def find_longest_word(words):
    """Return the longest word, or None if there are no words.

    When lengths tie, return the first word in the list.
    """
    longest_word = None
    for word in words:
        if longest_word is None or len(word) > len(longest_word):
            longest_word = word
    return longest_word


def main():
    """Collect one line of text and display its word statistics."""
    print("WORD ANALYSER")
    try:
        text = input("Enter some text: ")
    except (EOFError, KeyboardInterrupt):
        print("\nAnalysis cancelled.")
        return

    words = clean_text(text)
    if not words:
        print("No words found. Run again and enter some text.")
        return

    frequencies = count_word_frequency(words)
    most_common = find_most_common_word(frequencies)
    longest = find_longest_word(words)

    print("\nRESULTS")
    print(f"Total words: {count_words(words)}")
    print(f"Unique words: {count_unique_words(words)}")
    print(f"Most common word: {most_common} ({frequencies[most_common]} occurrences)")
    print(f"Longest word: {longest} ({len(longest)} characters)")
    print("\nWord frequencies:")
    for word, count in frequencies.items():
        print(f"  {word}: {count}")


if __name__ == "__main__":
    main()
