# Python Practice Exercises — 22 Questions

## Section A: Basic Python Exercises

### 1. Detect Duplicate Numbers
Given `numbers = [1, 2, 3, 1]`, write a program that checks whether the list contains duplicate numbers. Use a loop and a collection to track numbers already seen. Print `Duplicate found` and stop at the first duplicate.

**Expected output:** `Duplicate found`

### 2. Reverse a String
Given `text = "python"`, reverse the order of its characters and print the result.

**Expected output:** `nohtyp`

### 3. Count Characters in a String
Given `text = "programming"`, count its characters using a `for` loop and a counter variable, **without using `len()`**.

**Expected output:** `11`

### 4. Count Occurrences of a Character
Given `text = "banana"`, count how many times the character `a` appears using a loop.

**Expected output:** `3`

### 5. Student Score Lookup
Given:

```python
students = {"David": 85, "John": 72, "Mary": 91, "Sarah": 88}
```

Ask the user to enter a student name. Remove leading/trailing spaces, look up the name in the dictionary, and print the score. If the name is absent, print `invalid student`.

**Example:** Input `Mary` → Output `91`.

### 6. Count Word Frequencies
Given `sentence = "python is easy and is python is powerful"`, split the sentence into words, count each word's occurrences using a dictionary, and print the dictionary.

**Expected output:**

```python
{'python': 2, 'is': 3, 'easy': 1, 'and': 1, 'powerful': 1}
```

### 7. Count Vowels
Given `text = "programming"`, count the total occurrences of the vowels `a`, `e`, `i`, `o`, and `u` using a loop.

**Expected output:** `3`

### 8. Find the Most Frequent Character
Given `text = "banana"`, count each character's frequency in a dictionary, then find and print the most frequent character. If there is a tie, choose the character encountered first.

**Expected output:** `a`

### 9. Remove Duplicate Characters
Given `text = "banana"`, create a new string containing each character only once, preserving its first-appearance order.

**Expected output:** `ban`

### 10. Count Words in a Sentence
Given `sentence = "Python is easy to learn"`, split the sentence and count the words using a loop, **without using `len()` to count them**.

**Expected output:** `5`

### 11. Find the Longest Word
Given `sentence = "Python programming is interesting"`, split the sentence into words and find the longest one. If words tie, return the first encountered.

**Expected output:** `programming`

---

## Section B: Functions and Problem-Solving

### 12. Find the Largest and Smallest Numbers
Write `find_min_max(numbers)` for the list:

```python
numbers = [15, 3, 27, 8, 42, 11]
```

- Find the largest and smallest values using a loop, **without `min()` or `max()`**.
- Return both values (largest first).
- Return `None` for an empty list, and display a suitable message in that case.

**Expected output:**

```text
Largest: 42
Smallest: 3
```

### 13. Count Word Frequencies with a Function
Write `word_frequency(sentence)` for:

```python
sentence = "python is great and python is powerful"
```

Convert the sentence to lowercase, split it into words, count each word using a dictionary, and return the dictionary. Display each word with its count.

**Expected output:**

```text
python: 2
is: 2
great: 1
and: 1
powerful: 1
```

### 14. Search for a Student by Name
Given:

```python
students = [
    {"name": "Alice", "age": 20, "score": 85},
    {"name": "Bob", "age": 22, "score": 72},
    {"name": "Charlie", "age": 19, "score": 91},
    {"name": "David", "age": 21, "score": 68},
    {"name": "Esther", "age": 20, "score": 95}
]
```

Write `search_student(students, name)` that searches case-insensitively and returns the matching student's dictionary, or `None` if absent. Prompt for a name and print the student's name, age, and score, or `Student not found.`

**Example input:** `Esther`

**Expected output:**

```text
Student Found!
Name: Esther
Age: 20
Score: 95
```

### 15. Find Duplicate Numbers and Their Frequencies
Given:

```python
numbers = [4, 2, 7, 4, 9, 2, 4, 7, 7, 7]
```

Write `analyze_numbers(numbers)` that:

1. Counts occurrences of every number.
2. Creates a dictionary of only duplicated numbers and their frequencies.
3. Finds the most frequent number and its count (choose the first encountered on a tie).
4. Returns the duplicates dictionary, most frequent number, and highest count.

**Expected output:**

```text
Duplicate numbers:
4 appears 3 times
2 appears 2 times
7 appears 4 times

Most frequent number: 7
Frequency: 4
```

### 16. Find the First Non-Repeating Character
Write `first_unique_character(text)` to count character frequencies and return the first character appearing exactly once. Return `None` if none exists.

**Example input:** `aabbcdd`

**Expected output:** `First unique character: c`

**If none exists:** `No unique character found.`

### 17. Separate Even and Odd Numbers
Given `numbers = [12, 7, 9, 4, 6, 3]`, write `separate_numbers(numbers)` to return two lists: even numbers and odd numbers. Preserve their original order.

**Expected output:**

```text
Even numbers: [12, 4, 6]
Odd numbers: [7, 9, 3]
```

### 18. Find All Positions of a Target Number
Given `numbers = [4, 7, 2, 7, 9, 7]`, write `find_positions(numbers, target)` that returns a list of all zero-based indices where the target appears. Return an empty list if absent.

**Expected results:**

```python
find_positions(numbers, 7)   # [1, 3, 5]
find_positions(numbers, 10)  # []
```

### 19. Calculate the Sum of Digits
Write `sum_digits(number)` to add the individual digits of an integer. Ignore the minus sign for negative numbers; return `0` for zero.

**Expected results:**

```python
sum_digits(482)   # 14
sum_digits(-305)  # 8
sum_digits(0)     # 0
```

### 20. Find Students Scoring Above Average
Given:

```python
scores = {"Alice": 80, "Bob": 60, "Mary": 90, "David": 50}
```

Write `above_average(scores)` that calculates the average score and returns a list of names whose scores are **strictly greater** than the average. Return an empty list for an empty dictionary.

**Expected results:**

```python
above_average(scores)  # ['Alice', 'Mary']
above_average({})      # []
```

### 21. Replace Every Matching Word
Given `sentence = "I like Java and Java is useful"`, write `replace_word(sentence, old_word, new_word)` to replace every exact word match. Split the sentence into words, build an updated list, join it back into a string, and return it.

**Example:** `replace_word(sentence, "Java", "Python")`

**Expected output:** `I like Python and Python is useful`

### 22. Combine Two Stock Dictionaries
Given:

```python
first_shop = {"books": 10, "pens": 20}
second_shop = {"pens": 15, "bags": 5}
```

Write `combine_stock(first_shop, second_shop)` to return a **new** dictionary combining the inventory quantities. Add quantities for items in both shops and retain quantities for items in only one. Do not modify the original dictionaries.

**Expected output:**

```python
{'books': 10, 'pens': 35, 'bags': 5}
```

---

## Skills Practised

| Concept | Exercises |
|---|---|
| Strings and string manipulation | 2–4, 7–9, 11, 16, 21 |
| Lists and indexing | 1, 12, 14, 15, 17, 18 |
| Dictionaries | 5, 6, 8, 13–16, 20, 22 |
| Loops and conditionals | Most exercises |
| Functions and return values | 12–22 |
| Searching | 1, 5, 14, 16, 18 |
| Frequency counting | 4, 6–8, 13, 15, 16 |

**Practice challenge:** Solve each exercise without checking the earlier solution. For exercises 12–22, test your function with at least three inputs, including an edge case.