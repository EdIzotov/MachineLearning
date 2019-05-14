import math


class Circle:
    def __init__(self, x, y, r):
        self._x_coordinate = x
        self._y_coordinate = y
        self.__radius = r

    def calculate_area(self):
        area = math.pi * self.radius ** 2
        return area


c = Circle(1, 0, 1)
print(c._Circle__radius)
