class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def sqare(self):
        s = self.perimeter() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def is_valid(self):
        return self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a


triangle = Triangle(3, 4, 5)


if triangle.is_valid():
    print(f'Perimetr: {triangle.perimeter()}')
    print(f'Sqare: {triangle.sqare()}')
else:
    print('Error critical damage')
