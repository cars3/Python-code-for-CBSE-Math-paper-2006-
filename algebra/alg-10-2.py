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


#Question 1.1b
x_y = []
for x in range(1,100):
    for y in range(1,100):
        a = -y
        b = x
        if (a*x/b) - (b*y/a) == a + b:
            if a*x - b*y == 2*a*b:
                x_y.append((x,y))
print(f" For Q1.1b) Here these equations are possible with following values of x and y {x_y}")