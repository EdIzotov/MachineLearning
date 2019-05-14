n = int(input("Input q-ty of numbers: "))

max_number = 0
for i in range(n):
    number = int(input("Input " + str(i + 1) + "th number: "))
    if number > max_number:
        max_number = number

print(max_number)
