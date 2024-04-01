import numpy as np

array = np.random.randint(0, 100, size=(4, 6))


print("Масив:")
print(array)
print("\nСума всіх елементів у масиві:", np.sum(array))
print("Мінімальне значення у масиві:", np.min(array))
print("\nВідсортований масив:")
print(np.sort(array, axis=None))
print("\nСереднє значення елементів у масиві:", np.mean(array))
