# -*- coding: utf-8 -*-
"""
Import the math module.
Assimilate any functionality of the math module into your script.
"""
import math
x = int(input("What number square-root you want:-"))
y = math.sqrt(x)
print(f"Square roof of {x} is :- {y}")

"""
Implement the raise to the power functionality using **
"""
x1 = int(input("What number you want to raise:-"))
x2 = int(input("Raise to power:-:-"))
print(f"{x1} raised to power {x2} is {x1 ** x2}")

"""
Implement the modulus functionality using %
"""
x3 = int(input("What number you want to modulus of:-"))
x4 = int(input("Divisible by:-"))
print(f"modulus of {x3} by {x4} is {x3 % x4}")
