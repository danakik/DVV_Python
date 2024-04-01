import numpy as np

a = np.random.randint(0, 10, (1, 15))
num = np.mean(a)
num = round(num, 3)
x = a - num

with open('lab_5/2.csv', 'w', encoding='utf-8') as f:
    f.write(f'Масив: {a},\n Середю : {num},\n {(x)}')

