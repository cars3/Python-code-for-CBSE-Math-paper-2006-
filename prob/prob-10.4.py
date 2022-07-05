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

#Question 3.3 a

roof_area = 22*20 
vessel_volume = (22/7) * (1**2) * 3.5

rain_fall = (vessel_volume / roof_area) * 100 #converting to cm

print(f"Q3.3a The rainfall in centimeteres is {rain_fall}cm ")