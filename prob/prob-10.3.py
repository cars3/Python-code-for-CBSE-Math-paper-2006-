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

#Question 2.2

#set 1
s = 0 # for the sake of python, the value is kept as 0, this is supposed to be x the variable
d = 300
t = 0 # for the sake of python, the value is kept as 0, this is supposed to be t the variable

#set 2
ss = s + 5
dd = d
tt = t-2

# dd = ss * tt
# 300 = (x-5)(t-2)
# t = d/s = 300/x
# 300 = (x-5)(300/x - 2)
#x^2 + 5x - 750

a = +1
b = 5
c = -750
dis = b * b - 4 * a * c 
sqrt_val = math.sqrt(abs(dis)) 
x_val = (x_1, x_2) = ((-b - sqrt_val)/(2 * a),(-b + sqrt_val)/(2 * a))

for x in x_val:
    if x < 0:
        continue
    else:
        print(f"Q2.2 The speed the train could have gone to save 2 hrs is {x}kmph")
      