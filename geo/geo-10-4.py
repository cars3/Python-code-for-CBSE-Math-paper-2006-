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


#Question 2.6b
A = (Ax, Ay)= (5, 1)
B = (Bx,By) = (-3,-7)
C = (Cx,Cy)= (7,-1)

for x in range(-100,100):
    for y in range(-100,100):
        if math.sqrt((Ax - x)**2 + (Ay - y)**2) == math.sqrt((Bx - x)**2 + (By - y)**2) == math.sqrt((Cx - x)**2 + (Cy - y)**2):
            print(f"Q2.6b. The value of the coordinates equidistant to A,B and C is {x,y}")