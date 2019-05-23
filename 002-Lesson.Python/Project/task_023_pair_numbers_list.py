number = int(input("Input number: "))


def get_numbers(n):
    nums = []
    for i in range(n):
        nums.append(int(input("Input number: ")))
    return nums


def get_slice(collection, start, end):
    step = 1
    if end < start:
        step = -1
    return collection[start:end:step]


numbers = get_numbers(number)

while True:
    a = int(input("Input start number: "))
    b = int(input("Input end number: "))
    print(numbers)
    if a == 0 and b == 0:
        break
    print(get_slice(numbers, a, b))
