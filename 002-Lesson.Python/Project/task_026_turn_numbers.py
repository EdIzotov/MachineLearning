number = int(input("Input q-ty numbers: "))


def get_numbers(n):
    nums = []
    for i in range(n):
        nums.append(int(input("Input number: ")))
    return nums


numbers = get_numbers(number)


for num in numbers[::-1]:
    print(num)
