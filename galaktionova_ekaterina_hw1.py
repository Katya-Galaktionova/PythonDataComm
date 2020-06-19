'''
Galaktionova Ekaterina Python HW1
'''
#1.1
from random import randint
NUMBER = randint(1, 20)
GUESS = int(input("Enter a number: "))
if GUESS > 20 or GUESS < 0:
    print("It is out of range")
elif GUESS < NUMBER:
    print("That is less")
elif GUESS > NUMBER:
    print("That in higher")



#1.2
GAME_NAME = input("What game do you want to play?: ")
while GAME_NAME.lower() != "chess":
    print("Wouldn't you prefer playing Chess?")
    GAME_NAME = input("What game do you want to play?: ")
    print(GAME_NAME)
else:
    print("What a coincidence! I want to play chess too")


#1.3
NUMBER1 = randint(1, 20)
GUESS1 = 0
ATTEMPT = 0
while NUMBER != GUESS1:
    ATTEMPT += 1
    GUESS1 = int(input("Enter a number: "))
    print(GUESS1)
    if GUESS1 > 20 or GUESS1 < 0:
        print("It is out of range")
    elif GUESS1 < NUMBER1:
        print("That is less")
    elif GUESS1 > NUMBER1:
        print("That in higher")
    elif GUESS1 == NUMBER1:
        if ATTEMPT == 1:
            print("Excellent!")
        elif ATTEMPT > 1 and ATTEMPT < 20:
            print("OK")
        elif ATTEMPT == 20:
            print("Bad")
        break
