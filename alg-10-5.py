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

#Question 1.4a

aa= 2
bb = 3

#eq 12abx2 − 9a2 − 8b2 ·x−6ab
a = 12*aa*bb
b = - (9*aa^2 - 8*bb^2)
c = -6*aa*bb

d = (b**2) - (4*a*c)


sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print(f"Q1.4a The 2 solutions of this equation are {sol1} x -a/b and {sol2} x -b/a")