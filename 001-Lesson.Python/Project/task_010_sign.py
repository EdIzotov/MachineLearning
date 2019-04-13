def sign(number):
    if number < 0:
        return -1
    elif number == 0:
        return 0
    elif number > 0:
        return 1


a = int(input("Input number1: "))
print("Number sign is " + str(sign(a)))
