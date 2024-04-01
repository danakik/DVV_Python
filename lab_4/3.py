def sort(line):
    numbers = [int(num) for num in line.split()]
    sorted_numbers = sorted(numbers)
    return ', '.join(map(str, sorted_numbers))

def find_index(line, number):
    numbers = [int(num) for num in line.split()]
    index = numbers.index(number)
    return f"Index of {number}: {index+1}"

def min_numbers(line):
    numbers = [int(num) for num in line.split()]
    sorted_numbers = sorted(numbers)
    first_five_min = sorted_numbers[:5]
    return "First five minimum numbers: " + ', '.join(map(str, first_five_min))

def average(line):
    numbers = [int(num) for num in line.split()]
    average = sum(numbers) / len(numbers)
    return f"Average: {average}"

def tam_net_dva(line):
    numbers = [int(num) for num in line.split()]
    unique_numbers = list(set(numbers))
    return "Unique numbers: " + ', '.join(map(str, unique_numbers))

filename = '3.txt'

with open(filename, 'r') as file:
    lines = file.readlines()


with open(filename, 'a') as file:
    result = sort(lines[0])
    file.write(f'Task 1: {result}\n')


with open(filename, 'a') as file:
    result = find_index(lines[1], 5)
    file.write(f'Task 2: {result}\n')


with open(filename, 'a') as file:
    result = min_numbers(lines[2])
    file.write(f'Task 3: {result}\n')


with open(filename, 'a') as file:
    result = average(lines[3])
    file.write(f'Task 4: {result}\n')


with open(filename, 'a') as file:
    result = tam_net_dva(lines[4])
    file.write(f'Task 5: {result}\n')
