phone_book = {}

while True:
    commands = input().split()
    command = commands[0]
    name = commands[1]
    if command == "insert":
        number = commands[2]
        phone_book[name] = number
    elif command == "delete":
        phone_book.pop(name)
    elif command == "get":
        if name in phone_book:
            print(phone_book[name])
        else:
            print("Not found")
    else:
        print("Command not found")
