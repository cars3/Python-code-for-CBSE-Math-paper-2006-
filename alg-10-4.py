from numbers import Rational
from re import A, X
from symtable import Symbol
from matplotlib.style import available
import numpy as np
from traitlets import Int
import math
import matplotlib.pyplot as plt
from sympy import solve, Symbol, Eq, Poly , collect
from fractions import Fraction

#Question 1.3

#roots of the equation x = 2,-3
x = [2,-3]
a_val = []
b_val = []

for val in x:
    for a in range(-100,100):
        Px = ((val^2) - (3*val) + 2) * ((2 * val^2)  + (7*val) + a)
        if Px == 0:
            a_val.append((a))

for val1 in x:
    for b in range(-100,100):
        Qx = (val1^2 + 4*val1 + 3) * (3 * val1^2  - 7*val1 + b)
        if Qx == 0:
            b_val.append((b))

print(f"Q1.3 If x = 2, then the values of a,b are {a_val[0]},{b_val[0]} "
      f"If x = -3, then the values of a,b are {a_val[1]},{b_val[1]}")