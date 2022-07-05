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

#Question 1.5

a6 = -10
a10 = -26
a15 = 0

d = int((a10 - a6)/4)

# a6 = a + 5d

a = a6 - 5*d
print(a)

a15 = a + (15 - 1)*d

print(f"Q1.5. in this AP, a15 is {a15}")