"""A beginner-friendly command-line word analyser."""


def clean_text(text):
    """Return lowercase words, treating punctuation as word separators."""
    cleaned_text = ""
    for character in text.lower():
        if character.isalnum():
            cleaned_text += character
        else:
            cleaned_text += " "
    return cleaned_text.split()


def count_words(words):
    """Return the number of words, including repeated words."""
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
