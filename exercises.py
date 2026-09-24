# numbers = [1, 2, 3, 1]

# seen = []

# for number in numbers:
#     if number in seen:
#         print("Duplicate found")
#         break

#     seen.append(number)
#     # print(seen)
#------------------------------------------
"""reverse"""

# text = "python"
# reversed = text[::-1]

# print(reversed)
#------------------------------------------
"""count number of characters"""

# text = "programming"
# count = 0

# for char in text:
#     count += 1

# print(count)
#------------------------------------------
"""count a's"""

# text = "banana"
# count = 0

# for char in text:
#     if char == "a":
#         count += 1

# print(count)
#------------------------------------------
"""lookup"""

# students = {
#     "David": 85,
#     "John": 72,
#     "Mary": 91,
#     "Sarah": 88
# }

# user_input = input("Enter student: ")
# user_input = user_input.strip()

# if user_input in students:
#     print(students[user_input])
# else:
#     print("invalid student")
#-------------------------------------------
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