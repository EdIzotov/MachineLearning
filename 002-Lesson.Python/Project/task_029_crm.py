crm = list()

while True:
    commands = input().split()
    command = commands[0]
    name = None
    if command != "list" and command != "stop":
        name = str(commands[1])
    if command == "add":
        crm.append(name)
    elif command == "find":
        result = None
        for i in range(len(crm)):
            if crm[i] == name:
                result = crm[i]
        print(result)
    elif command == "list":
        print(crm)
    elif command == "stop":
        break
    else:
        print("Command not found")
