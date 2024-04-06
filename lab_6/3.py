import numpy as np
import matplotlib.pyplot as plt

x1 = list(range(0, 11))  
y1 = [x**np.cos(x**2) for x in x1]

x2 = list(range(0, 9)) 
y2 = [5 * np.sin(10 * x) * np.sin(3 * x) / x**x for x in x2]

plt.plot(x1, y1, label='x=[1,10]', color='red')
plt.plot(x2, y2, label='x=[0,8]', color='blue')

plt.xlabel('X')
plt.ylabel('Y')
plt.title('граіфки математичних функції')
plt.legend()
plt.show()

plt.subplot(2, 1, 1)
plt.plot(x1, y1, label='x=[1,10]', color='red')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Графіки математичних функцій')
plt.legend()


plt.subplot(2, 1, 2)
plt.plot(x2, y2, label='x=[0,8]', color='blue')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()

plt.tight_layout()  
plt.show()