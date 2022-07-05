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


#Question 2.6a (there is no s its a 5)

A = (Ax,Ay) =(1, 2)
B = (Bx,By) =(5, 4)
C = (Cx,Cy) =(3, 8)
D = (Dx,Dy) =(-1, 6)

AB = (Bx - Ax)**2 + (By - Ay)**2
BC = (Cx - Bx)**2 + (Cy - By)**2
CD = (Dx - Cx)**2 + (Dy - Cy)**2
AD = (Dx - Ax)**2 + (Dy - Ay)**2
AC = (Cx - Ax)**2 + (Cy - Ay)**2
BD = (Dx - Bx)**2 + (Dy - By)**2

if AB == BC == CD == AD:
    if AC == BD:
        print(f"The quadrilateral with vertices {A}, {B}, {C}, {D}, is a quadrilateral")