def process_list_commands():
    n = int(input())
    list = []
    for i in range(n):
        command = input()
        if "insert" in command:
            splitStr = command.split(" ")
            list.insert(int(splitStr[1]), int(splitStr[2]))
        elif "print" in command:
            print(list)
        elif "remove" in command:
            splitStr = command.split(" ")
            list.remove(int(splitStr[1]))
        elif "append" in command:
            splitStr = command.split(" ")
            list.append(int(splitStr[1]))
        elif "sort" in command:
            list.sort()
        elif "pop" in command:
            list.pop()
        elif "reverse" in command:
            list.reverse()
        else:
            continue

