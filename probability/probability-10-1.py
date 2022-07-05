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


#Question 2.10
#a
print("Q2.10")
a = []
for num in range(0,20):
        if num % 2 != 0:
            a.append("1")
        else:
                continue
print(f"a) The probability of getting an odd number is {int((len(a)/20)*100)}% ")

b = []
for num in range(1,20):
        if num % 2 == 0:
            b.append(num)
        if num % 3 == 0:
            b.append(num)
        else:
            continue
b = list(set(b))
print(f"b) The probability of getting a number divisible by 2 or 3 is {int((len(b)/20)*100)}% ")

non_prime = []
for num in range(2,20):
        for div in range(2,num):
                if num % div == 0:
                        non_prime.append(num)
non_prime = list(set(non_prime))
c = []
for num in range(2,20):
        if num not in non_prime:
                c.append(num)

print(f"c) The probability of getting a prime number {int((len(c)/20)*100)}% ")

d = []
for num in range(1,20):
        if num % 10 != 0:
            d.append(num)
        else:
            continue
d = list(set(d))
print(f"d) The probability of getting a number not divisible by 10 is {int((len(d)/20)*100)}% ")