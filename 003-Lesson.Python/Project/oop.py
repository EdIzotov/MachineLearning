import math


def calc_area(radius):
    area = math.pi * radius ** 2
    return area


circles = [1, 5]
circles2 = [(1, 0, 1), (0, 1, 5)]  # (x, y, r)
for circle in circles:
    print(calc_area(circle))
