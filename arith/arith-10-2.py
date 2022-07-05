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

#Question 1.6
sum_of_numbers = 0
for number in range(10,99):
    if number % 4 == 0:
        sum_of_numbers += number
print(f"Q1.6. The sum of all the two digit natural numbers that are divisible by 4 are {sum_of_numbers}")