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

#Question 1.7
(principle,down_payment,rate_of_interest) = (2500,520,25/100)
installment = (principle - down_payment)/4
interest = rate_of_interest * installment
sum = 0
for month in range(0,4):
   sum += installment + interest
print(f"Q1.7. The total the sum that will have to be paid (not considering the down payment is) Rs.{sum} and each "
      f"installment will cost {installment + interest}")