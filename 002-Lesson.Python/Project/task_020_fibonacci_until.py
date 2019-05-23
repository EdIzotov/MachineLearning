fibonacci_number = int(input("Input number: "))


def fibonacci(number):
    n1 = 0
    n2 = 1
    if number <= 0:
        print("Input a positive number!")
    elif number == 1:
        print(n1)
    else:
        for i in range(number):
            if n1 > number:
                break
            print(n1)
            ntn = n1 + n2
            n1 = n2
            n2 = ntn


fibonacci(fibonacci_number)
