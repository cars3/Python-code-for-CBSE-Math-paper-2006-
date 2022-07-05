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

#Question 1.2

x= Symbol('x')

P = 2 /x**2 - x - 6
Q = 3 / x**2 + x - 3
R = 4 / x**2 - 4*x + 3
eq = (P+Q) + R
expr = eq
expr0 = expr.expand()
expr1 = collect(expr0, x)
print(f"Q1.2 The solution of the equation is {expr1}")

