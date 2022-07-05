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

#Question 2.3

x = 1
r = 2
h = 3

#vol = (22/7) * (r* (x)^2) * (h*x)  
ratio = np.cbrt(1617/(r*h*(x^3)*22/7))

TSA = 2*(22/7)*r*ratio*((h*ratio)+(r*ratio))
print(f"Q2.3 The Total Surface Area of this figure is {TSA} cm2")