import numpy as np

a = np.random.randint(0, 10, (1, 20))
x = a.reshape(4, 5)
x_plus_10 = x + 10

with open('lab_5/3.csv', 'w', encoding='utf-8') as f:
    f.write('Масив 1, Масив 2\n')
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            f.write(f"{a[0, i * x.shape[1] + j]}, {x_plus_10[i, j]}\n")

