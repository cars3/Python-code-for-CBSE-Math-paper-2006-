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

# Question 3.3b

R = 20
r = 8
h = 16

l = math.sqrt(h**2 + (R-r)**2)
# total area (for a bucket) = curved area + area of bottom circle
area = (3.14 * l * (R + r)) + (3.14 * r**2)
cost_per_metre = 0.15
cost = area * cost_per_metre

print(f"Q3.3b. The cost of making a bucket with such dimensions with the price of Rs.0.15 for 1 cm^2 of"
      f" metal is Rs.{cost}")