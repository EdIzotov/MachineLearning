number = int(input("Input q-ty numbers: "))


def get_numbers(n):
    nums = []
    for i in range(n):
        nums.append(int(input("Input number: ")))
    return nums


numbers = get_numbers(number)
numbers_sorted = sorted(numbers)

for index in range(len(numbers_sorted)):
    if index == 0:
        if not numbers_sorted[index] == numbers_sorted[index + 1]:
            print(numbers_sorted[index])
            continue
    elif index == len(numbers_sorted) - 1:
        if not numbers_sorted[index] == numbers_sorted[index - 1]:
            print(numbers_sorted[index])
            continue
    if not (numbers_sorted[index] == numbers_sorted[index - 1] or numbers_sorted[index] == numbers_sorted[index + 1]):
        print(numbers_sorted[index])
