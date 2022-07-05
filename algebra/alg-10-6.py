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

#Question 1.4b
tens = 1
ones = 1

for tens in range(1,9):
    for ones in range(1,9):
        if tens * ones == 35:
            number = int(str(tens) + str(ones))
            number_flip = int(str(ones) + str(tens))
            if number + 18 == number_flip:
                print(f"Q1.4b. A two-digit number is such that the product of its digits is 35 and when 18 is added,"
                f"number's digits interchange their places, is {number}")