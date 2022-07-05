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

#Question 2.4(b)

x = 60 # = theta
ans_1 = (1/np.cos(90 - x) * 1/np.cos(90 - x)) - (1/np.tan(x) * 1/np.tan(x)) 
ans_2 = (2 * np.cos(60) * np.cos(60)) / 3*((1/np.cos(43) * 1/np.cos(43)) - (1/np.tan(47) * 1/np.tan(47)) )
print(f"Q2.4b The sum of this equation is {ans_1 + ans_2}")