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

#Question 3.5

income = 385000
expenses = 90000 + 3500*4 + 20000 + 1600*11
tax = 13000 + (30/100)*(385000 - 10000 - 5000)
edu_tax = (2/100) * (13000 + (30/100)*(385000 - 10000 - 5000))

tax += edu_tax

print(f"Q3.5 the income tax is {tax}")