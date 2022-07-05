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



#Question 3.1

AB = 1
AC = np.sqrt(2 *(AB**2))

# as the triangles are equitlateral that makes them similiar, as all angles = 60

ratio = f"{AB**2}/{int(AC**2)}"
print("Q3.1 As the 2 triangles are similiar to each other, and as the the ratio of the sides are in the ratio"
     f" of {ratio}, Hence, ar(ΔABD)= {ratio} ar(ΔCAE)")