numbers = [1, 2, 3, 1]

seen = []

for number in numbers:
    if number in seen:
        print("Duplicate found")
        break

    seen.append(number)
    # print(seen)

#-----------------------------------------------------------------
#-----------------------------------------------------------------

"""reverse"""

text = "python"
reversed = text[::-1]

print(reversed)

#-----------------------------------------------------------------
#-----------------------------------------------------------------

"""count number of characters"""

text = "programming"
count = 0

for char in text:
    count += 1

print(count)

#------------------------------------------------------------------
#------------------------------------------------------------------

"""count a's"""

text = "banana"
count = 0

for char in text:
    if char == "a":
        count += 1

print(count)

#--------------------------------------------------------------
#--------------------------------------------------------------

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

#--------------------------------------------------------------
#--------------------------------------------------------------

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

#--------------------------------------------------------------
#--------------------------------------------------------------

""" count vowels """

text = "programming"
vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1
print(count)

#--------------------------------------------------------------
#--------------------------------------------------------------

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

#----------------------------------------------------------------
#----------------------------------------------------------------

""" remove duplicate character """
text = "banana"

result = ""

for char in text:
    if char not in result:
        result += char

print(result)

#-----------------------------------------------------------------
#-----------------------------------------------------------------

""" count words """
sentence = "Python is easy to learn"
splitter = sentence.split()
count = 0
for word in splitter:
    count += 1

print(count)

#-----------------------------------------------------------------
#-----------------------------------------------------------------

""" find the longest word """
sentence = "Python programming is interesting"
splitter = sentence.split()
longest = ""
for word in splitter:
    if len(word) > len(longest):
        longest = word
print(longest)

#-----------------------------------------------------------------
#-----------------------------------------------------------------

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

#---------------------------------------------------------------
#---------------------------------------------------------------

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

#-------------------------------------------------------------
#-------------------------------------------------------------

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

#--------------------------------------------------------------------
#--------------------------------------------------------------------

"""Find the First Non-Repeating Character"""
def first_unique_character(text):

    frequency = {}

    # Step 1: Count each character
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Step 2: Find the first unique character
    for char in text:
        if frequency[char] == 1:
            return char

    return None


word = "aabbcdd"

result = first_unique_character(word)

if result is not None:
    print("First unique character:", result)
else:
    print("No unique character found.")

#---------------------------------------------------------------------
#---------------------------------------------------------------------

"""seperate even and odd numbers"""

def separate_numbers(numbers):
    even_numbers = []
    odd_numbers = []

    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    return even_numbers, odd_numbers


numbers = [12, 7, 9, 4, 6, 3]

even, odd = separate_numbers(numbers)

print("Even numbers:", even)  # [12, 4, 6]
print("Odd numbers:", odd)    # [7, 9, 3]

#-------------------------------------------------------------------
#-------------------------------------------------------------------

""" index of target number"""

def find_positions(numbers, target):
    positions = []

    for index in range(len(numbers)):
        if numbers[index] == target:
            positions.append(index)

    return positions


numbers = [4, 7, 2, 7, 9, 7]

print(find_positions(numbers, 7))   # [1, 3, 5]
print(find_positions(numbers, 10))  # []

#----------------------------------------------------------------
#----------------------------------------------------------------

"""adds the individual digits of an integer"""

def sum_digits(number):
    total = 0

    # Remove the negative sign, if there is one.
    number = abs(number)

    for digit in str(number):
        total += int(digit)

    return total


print(sum_digits(482))   # 14
print(sum_digits(-305))  # 8
print(sum_digits(0))     # 

#----------------------------------------------------------------
#----------------------------------------------------------------

"""names of students above average score"""

def above_average(scores):
    if not scores:
        return []

    total = 0

    for score in scores.values():
        total += score

    average = total / len(scores)

    selected_students = []

    for name, score in scores.items():
        if score > average:
            selected_students.append(name)

    return selected_students


scores = {
    "Alice": 80,
    "Bob": 60,
    "Mary": 90,
    "David": 50
}

print(above_average(scores))  # ['Alice', 'Mary']
print(above_average({}))      # []

#-------------------------------------------------------------------
#-------------------------------------------------------------------

"""replace every matching word"""

def replace_word(sentence, old_word, new_word):
    words = sentence.split()
    updated_words = []

    for word in words:
        if word == old_word:
            updated_words.append(new_word)
        else:
            updated_words.append(word)

    return " ".join(updated_words)


sentence = "I like Java and Java is useful"

result = replace_word(sentence, "Java", "Python")

print(result)
# I like Python and Python is useful

#-------------------------------------------------------------------
#-------------------------------------------------------------------

"""combine two stock dictionaries"""

def combine_stock(first_shop, second_shop):
    combined = {}

    for item, quantity in first_shop.items():
        combined[item] = quantity

    for item, quantity in second_shop.items():
        if item in combined:
            combined[item] += quantity
        else:
            combined[item] = quantity

    return combined


first_shop = {
    "books": 10,
    "pens": 20
}

second_shop = {
    "pens": 15,
    "bags": 5
}

print(combine_stock(first_shop, second_shop))
# {'books': 10, 'pens': 35, 'bags': 5}

#--------------------------------------------------------------------
#--------------------------------------------------------------------

def fib(n):
    """Write Fibonacci series up to n."""
    a, b = 0, 1
    # while a < n:  
    for i in range(n):

        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """Return Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    # while a <= n:
    for i in range(n):
        result.append(a)
        a, b = b, a+b
    return result

fib(10)

numbers = fib2(20)

print(numbers)