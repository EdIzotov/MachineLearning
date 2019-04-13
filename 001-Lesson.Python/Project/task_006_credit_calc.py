def total_credit(s, percent):
    return s + s / 100 * percent


def diff_credit(s, percent):
    return total_credit(s, percent) - s


credit_sum = int(input("Input credit sum: "))
credit_percent = int(input("Input credit percent: "))
print("The total credit sum with percent is " + str(total_credit(credit_sum, credit_percent)))
print("The difference between total and credit sum is " + str(diff_credit(credit_sum, credit_percent)))
