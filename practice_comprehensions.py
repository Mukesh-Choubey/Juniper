# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:13:37 2020

@author: mchoubey
"""

x = [x for x in range(5) for y in range(5)]
print(x)
from random import randint
numbers = [x for x in range(0,21,2)]
randin_ints = []
randin_ints = [randint(1, 100) for i in range(20)]
print(numbers, randin_ints)
from math import factorial

dict = {'a':5, 'b':10, 'c':20}

triple= {k:v**2 for (k, v) in dict.items()}
print(triple)

x = [factorial(x) for x in range(5)]
print(x)
#####Generator uses ( in stead of [
x = (factorial(x) for x in range(5))
print(x)
for i in range(5):
    print(next(x))
    

num1 = [x for x in range(1,10) if x % 2 == 0]
print(num1)    