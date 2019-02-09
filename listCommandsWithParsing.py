if __name__ == '__main__':
    N = int(input("\nHow many list commands would you like to run..?\n"))
    list = []

def runCommands():
    a = input("\nWhat is your command..?\n")
    aSplit = a.split()
    if len(aSplit) == 2 or len(aSplit) == 3:
        i = int(aSplit[1])  
    if len(aSplit) == 3:
        e = int(aSplit[2])
    
    if aSplit[0] == "print":
        print(list)
    if aSplit[0] == "sort":
        list.sort()
        print(list)
    if aSplit[0] == "pop":
        list.pop()
        print(list)
    if aSplit[0] == "reverse":
        list.reverse()
        print(list)
    if aSplit[0] == "insert":
        list.insert(i,e)
        print(list)
    if aSplit[0] == "remove":
        list.remove(i)
        print(list)
    if aSplit[0] == "append":
        list.append(i)
        print(list)

for o in range(N):
    runCommands()
