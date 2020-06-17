# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:55:51 2020

@author: mchoubey
"""
sale = {}
shopping_cart = {
                'beer':['12', '50'],
                'kebab':['10', '40'],
                'wine':['2', '20'],
                'peanuts':['50', '5'],
                'chips':['1', '5']
                 }
print(shopping_cart.keys())
print(shopping_cart.values())
for item, list in shopping_cart.items():
    print(f"Item: {item} : Quantity:-{list[0]} Price:-{list[1]}")
    if int(list[1]) <= 10:
        sale[item] = list[1]
    
print(f"Sale items {sale}")
    
        