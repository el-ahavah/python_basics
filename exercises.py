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