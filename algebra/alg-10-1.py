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

#Question 1.1a

A = np.array([[47, 31],
              [31, 47]])

B = np.array([
    [63],
    [15]
])

X = np.dot(np.linalg.inv(A), B)
X0 = float(X[0])
X0 = "{:.2f}".format(X0)

X1 = float(X[1])
X1 = "{:.2f}".format(X1)

print(f" For Q1.1a)  the value of x in this pair of equations is {X0} and the value of y is {X1}  ")