# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 13:27:16 2020

@author: mchoubey
"""

import string
from random import choice
from random import randint
##List of first names
first_names = ['Jon', 'Rick', 'Ben', 'Vishal', 'Bill']
last_names = ['Singh', 'Pandey', 'Jones', 'Patel', 'Shah']
services = ['gmail', 'yahoo', 'rediffmail', 'outlook']
for x in range(100):
    first, last = choice(first_names), choice(last_names)
    random_name = f'{first} {last}'
    service = choice(services)
    mail = f'{first.lower()}.{last.lower()}@{service}.com'
    phone = f'{randint(1,9)}{randint(0,9)}{randint(0,9)}-{randint(0,9)}{randint(0,9)}{randint(0,9)}-{randint(0,9)}{randint(0,9)}{randint(0,9)}{randint(0,9)}'
  
    print(f'{random_name}:-Email:-{mail} Phone:- {phone}')

    
