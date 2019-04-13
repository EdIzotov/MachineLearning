def detect_triangle(a, b, c):
    if a == b == c:
        print("The triangle is Equilateral")
    elif a == b or a == c or b == c:
        print("The triangle is Isosceles")
    else:
        print("The triangle is Common")


side1 = int(input("Input side 1 of triangle: "))
side2 = int(input("Input side 2 of triangle: "))
side3 = int(input("Input side 3 of triangle: "))
detect_triangle(side1, side2, side3)
