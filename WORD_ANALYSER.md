# Word analyser

This program reads a sentence you type and tells you about its words.
It shows the total number of words, how many different words you used,
how often each word appears, the most common word, and the longest word.

## What you need

You need Python 3.7 or newer installed on your computer and a copy of this
repository. You do not need to install any extra Python packages.

## How to open and run it in VS Code

1. Open VS Code.
2. Click **File > Open Folder** and select your **python_basics** folder.
3. Click **Terminal > New Terminal**. The terminal is the area where you type commands.
4. If your folder is already connected to this GitHub repository, get the latest files:

   ```bash
   git pull origin main
   ```

5. Type this command in the terminal and press **Enter**:

   ```bash
   python word_analyser.py
   ```

   If your computer uses `python3` instead, run `python3 word_analyser.py`.
   On Windows, you can also try `py word_analyser.py`.

## How to use it

1. Wait until you see `Enter some text:`.
2. Type or paste a sentence on one line.
3. Press **Enter**.
4. Read the results shown in the terminal.

For example, type:

```text
Python is fun and python is useful
```

The program displays:

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

Here is what those results mean:

- **Total words:** all the words you entered, including repeats.
- **Unique words:** the number of different words you entered.
- **Most common word:** the word that appears the most. "Occurrences" means how many times it appears.
- **Longest word:** the word with the most characters.
- **Word frequencies:** a list showing how many times each word appears.

In this example, `python` and `is` both appear twice. The program picks
`python` because it appeared first. It also picks `python` over `useful`
as the longest word because both have six characters and `python` came first.

## How to try another sentence or stop

The program finishes after showing one result. To analyse another sentence,
run `python word_analyser.py` again.

If you press Enter without typing any words, it asks you to run again and
enter some text. You can press **Ctrl+C** while it is waiting for input to cancel.
Your text and results are displayed in the terminal; the program does not save
them to a file.

## If it does not run

- **"Python was not found" or "command not found":** try `py` on Windows or
  `python3` on macOS/Linux in place of `python`. If none works, check that
  Python is installed and available in your terminal.
- **"Can't open file" or "No such file":** make sure your terminal is inside
  the folder containing `word_analyser.py`. Opening the correct folder in
  VS Code before creating the terminal usually resolves this.
- **No words found:** enter some letters or numbers. Spaces and punctuation
  on their own do not count as words.

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
