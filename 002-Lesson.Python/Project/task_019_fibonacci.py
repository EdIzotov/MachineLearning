fibonacci_number = int(input("Input number: "))


def fibonacci(number):
    start = 0
    print(start)
    for i in range(number):
        start += i + 1
        print(start)


fibonacci(fibonacci_number)
#