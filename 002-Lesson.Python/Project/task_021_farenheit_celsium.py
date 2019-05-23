start_celsium_number = int(input("Input start celsium number: "))
end_celsium_number = int(input("Input end celsium number: "))
step_celsium = int(input("Input step number: "))


def celsium_farenheit_table(start, end, step):
    for i in range(start, end, step):
        far = (i * 9 / 5) + 32
        print(str(i) + "\t\t" + str(far))


celsium_farenheit_table(start_celsium_number, end_celsium_number, step_celsium)
