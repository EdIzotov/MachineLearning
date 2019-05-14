sign = input("Input + or *:")
n = int(input("Input q-ty of numbers: "))

number = 0

if sign == "*":
    number = 1

for i in range(n):
    x = int(input("Input " + str(i + 1) + "th number: "))
    if sign == "+":
        number += x
    elif sign == "*":
        number *= x
    else:
        print("INCORRECT SIGN!")
        break
else:
    print(number)
