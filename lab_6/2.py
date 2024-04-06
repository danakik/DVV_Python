import matplotlib.pyplot as plt
import numpy as np

x = list(range(-6, 7))  


y1 = [np.abs(x) for x in x]
y2 = [x**3 for x in x]
y3 = [0.5 * x for x in x]

plt.plot(x, y1, label='|x|', color='red')
plt.plot(x, y2, label='$x^3$', color='yellow')
plt.plot(x, y3, label='$\\frac{1}{2}x$', color='green')

plt.xlabel('X', fontsize=16, color='red')
plt.ylabel('Y', fontsize=16, color='red')
plt.title('граіфки математичних функції', fontsize=16, color='blue')

plt.legend(loc='lower right', fontsize=14)

plt.savefig('2.png')

plt.show()
