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


#Question 2.7
A = (Ax, Ay) = (-1, 3)
B = (Bx, By) = (2, 0)
C = (Cx, Cy) = (5, -1)
for number in range(-100,100):
    A = (Ax, Ay) = (-1, 3)
    B = (Bx, By) = (2, number)
    C = (Cx, Cy) = (5, -1)
    area = (1 / 2) * math.fabs(Ax * (By - Cy) + Bx * (Cy - Ay) + Cx * (Ay - By))
    if area == 0:
        print(f"Q2.7. The points A,B,C become collinear when B(y) is changed to {number} ")
    else:
       continue