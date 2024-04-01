def calculate_function(x):
    return 2 * x - 1

start = -3
end = 3
step = 0.5

with open('1.txt', 'w') as file:
    x = start
    while x <= end:
        y = calculate_function(x)
        file.write(f'{y}\n')
        x += step

