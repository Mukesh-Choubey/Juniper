# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:35:58 2020

@author: mchoubey
"""
import re
hosts = open ('C:/Users/mchoubey/Desktop/rsvp')
content = hosts.read()
#print(content)
print(hosts.tell())
regex = re.compile(r'lsp')
x = regex.search(content)
print(x)