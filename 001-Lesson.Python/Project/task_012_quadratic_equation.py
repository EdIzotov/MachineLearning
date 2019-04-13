import math


def discriminant(a, b, c):
    return math.pow(b, 2) - 4 * a * c


def quadratic(a, b, c):
    discr = discriminant(a, b, c)
    values = {"x1": None, "x2": None}
    if discr < 0:
        return values
    elif discr == 0:
        values["x1"] = -b / 2 * a
    elif discr > 0:
        values["x1"] = (-b + math.sqrt(discr)) / (2 * a)
        values["x2"] = (-b - math.sqrt(discr)) / (2 * a)
    return values


member_a = int(input("Number a: "))
member_b = int(input("Number b: "))
member_c = int(input("Number c: "))

print("Values are: " + str(quadratic(member_a, member_b, member_c)))
