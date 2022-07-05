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

#Question 2.8
p = 1
classes = [0,20,40,60,80,100]
frequency = [17,p,32,24,19]
avg_list = []
xf = []
count = 0
mean = 50

for x in frequency:
    sigma_xf  = 0
    sigma_f  = 0
    avg = (classes[count] + classes[count+1]) / 2
    avg_list.append(int(avg))
    count = count + 1

for val in range(0,30):
    xf.clear()
    p = val
    frequency[1] = p
    for i in range(0, len(avg_list)):
        xf.append(avg_list[i] * frequency[i])

    for i in xf:
        sigma_xf += i


    for j in frequency:
        sigma_f += j
    
    if sigma_xf / sigma_f == 50:
        print(f"Q2.8 The value of 'p' in this table is {p}")

    sigma_xf  = 0
    sigma_f  = 0
    