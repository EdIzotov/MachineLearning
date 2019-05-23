number = int(input("Input q-ty numbers: "))


def get_numbers(n):
    nums = []
    for i in range(n):
        nums.append(int(input("Input number: ")))
    return nums


numbers = get_numbers(number)


for index in range(len(numbers)):
    if index == 0 or index == (len(numbers) - 1):
        continue
    if numbers[index - 1] < numbers[index] > numbers[index + 1]:
        print(numbers[index])
