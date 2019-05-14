emails = set()
while True:
    e = input("Input email: ")
    if e in emails:
        print("The email already exists!")
    else:
        emails.add(e)

