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
