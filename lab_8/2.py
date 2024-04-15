class Car:
    def __init__(self, m, mod, r):
        self.marka = m
        self.model = mod
        self.r = r
        self.v = 0

    def accelerate(self):
        self.v += 10

    def brake(self):
        self.v -= 10

    def get_speed(self):
        print(self.v)

car1 = Car('BMW', 'A8', '2010')
car1.get_speed()
car1.accelerate()
car1.get_speed()
car1.accelerate()
car1.get_speed()
car1.brake()
car1.get_speed()
    
