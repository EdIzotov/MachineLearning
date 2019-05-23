start_celsium_number = int(input("Input start celsium number: "))
end_celsium_number = int(input("Input end celsium number: "))
step_celsium = float(input("Input step number: "))


def celsium_farenheit_table_while(start, end, step):
    t = start
    while t < end:
        f = (t * 9 / 5) + 32
        print(str(t) + "\t\t" + str(f))
        t += step


celsium_farenheit_table_while(start_celsium_number, end_celsium_number, step_celsium)
