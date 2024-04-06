import matplotlib.pyplot as plt

labels = ['Полісся', 'Грант', 'Міріса', 'AT trading', 'Trabe F']
sizes = [10, 45, 19, 11, 15] 
colors = ['red', 'green', 'blue', 'yellow', 'orange']

explode = (0.1, 0, 0, 0, 0)

plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', explode=explode)
plt.title('Валовий дохід підприємств')
plt.axis('equal')
plt.savefig('5.png')
plt.show()

