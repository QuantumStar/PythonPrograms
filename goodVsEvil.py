import random
    
good = 777
evil = 666

goodCount = 0
evilCount = 0

number = 0

while goodCount < 99 or evilCount < 99:
    number = random.randint(1, 999999)
    if number == 666:
        evilCount += 1
        print("Evil grows stronger....   " + str(evilCount - goodCount))
        if evilCount == 99:
            print("\nEvil has covered the land, and filled the hearts of men with darkness forever more...\n")
            exit()
    if number == 777:
        goodCount += 1
        print("Good is prevailing...!   " + str(goodCount - evilCount))
        if goodCount == 99:
            print("\nGood has triumphed over Evil, peace will reign for a thousand years...!\n")
            exit()

    

