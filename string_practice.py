# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 11:13:53 2020

@author: mchoubey
"""
x = 'hello world !'
print(x[0:5])
print(x[:])
print(len(x))
###Reverse the string
print(x[::-1])
###Count number of ls in string
print(x.count('l'))

####Iterate over string, two lines
for a in x:
#    print(a)
    print(a, end='\n \n')

###Print with space in stead of new line
for a in x:
    print(a, end=' ')
    
###Using enumerate, index
for index, char in enumerate(x):
    print(index, char)
 
####r string to avoid special character     
path = 'c:\neon\example'    
part = r'c:\neon\example'
print(part, path, part.upper())

##Chaining of funtion
poem = """ This is a poem
of nothing"""
new = poem.capitalize().upper()
print(new)
print([x for x in poem])
#####Join function in between characters
char = 'abc'
print(' '.join(char))
print('<<<>>> '.join(char))

import string
char = 'Z'
print(char in string.ascii_letters)
