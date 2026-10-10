numbers = [1, 2, 3, 1]

seen = []

for number in numbers:
    if number in seen:
        print("Duplicate found")
        break

    seen.append(number)
    # print(seen)
#------------------------------------------
"""reverse"""

text = "python"
reversed = text[::-1]

print(reversed)
#------------------------------------------
"""count number of characters"""

text = "programming"
count = 0

for char in text:
    count += 1

print(count)
#------------------------------------------
"""count a's"""

text = "banana"
count = 0

for char in text:
    if char == "a":
        count += 1

print(count)
#------------------------------------------
"""lookup"""

students = {
    "David": 85,
    "John": 72,
    "Mary": 91,
    "Sarah": 88
}

user_input = input("Enter student: ")
user_input = user_input.strip()

if user_input in students:
    print(students[user_input])
else:
    print("invalid student")
#--------------------------------------------
""" word counter """
sentence = "python is easy and is python is powerful"
splitter = sentence.split()

storage = {}

for word in splitter:
    if word in storage:
        storage[word] += 1
    else:
        storage[word] = 1

print(storage)
#----------------------------------------------
""" count vowels """

text = "programming"
vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1
print(count)
#-----------------------------------------------
""" most frequent character """
text = "banana"
store = {}
for char in text:
    if char in store:
        store[char] += 1
    else:
        store[char] = 1

# most_frequent = max(store, key=store.get)

most_frequent = ""
highest_count = 0

for char in store:
    if store[char] > highest_count:
        highest_count = store[char]
        most_frequent = char

print(most_frequent)
#-----------------------------------------------
""" remove duplicate character """
text = "banana"

result = ""

for char in text:
    if char not in result:
        result += char

print(result)
#-----------------------------------------------
""" count words """
sentence = "Python is easy to learn"
splitter = sentence.split()
count = 0
for word in splitter:
    count += 1

print(count)
#-----------------------------------------------
""" find the longest word """
sentence = "Python programming is interesting"
splitter = sentence.split()
longest = ""
for word in splitter:
    if len(word) > len(longest):
        longest = word
print(longest)
#------------------------------------------------------------------
"""Find the Largest and Smallest Numbers"""
def find_min_max(numbers):

    if not numbers:
        return None

    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers:

        if number > largest:
            largest = number

        if number < smallest:
            smallest = number

    return largest, smallest


numbers = [15, 3, 27, 8, 42, 11]

result = find_min_max(numbers)

if result is not None:
    largest, smallest = result

    print("Largest:", largest)
    print("Smallest:", smallest)
else:
    print("The list is empty.")
#----------------------------------------------------
"""Count Word Frequencies"""
def word_frequency(sentence):

    words = sentence.lower().split()

    frequency = {}

    for word in words:

        if word in frequency:
            frequency[word] += 1

        else:
            frequency[word] = 1

    return frequency


sentence = "python is great and python is powerful"

result = word_frequency(sentence)

for word, count in result.items():
    print(f"{word}: {count}")
#-------------------------------------------------------------
"""Search for a Student by Name"""
students = [
    {"name": "Alice", "age": 20, "score": 85},
    {"name": "Bob", "age": 22, "score": 72},
    {"name": "Charlie", "age": 19, "score": 91},
    {"name": "David", "age": 21, "score": 68},
    {"name": "Esther", "age": 20, "score": 95}
]


def search_student(students, name):

    for student in students:

        if student["name"].lower() == name.lower():
            return student

    return None


search_name = input("Enter student name: ")

result = search_student(students, search_name)

if result:

    print("\nStudent Found!")
    print("Name:", result["name"])
    print("Age:", result["age"])
    print("Score:", result["score"])

else:
    print("Student not found.")
#---------------------------------------------------------------
"""Find Duplicate Numbers and Their Frequencies"""
def analyze_numbers(numbers):

    frequency = {}

    # Count occurrences
    for number in numbers:

        if number in frequency:
            frequency[number] += 1

        else:
            frequency[number] = 1

    # Find duplicates
    duplicates = {}

    for number, count in frequency.items():

        if count > 1:
            duplicates[number] = count

    # Find most frequent number
    most_frequent = None
    highest_count = 0

    for number, count in frequency.items():

        if count > highest_count:
            highest_count = count
            most_frequent = number

    return duplicates, most_frequent, highest_count


numbers = [4, 2, 7, 4, 9, 2, 4, 7, 7, 7]

duplicates, most_frequent, highest_count = analyze_numbers(numbers)

print("Duplicate numbers:")

for number, count in duplicates.items():
    print(f"{number} appears {count} times")

print()

print("Most frequent number:", most_frequent)
print("Frequency:", highest_count)