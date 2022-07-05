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


#Question 1.10

#PA * PB = PC *PD

PA = 3
AB = 9
PB = PA + AB

PC = 4
PD = PC
for x in range(0,10):
    if PD + x == PA * PB / PC:
        print(f"Q1.10. From this figure, the value of CD = {x}cm ")
    else:
        continue