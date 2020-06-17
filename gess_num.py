# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 10:22:03 2020

@author: mchoubey
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 10:12:57 2020

@author: mchoubey
"""

import random
number = random.randint(1, 100)
print(number)

def run_game():
    
    print("I'm thinking of a number between 1 and 100")
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess == number:
            print("That's right!")
            break
        elif number < guess:
            print("Lower")
        else:
            print("Higher")
 
run_game()