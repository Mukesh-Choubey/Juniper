# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:58:58 2020

@author: mchoubey
"""


def table(table=5):
    tableend = 10*table+1
    for i in range (table, tableend, table):
        times = int(i/table)
        print(f"{table} X {times} = {i}")
num = (int(input("enter the number for which you need table:-")))
table(num)

####Table upto a number
def mul(x=5):
    for x in range(1, x+1):
        for y in range(1, x+1):
            print(f"{x} X {y} = {x*y}")
            
mul(10)