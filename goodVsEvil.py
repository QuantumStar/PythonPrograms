# Original concept and code by Wesley Swafford, 2017
#
# This program generates a random number between 1 and 999,999. If the number is equal to 666, one point is added to the 'evilCount'
# counter. If is is equal to 777, one point is added to the 'goodCount' counter. Whenever either comes up, it is printed to the console,
# and the score is shown. The score is a positive or negative integer, and shows how far 'ahead' one may be. Whichever counter reaches 99
# first is the 'winner', and a message is displayed with the outcome.
#
# The only difference between this version and the 'fast' version is that this has a
# wider range of random numbers (1, 999999). This is so modern computers don't run the program
# so quickly that the process is too fast to see. The 'fast' version is better for the Raspberry Pi
# or microcontrollers running Python. Should be fixed in program, but, I'm not sure how to do that as of now.
#
#

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
