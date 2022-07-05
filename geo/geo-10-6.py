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



#Question 2.9
monthly_expenditure = ['Rent', 'Food', 'Clothing','Education', 'Misc.']

data = [1500, 3600, 1200, 2100, 2400]

fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=monthly_expenditure)

plt.show()