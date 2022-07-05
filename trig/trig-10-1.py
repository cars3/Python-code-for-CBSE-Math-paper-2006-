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

#Question 2.4(a)

for x in range(1,91):
    if (np.sin(x) + np.cos(x) / np.sin(x) - np.cos(x)) + (np.sin(x) - np.cos(x) / np.sin(x) + np.cos(x)) == (2 * ((1/np.cos(x))**2) / (np.tan(x))**2 - 1):
        print(f"Q2.4a. When Theta has a value of{x}, then the following case is true")
    else:
        continue