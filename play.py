# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 09:27:36 2020

@author: mchoubey
"""
try:
    x3 = int(input("What number you want to modulus of:-"))
    x4 = int(input("Divisible by:-"))
    print(f"modulus of {x3} by {x4} is {x3 % x4}")
except ZeroDivisionError as z:
    print(z.args)
finally:
    print("This will alwasys run")
    