number_n = int(input("Input N numbers: "))


def get_numbers(n):
    nums = []
    for i in range(n):
        nums.append(int(input("Input number: ")))
    return nums


numbers_n = get_numbers(number_n)
number_m = int(input("Input M numbers: "))
numbers_m = get_numbers(number_m)

duplicate_numbers = list(set(numbers_n) & set(numbers_m))

print(duplicate_numbers)
