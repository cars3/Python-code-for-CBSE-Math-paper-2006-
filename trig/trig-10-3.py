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

#Question 3.4a

AB = ED = 50
CD = X
CE = 1
AE = 1
CD = 1
#AE = BD
tan30 = round(math.tan(0.523599),2)
tan60 = round(math.tan(1.0472), 2)

AE = CE / tan30
CD = tan60 * AE
#As AE = BD

ratio = int(CD/CE ) + 1

#CD = 50 + CE
# 50 + CE : CE :: 3:1

CE = Symbol('CE')
eq = Eq(50 - 2*CE )
ans = solve(eq)
CD = ans[0] + ED
print(f"Q3.4a The value of the height of the building is {CD}")