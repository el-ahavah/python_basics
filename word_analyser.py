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
