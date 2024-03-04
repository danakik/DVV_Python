m = int(input('friends: '))
n = int(input('money: '))

n = n + (n / 100 * 15)

print(f'all: {n}, each: {n / m}')