# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:52:08 2020

@author: mchoubey
"""

try:
    def ip(a='172', b='16', c='254', d='1'):
        if (a.isdigit and len(a) ==3 and int(a) <= 255):
            
            print (f"Your ip address is:-{a}.{b}.{c}.{d}")
        else: raise ValueError("Enter carefully")               
except ValueError:
        raise ValueError("ValueError thrown")        
#ip()
#ip(a='123')    
ip(a='100', b='255', c='876', d='8')