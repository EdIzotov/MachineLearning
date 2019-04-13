import math


def triangle_square(a, b, c):
    half_p = (a + b + c) / 2
    return math.sqrt(half_p * (half_p - a) * (half_p - b) * (half_p - c))


def triangle_perimeter(a, b, c):
    return a + b + c


side1 = int(input("Input side 1 of triangle: "))
side2 = int(input("Input side 2 of triangle: "))
side3 = int(input("Input side 3 of triangle: "))
print("The triangle perimeter is " + str(triangle_perimeter(side1, side2, side3)))
print("The triangle square is " + str(triangle_square(side1, side2, side3)))
