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


#Question 3.4b
a = 1
x = 1
h = 1
tan_alpha = 1
tan_beta = 1
#tan_alpha = h / a + x
#tan_beta = h / x 

x = h / tan_alpha - a
x = h / tan_beta

#h / tan_beta = (h / tan_alpha )- a
#h * (1/tan_beta  - 1/tan-alpha) = -a
#h = a /(1/tan_beta  - 1/tan-alpha)
# h = a * tan_alpha * tan_beta / tan_beta - tan_alpha