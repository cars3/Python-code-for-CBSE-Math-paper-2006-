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

#Question 1.8
(P,T,R) = (36410,3,10/100)
Amount = int(P * (1 + R)**T)
print(f"Q1.8. The amount that the man has to pay is Rs.{Amount} ")
