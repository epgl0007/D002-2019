def printer(secret, opened):
    i = 0
    while i < len(secret):
        if secret == opened[i]:
            printer.append(_)
        i = i + 1
        print(i, end="")

printer("apple", [1, 2])
printer("orange", [0, 5])
printer("cat", [])
#secret = %d opened = [] _
