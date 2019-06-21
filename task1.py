main_list = []
count = int(input("Hom many commands: "))
while count > 0:
    command = input().split()
    print(command)
    if len(command) == 3 and command[0] == "insert":
        main_list.insert(int(command[1]), int(command[2]))
        count -= 1
    elif len(command) == 1 and command[0] == "print":
        print(main_list)
        count -= 1
    elif len(command) == 2 and command[0] == "remove":
        main_list.remove(command[1])
        count -= 1
    elif len(command) == 2 and command[0] == "append":
        main_list.append(int(command[1]))
        count -= 1
    elif len(command) == 1 and command[0] == "sort":
        main_list.sort()
        count -= 1
    elif len(command) == 1 and command[0] == "pop":
        main_list.pop()
        count -= 1
    elif len(command) == 1 and command[0] == "reverse":
        main_list.sort(reverse=True)
        count -= 1
    else:
        print("Error, try again")
