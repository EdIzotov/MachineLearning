sign = input("Input + or *: ")
n = int(input("Input q-ty of numbers: "))

number = 0

if sign == "*":
    number = 1

for i in range(n):
    print(sign != "+")
    print(sign != "*")
    if not (sign == "+" or sign == "*"):
        print("INCORRECT SIGN!")
        break
    x = int(input("Input " + str(i + 1) + "th number: "))
    if sign == "+":
        number += x
    elif sign == "*":
        number *= x
else:
    print(number)
