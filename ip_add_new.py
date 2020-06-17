# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:47:24 2020

@author: mchoubey
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:52:54 2020

@author: mchoubey
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 16:35:15 2020

@author: mchoubey
"""
"""
Has default parameters of a='172', b='16', c='254', d='1'
 'a' must be exactly length of 3 and contains ONLY strings of digits
'b' must be exactly length 2 and contains ONLY strings of digits
'c' must be exactly length 3 and contains ONLY strings of digits
'd' must be exactly length 1 and contains ONLY strings of digits
If any of the following conditions are invalid then a ValueError() exception will be raised.
Research how to raise a ValueError
"""

try:
    def ip(a='172', b='16', c='254', d='1'):
        if (a.isdigit and len(a) ==3 and int(a) <= 255) and (b.isdigit and len(b) == 2) and (c.isdigit and len(c) == 3 and int(c) <= 254) and (d.isdigit and len(d) == 1):
            print (f"Your ip address is:-{a}.{b}.{c}.{d}")
        else: raise ValueError("Enter carefully")               
except ValueError:
        raise ValueError("ValueError thrown")        
#ip()
#ip(a='123')    
ip(a='100', b='255', c='876', d='8')
#ip(a='123', b='18', c='220', d='2')