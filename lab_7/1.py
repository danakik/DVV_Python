class Point3D:
    instances = []
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        Point3D.instances.append(self)

    def __str__(self):
        if hasattr(self, 'z'):
            return f'({self.x}, {self.y}, {self.z})'
        else:
            return f'({self.x}, {self.y})'
    
    def swap(self):
        self.x, self.y = self.y, self.x 

    @classmethod
    def remove_z(cls):
        for instance in cls.instances:
            del instance.z



point1 = Point3D(1, 2, 3)
point2 = Point3D(4, 5, 6)
point3 = Point3D(-1, -2, -3)
print(point1)
print(point2)
print(point3)

print('change:')
print(point3)
point3.x = 4
print(point3)

print('del:')
print(point1)
print(point2)
print(point3)
Point3D.remove_z()
print(point1)
print(point2)
print(point3)

print('Swap:')
print(point1)
point1.swap()
print(point1)

