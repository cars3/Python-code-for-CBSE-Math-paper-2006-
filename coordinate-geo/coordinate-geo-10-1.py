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



#Question 2.1

x = []
y = []
xx = []
yy = []

for a in range(-20,20):
    for b in range(-20,20):
        if 4*a - b -8 == 0:
            x.append(a)
            y.append(b)

for a in range(-20,20):
    for b in range(-20,20):
        if 2*a - 3*b +6 == 0:
            xx.append(a)
            yy.append(b)

plt.plot(x, y)
plt.plot(xx,yy)
plt.axvline(x=0,color='black')
plt.axhline(y=0,color='black')

plt.title('Question 2.1')
plt.show() #un-hash this line to see the graph itself
print(f"Q2.1 This is the graph along with that the points which form a triangle are (3,4), (0,-3), (0,2) "
      f"with the x axis")