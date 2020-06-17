# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 11:26:37 2020

@author: mchoubey
"""

try:
    a = int(input("Enter an integer :-"))
    raise Exception("Something  strange")
except ValueError as err:
    print("Something", err.with_traceback)