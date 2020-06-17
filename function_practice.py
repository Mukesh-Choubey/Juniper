# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 14:35:21 2020

@author: mchoubey
"""
def f(x):
    """
    This function double the value
    """
    x = 2 * x
    print(x)
f(10)
print(f.__doc__)

###With return
def f1(x):
    """
    This function double the value
    """
    x = 2 * x
    return(x)
    
print(f1(200))

####Variable arguments in function
def f2(*args):
    count = 0
    for i in args:
        count += i
    return(count)
    
count = f2(10, 20, 30)
print(count)
    
######With default
def f3(x=2, y=10):
    return(x+y)
    
print(f3(20, 10))
print(f3(10))

###With ** we can pass in keyword arguments
def f4(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
        
f4(a=10, b=20, c=100)

#### Mutiply finction
def mul(*x):
    result = 1
    for i in x:
        result = result * i
        print(result)
        
mul(10, 20)
mul(10, 30, 30)

###Isinstance used to check variable type    
def fun(*arga):
    for x in arga:
        if isinstance(x, int):
            print(f"Integer {x}")
        else:    
            print(f"not int {x}")
            

fun(10, 20, 'hello')


    
