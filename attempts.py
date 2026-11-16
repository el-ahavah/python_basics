# def find_largest(numbers):
#     largest = numbers[0]
#     for number in numbers:

#         if numbers == []:
#            return None

#         if number > largest:
#             largest = number
#     return largest

# def main():
#     numbers = [3, 41, 56, 21, 76, 9]
#     output = find_largest(numbers)
#     print(output)

# main()

#------------------------------------------------------------

# def find_smallest(numbers):
#     smallest = numbers[0]
#     for number in numbers:

#         if numbers == []:
#             return None

#         if number < smallest:
#             smallest = number
#     return smallest

# def main():
#     numbers = [-3, -10, -1, -6]

#     output = find_smallest(numbers)
#     print(output)

# main()

#------------------------------------------------------------

# """sum of numbers"""
# def list_sum(numbers):
#     sum = 0
#     for number in numbers:
#         if numbers == []:
#             return None
#         sum += number
#     return sum
    
# def main():
#     numbers = [2, 4, 6, 8]
#     sum = list_sum(numbers)
#     print(sum)

# main()

#------------------------------------------------------------

# """ count even numbers"""
# def count_even(numbers):
#     count = 0
#     for number in numbers:

#         if number % 2 == 0:
#             count += 1

#     return count

# def main():
#     numbers = [1, 2, 3, 4, 6]
#     count = count_even(numbers)
#     print(count)

# main()

#------------------------------------------------------------

# """Count Occurrences"""
# def count_occurrences(numbers, target):
#     count = 0
#     for number in numbers:
#         if number == target:
#             count += 1
#     return count

# def main():
#     numbers = [2, 5, 2, 8, 2]
#     target = 2
#     output = count_occurrences(numbers, target)
#     print(output)

# main()

#------------------------------------------------------------

# """Find a Number in a List"""
# def find_number(numbers, target):
#     for i in range(len(numbers)):
#         if numbers[i] == target:
#             return i
#     return -1

# def main():
#     numbers = [10, 25, 30, 45]
#     target = 30
#     output = find_number(numbers, target)
#     print(output)

# main()

#------------------------------------------------------------

"""Reverse a List"""

# def reverse_list(items):
#     result = []

#     for i in range(len(items) - 1, -1, -1):
#         result.append(items[i])

#     return result





# def reverse_list(items):
#     result = []
#     i = len(items) - 1

#     while i >= 0:
#         result.append(items[i])
#         i -= 1

#     return result





# def reverse_list(items):
#     result = []

#     left = 0
#     right = len(items) - 1

#     while right >= left:
#         result.append(items[right])
#         right -= 1

#     return result

# def main():
#     items = [1, 2, 3, 4]
#     result = reverse_list(items)
#     print(result)

# main()

#------------------------------------------------------------

"""Check if a List Contains Duplicates"""

def has_duplicates(numbers):
    store = dict()

    for number in numbers:
        if number in store:
            return True

        store[number] = True

    return False


# def has_duplicates(numbers):
#     store = set()

#     for number in numbers:
#         if number in store:
#             return True

#         store.add(number)

#     return False

def main():
    numbers = [1, 2, 3, 4, 2]
    output = has_duplicates(numbers)
    print(output)

main()