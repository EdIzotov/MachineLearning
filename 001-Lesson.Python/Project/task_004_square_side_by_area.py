import math


def square_side(area):
    return math.sqrt(area)


square_area = int(input("Input square area: "))
print("The side of the square is " + str(square_side(square_area)))
