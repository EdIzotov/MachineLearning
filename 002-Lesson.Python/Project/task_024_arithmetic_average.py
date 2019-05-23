import statistics as st


number = int(input("Input q-ty numbers: "))


def get_numbers(n):
    nums = []
    for i in range(n):
        nums.append(int(input("Input number: ")))
    return nums


numbers = get_numbers(number)
ar_ave = st.mean(numbers)

for index in range(len(numbers)):
    if numbers[index] > ar_ave:
        print(str(numbers[index]) + " > " + str(ar_ave))
    elif numbers[index] < ar_ave:
        print(str(numbers[index]) + " < " + str(ar_ave))
    elif numbers[index] == ar_ave:
        print(str(numbers[index]) + " = " + str(ar_ave))
