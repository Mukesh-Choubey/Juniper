# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 13:42:16 2020

@author: mchoubey
"""

import random
win = 0
while True:
    result = random.choice(['heads', 'tails'])
    toss = input("Heads or tails or done :-")
    if toss == result:
       win += 1
       print("You are correct")
    elif toss == 'done':
        print("Done")
        print(f"you won {win} number of times")
        break
    else:
       print("You are wrong")
