def previous_number(a):
    return a - 1


def next_number(a):
    return a + 1


number = int(input("Input number: "))
print("The next number for the number " + str(number) + " is " + str(next_number(number)))
print("The previous number for the number " + str(number) + " is " + str(previous_number(number)))
