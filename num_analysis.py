
numbers = input("please input you list of numbers: ")
numbers = [int(number) for number in numbers.split()]

start = 0
counting = 0
minimum = numbers[0]
maximum = numbers[0]
even = []
odd = []
positive = []
negative = []

for number in numbers:
    
    if minimum > number:
        minimum = number

    if maximum < number:
        maximum = number

    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

    if number > 0:
        positive.append(number)
    elif number < 0:
        negative.append(number)

    total = start + number
    start = total
    counting += 1

average = total/counting
print(total)
print(average)
print(minimum)
print(maximum)
print(even)
print(odd)
print(positive)
print(negative)