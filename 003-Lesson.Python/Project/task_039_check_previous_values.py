values = set()
while True:
    v = int(input("Input number: "))
    if v in values:
        print("The value already exists!")
    else:
        values.add(v)
