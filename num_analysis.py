# # method 1:
# numbers = input("please input you list of numbers: ")
# numbers = [int(number) for number in numbers.split()]

# start = 0
# counting = 0
# minimum = numbers[0]
# maximum = numbers[0]
# even = []
# odd = []
# positive = []
# negative = []

# for number in numbers:
    
#     if minimum > number:
#         minimum = number

#     if maximum < number:
#         maximum = number

#     if number % 2 == 0:
#         even.append(number)
#     else:
#         odd.append(number)

#     if number > 0:
#         positive.append(number)
#     elif number < 0:
#         negative.append(number)

#     total = start + number
#     start = total
#     counting += 1

# average = total/counting
# print(total)
# print(average)
# print(minimum)
# print(maximum)
# print(even)
# print(odd)
# print(positive)
# print(negative)

#-------------------------------------------------------------------
# method 2 - splitted into functions:

def get_numbers():
    numbers = input("please input your list of numbers: ")
    return [int(number) for number in numbers.split()]


def find_min(numbers):
    minimum = numbers[0]
    for number in numbers:
        if minimum > number:
            minimum = number
    return minimum


def find_max(numbers):
    maximum = numbers[0]
    for number in numbers:
        if maximum < number:
            maximum = number
    return maximum


def split_even_odd(numbers):
    even = []
    odd = []
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)
    return even, odd


def split_positive_negative(numbers):
    positive = []
    negative = []
    for number in numbers:
        if number > 0:
            positive.append(number)
        else:
            negative.append(number)
    return positive, negative


def total_and_average(numbers):
    start = 0
    counting = 0
    for number in numbers:
        total = start + number
        start = total
        counting += 1
    average = total / counting
    return total, average


def main():
    numbers = get_numbers()

    minimum = find_min(numbers)
    maximum = find_max(numbers)
    even, odd = split_even_odd(numbers)
    positive, negative = split_positive_negative(numbers)
    total, average = total_and_average(numbers)

    print("total:", total)
    print("average:", average)
    print("minimum:", minimum)
    print("maximum:", maximum)
    print("even:", even)
    print("odd:", odd)
    print("positive:", positive)
    print("negative:", negative)


main()