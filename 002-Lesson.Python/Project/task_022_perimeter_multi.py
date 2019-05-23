import math

multi = int(input("Input number: "))
x0 = 0
y0 = 0
x1 = 0
y1 = 0
length = 0

for i in range(multi):
    x2 = int(input("Input X" + str(i + 1) + " : "))
    y2 = int(input("Input Y" + str(i + 1) + " : "))
    if i == 0:
        x0 = x1 = x2
        y0 = y1 = y2
        continue

    length += math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
    x1 = x2
    y1 = y2
    if i == (multi - 1):
        length += math.sqrt(math.pow((x2 - x0), 2) + math.pow((y2 - y0), 2))


print(length)
