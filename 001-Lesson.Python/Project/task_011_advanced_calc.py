def calc(a, b, op):
    if op == "+":
        return int(a) + int(b)
    elif op == "-":
        return int(a) - int(b)
    elif op == "*":
        return int(a) * int(b)
    elif op == "/":
        return int(a) / int(b)


num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
operation = input("Input operation: ")
print(calc(num1, num2, operation))
