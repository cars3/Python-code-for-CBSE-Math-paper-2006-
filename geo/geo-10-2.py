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


#Question 2.5
A = (Ax,Ay) =(3.5, 5)
B = (Bx,By) =(0, 0)
C = (Cx,Cy) =(0, 7)

ab = [A[0], B[0]]
ab_1 = [A[1], B[1]]

bc = [B[0], C[0]]
bc_1 = [B[1], C[1]]

ac = [A[0], C[0]]
ac_1 = [A[1], C[1]]


plt.plot(ab, ab_1)
plt.plot(bc, bc_1)
plt.plot(ac, ac_1)
plt.show()