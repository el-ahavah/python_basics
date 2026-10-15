# Word analyser

A Python practice project with seven functions and no external packages.
Use Python 3.7 or newer so dictionary order preserves the first word entered.

## Run it

From this repository's folder:

```bash
python word_analyser.py
```

On systems where Python 3 uses `python3`, use that command instead.
Enter one line of text and press Enter.

For `Python is fun and python is useful`, the results are:

```text
Total words: 7
Unique words: 5
Most common word: python (2 occurrences)
Longest word: python (6 characters)

Word frequencies:
  python: 2
  is: 2
  fun: 1
  and: 1
  useful: 1
```

## The seven functions

| Function | What you practise |
| --- | --- |
| `clean_text(text)` | Strings, lowercase conversion, loops, conditions and splitting |
| `count_words(words)` | Lists, `len()` and return values |
| `count_unique_words(words)` | Sets that remove duplicate values |
| `count_word_frequency(words)` | Dictionaries, `.get()` and counting |
| `find_most_common_word(frequencies)` | Searching dictionary items and tracking a maximum |
| `find_longest_word(words)` | Searching a list and comparing lengths |
| `main()` | Input, calling functions, formatted output and error handling |

Read the functions from top to bottom. Notice how `main()` passes the cleaned
word list to the counting and searching functions. The `if __name__ == "__main__"`
guard runs the CLI only when the file is executed directly, so importing it for
tests does not prompt for input.

## Counting rules

- Capitalisation is ignored: `Python` and `python` match.
- Letters and digits are kept; other characters separate words.
- `hello,world` becomes two words rather than being joined together.
- Apostrophes and hyphens also separate words: `don't` becomes `don`, `t`;
  `well-known` becomes `well`, `known`. This is deliberately simple tokenisation.
- Numbers such as `123` count as words. Accented letters such as `é` are kept.
- When frequency or length ties, the first word entered wins.
- Frequencies are displayed in order of first appearance.
- Empty or punctuation-only input displays a helpful message.
- Ctrl+C or end-of-input cancels without a traceback.

## Check the project

```bash
python -m unittest test_word_analyser -v
```

The tests cover the example, punctuation, spacing, numbers, accented letters,
empty input, ties, later winners, CLI output and cancellation.

## Practice next

Before changing the code, predict the results for `cat dog dog elephant`.
Then run it and explain why the most common word and longest word differ.
Try writing a version of `count_unique_words()` that uses a loop instead of a set.
