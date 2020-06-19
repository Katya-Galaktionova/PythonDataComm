#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a program the prompts the user for  number between 1 and 59.
Use time to get the current second.
Pass the users guess to a function.
That function will compare to the current second.  If correct exit the program.
If incorrect, give them 5 attempts to guess.
"""
from time import strftime

def GUESS_SECOND():
    ATTEMPT = 0
    while ATTEMPT < 5:
        GUESS = int(input("Enter a number between 0 and 59: "))
        if GUESS == strftime("%S"):
            print("You win")
            break
        else:
            print("Your guess is incorrect")
            ATTEMPT += 1
GUESS_SECOND()
