import numpy as np

cord = np.random.randint(0, 100, size=(10, 3))
x = cord[:, 0]
y = cord[:, 1]
z = cord[:, 1]

radius = np.sqrt(x**2 + y**2 + z**2)
teta = np.arctan((x**2 + y**2) / z)
fi = np.arctan(x / y)

print('Декартові координати:')
print(cord)
print('Полярні координати (pадіальна, кут teta, кут fi):')
for i in range(len(radius)):
    print(f'{radius[i]:.2f}, {teta[i]:.2f}, {fi[i]:.2f}')
