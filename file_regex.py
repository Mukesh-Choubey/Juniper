# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:41:55 2020

@author: mchoubey
"""

import re
hosts = open ('C:/Users/mchoubey/Desktop/rsvp')
content = hosts.read()
#print(content)
print(hosts.tell())
regex = re.compile(r'\b 452')
x = regex.findall(content)
#print(x)
#regex = re.compile(r'\b 452\w+')
#x = re.findall(r'lsp', content)
#x = re.search(r"43\w+", content)
#print(x.group())
for line in content:
    if re.search(r"Jun 11 08:07:05.779080", line) != 'None':
        print(line, end = '')
        
#print(re.search(r"DEAD", content))


#print(x)






















hosts.close()