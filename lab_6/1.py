import matplotlib.pyplot as plt

x = list(range(-10, 11))  
y = [x + 2 for x in x] 

plt.plot(x, y, label='(x, x + 2)')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graph')
plt.grid(True)
plt.legend()
plt.show()
