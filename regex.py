# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 12:36:10 2020

@author: mchoubey
"""

import re
txt = "The rain in Spain Spain Spain"
print(re.findall(r'Spain', txt))
print(re.sub(r'Spain', 'London', txt))
print(txt)
###Below replaces Spain with London for first 2 occurances
print(re.sub(r'Spain', 'London', txt, 2))

####Below prints complete string where match
x = re.search(r"\bS\w+", txt)
print(x.group())
print(x.end())