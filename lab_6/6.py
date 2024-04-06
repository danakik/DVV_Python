import matplotlib.pyplot as plt
import numpy as np

categories = ['MS Exele', 'MS Word', 'MS PP']
quarters = ['I', 'II', 'III', 'IV']

sales = [
    [112, 231, 178, 129],
    [187, 195, 118, 148],
    [167, 129, 70, 90]
]

colors = ['green', 'blue', 'orange']

bar_width = 0.2
index = np.arange(len(quarters))

for i, category in enumerate(categories):
    plt.bar(index + i * bar_width, sales[i], bar_width, label=category, color=colors[i])

plt.xlabel('Квартали')
plt.ylabel('Продажі')
plt.title("Об'єми продажу книг в розрізі кварталу")
plt.xticks(index + bar_width, quarters)
plt.legend()
plt.savefig('6.png')
plt.show()
