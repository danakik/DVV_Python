import numpy as np

class Circle:
    def __init__(self, r):
        self.r = r
    
    def sqare(self):
        return np.pi * self.r ** 2
    
    def length(self):
        return 2 * np.pi * self.r

    def __str__(self):
        return f'sqare: {round(self.sqare(), 2)}, length: {round(self.length(), 2)}'
    

kolo1 = Circle(5)
print(kolo1)


    