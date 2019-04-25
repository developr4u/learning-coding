name = input("Enter your name: ")
lenght = len(name)
i = 0
temp = ""
while lenght > i:
    if name[i] not in temp:
        print(name[i], ":", name.count(name[i]))
        temp += name[i]

    i +=  1
        
        