# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 10:12:57 2020

@author: mchoubey
"""

import random


def run_game():
    number = random.randint(1, 20)

    print("I'm thinking of a number between 1 and 20")
    print('You have 4 guesses left')

    guess = int(input("Guess a number: "))
    if guess == number:
        print("That's right!")
        return
    elif number < guess:
        print("Lower")
    else:
        print("Higher")

    print('You have 3 guesses left')
    guess = int(input("Guess a number: "))
    if guess == number:
        print("That's right!")
        return
    elif number < guess:
        print("Lower")
    else:
        print("Higher")

    print('You have 2 guesses left')
    guess = int(input("Guess a number: "))
    if guess == number:
        print("That's right!")
        return
    elif number < guess:
        print("Lower")
    else:
        print("Higher")

    print('You have 1 guess left')
    guess = int(input("Guess a number: "))
    if guess == number:
        print("That's right!")
        return
    print("Nope! It was " + str(number))


run_game()