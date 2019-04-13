a = int(input("Input number1: "))
b = int(input("Input number2: "))

middle = (a + b) / 2
max_n = int(middle + abs(a - b) / 2)
min_n = int(middle - abs(a - b) / 2)
print("Max number is " + str(max_n))
print("Min number is " + str(min_n))
