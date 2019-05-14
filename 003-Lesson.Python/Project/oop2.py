import math


class Circle:
    def __init__(self, x, y, r):
        self.x_coordinate = x
        self.y_coordinate = y
        self.radius = r

    def calculate_area(self):
        area = math.pi * self.radius ** 2
        return area


class Sphere(Circle):
    def __init__(self, x, y, z, r):
        super().__init__(x, y, r)
        self.z_coordinate = z

    def calculate_area(self):
        area = 4 * math.pi * self.radius ** 2
        return area


s = Sphere(1, 1, 1, 1)
print(s.y_coordinate)
print(s.calculate_area())

c = Circle(1, 0, 1)
print(c.radius)
