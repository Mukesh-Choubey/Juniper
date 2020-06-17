# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 10:49:49 2020

@author: mchoubey
"""
###Set uses { like dictionary
set1 = {1, 2, 3, 4}

set2 = {3, 4, 5, 6}

#### | is used for union and & for intersection
print(f"intersection is {set1 & set2}")


print(f"union is {set1 | set2}")
x = [1, 1, 2, 3, 2, 4, 5]
###Convert list to set and back to list to remove duplicates
print(list(set(x)))
