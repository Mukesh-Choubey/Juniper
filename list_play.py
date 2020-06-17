# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 11:12:15 2020

@author: mchoubey
"""

x = [1, 2, 3, 4, 5]
print(f"First:- {x[0]} Third :-{x[2]} Fifth:-{x[4]}")
print("First, third and fifth", x[::2])
i = 0
y = len(x)
while i < y:
    print(x[i])
    i += 1
        
for item in x:
    print(item)
