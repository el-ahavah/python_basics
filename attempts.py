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

def list_sum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum
    
def main():
    numbers = [2, 4, 6, 8]
    sum = list_sum(numbers)
    print(sum)

main()