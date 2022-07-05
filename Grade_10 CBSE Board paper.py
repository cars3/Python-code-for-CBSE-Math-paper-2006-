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
#Question 1.1a

# A = np.array([[47, 31],
#               [31, 47]])

# B = np.array([
#     [63],
#     [15]
# ])

# X = np.dot(np.linalg.inv(A), B)
# X0 = float(X[0])
# X0 = "{:.2f}".format(X0)

# X1 = float(X[1])
# X1 = "{:.2f}".format(X1)

# print(f" For Q1.1a)  the value of x in this pair of equations is {X0} and the value of y is {X1}  ")

# #Question 1.1b
# x_y = []
# for x in range(1,100):
#     for y in range(1,100):
#         a = -y
#         b = x
#         if (a*x/b) - (b*y/a) == a + b:
#             if a*x - b*y == 2*a*b:
#                 x_y.append((x,y))
# print(f" For Q1.1b) Here these equations are possible with following values of x and y {x_y}")



# #Question 1.2

# x= Symbol('x')

# P = 2 /x**2 - x - 6
# Q = 3 / x**2 + x - 3
# R = 4 / x**2 - 4*x + 3
# eq = (P+Q) + R
# expr = eq
# expr0 = expr.expand()
# expr1 = collect(expr0, x)
# print(f"Q1.2 The solution of the equation is {expr1}")

# test = Poly(eq0.subs(x, Symbol('x')), Symbol('x')).all_coeffs()
# print(test)
# print(test[0])
# eq_numerator = solve((4*(x+2) + 2*(x-1) + 3*(x-3)*(x+2)*(x-1)),x)  
# eq_denominator = solve(((x-1)*(x+2)*(x-3)*(x**2  + x - 3)),x)

# ans_0 = eq_numerator[0]/ eq_denominator[1]
# print(ans_0)
# print(f"Q1.2 The solutions of the equation are ")

# #Question 1.3

# #roots of the equation x = 2,-3
# x = [2,-3]
# a_val = []
# b_val = []

# for val in x:
#     for a in range(-100,100):
#         Px = ((val^2) - (3*val) + 2) * ((2 * val^2)  + (7*val) + a)
#         if Px == 0:
#             a_val.append((a))

# for val1 in x:
#     for b in range(-100,100):
#         Qx = (val1^2 + 4*val1 + 3) * (3 * val1^2  - 7*val1 + b)
#         if Qx == 0:
#             b_val.append((b))s

# print(f"Q1.3 If x = 2, then the values of a,b are {a_val[0]},{b_val[0]} "
#       f"If x = -3, then the values of a,b are {a_val[1]},{b_val[1]}")



# #Question 1.4a

# aa= 2
# bb = 3

# #eq 12abx2 − 9a2 − 8b2 ·x−6ab
# a = 12*aa*bb
# b = - (9*aa^2 - 8*bb^2)
# c = -6*aa*bb

# d = (b**2) - (4*a*c)


# sol1 = (-b-cmath.sqrt(d))/(2*a)
# sol2 = (-b+cmath.sqrt(d))/(2*a)
# print(f"Q1.4a The 2 solutions of this equation are {sol1} x -a/b and {sol2} x -b/a")


# #Question 1.4b
# tens = 1
# ones = 1
#
# for tens in range(1,9):
#     for ones in range(1,9):
#         if tens * ones == 35:
#             number = int(str(tens) + str(ones))
#             number_flip = int(str(ones) + str(tens))
#             if number + 18 == number_flip:
#                 print(f"Q1.4b. A two-digit number is such that the product of its digits is 35 and when 18 is added,"
#                 f"number's digits interchange their places, is {number}")



# #Question 1.5

# a6 = -10
# a10 = -26
# a15 = 0

# d = int((a10 - a6)/4)

# # a6 = a + 5d

# a = a6 - 5*d
# print(a)

# a15 = a + (15 - 1)*d

# print(f"Q1.4b. in this AP, a15 is {a15}")


# #Question 1.6
# sum_of_numbers = 0
# for number in range(10,99):
#     if number % 4 == 0:
#         sum_of_numbers += number
# print(f"Q1.6. The sum of all the two digit natural numbers that are divisible by 4 are {sum_of_numbers}")


# #Question 1.7
# (principle,down_payment,rate_of_interest) = (2500,520,25/100)
# installment = (principle - down_payment)/4
# interest = rate_of_interest * installment
# sum = 0
# for month in range(0,4):
#    sum += installment + interest
# print(f"Q1.7. The total the sum that will have to be paid (not considering the down payment is) Rs.{sum} and each "
#       f"installment will cost {installment + interest}")


# #Question 1.8
# (P,T,R) = (36410,3,10/100)
# Amount = int(P * (1 + R)**T)
# print(f"Q1.8. The amount that the man has to pay is Rs.{Amount} ")

#Question 1.9


# #Question 1.10

# #PA * PB = PC *PD

# PA = 3
# AB = 9
# PB = PA + AB

# PC = 4
# PD = PC
# for x in range(0,10):
#     if PD + x == PA * PB / PC:
#         print(f"Q1.10. From this figure, the value of CD = {x}cm ")
#     else:
#         continue



# #Question 2.1

# x = []
# y = []
# xx = []
# yy = []

# for a in range(-20,20):
#     for b in range(-20,20):
#         if 4*a - b -8 == 0:
#             x.append(a)
#             y.append(b)

# for a in range(-20,20):
#     for b in range(-20,20):
#         if 2*a - 3*b +6 == 0:
#             xx.append(a)
#             yy.append(b)

# plt.plot(x, y)
# plt.plot(xx,yy)
# plt.axvline(x=0,color='black')
# plt.axhline(y=0,color='black')

# plt.title('Question 2.1')
# plt.show() #un-hash this line to see the graph itself
# print(f"Q2.1 This is the graph along with that the points which form a triangle are (3,4), (0,-3), (0,2) "
#       f"with the x axis")



# #Question 2.2

# #set 1
# s = 0 # for the sake of python, the value is kept as 0, this is supposed to be x the variable
# d = 300
# t = 0 # for the sake of python, the value is kept as 0, this is supposed to be t the variable

# #set 2
# ss = s + 5
# dd = d
# tt = t-2

# # dd = ss * tt
# # 300 = (x-5)(t-2)
# # t = d/s = 300/x
# # 300 = (x-5)(300/x - 2)
# #x^2 + 5x - 750

# a = +1
# b = 5
# c = -750
# dis = b * b - 4 * a * c 
# sqrt_val = math.sqrt(abs(dis)) 
# x_val = (x_1, x_2) = ((-b - sqrt_val)/(2 * a),(-b + sqrt_val)/(2 * a))

# for x in x_val:
#     if x < 0:
#         continue
#     else:
#         print(f"Q2.2 The speed the train could have gone to save 2 hrs is {x}kmph")
      


# #Question 2.3

# x = 1
# r = 2
# h = 3

# #vol = (22/7) * (r* (x)^2) * (h*x)  
# ratio = np.cbrt(1617/(r*h*(x^3)*22/7))

# TSA = 2*(22/7)*r*ratio*((h*ratio)+(r*ratio))
# print(f"Q2.3 The Total Surface Area of this figure is {TSA} cm2")


#Question 2.4(a)

# for x in range(1,91):
#     if (np.sin(x) + np.cos(x) / np.sin(x) - np.cos(x)) + (np.sin(x) - np.cos(x) / np.sin(x) + np.cos(x)) == (2 * ((1/np.cos(x))**2) / (np.tan(x))**2 - 1):
#         print(f"Q2.4a. When Theta has a value of{x}, then the following case is true")
#     else:
#         continue

# #Question 2.4(b)

# x = 60 # = theta
# ans_1 = (1/np.cos(90 - x) * 1/np.cos(90 - x)) - (1/np.tan(x) * 1/np.tan(x)) 
# ans_2 = (2 * np.cos(60) * np.cos(60)) / 3*((1/np.cos(43) * 1/np.cos(43)) - (1/np.tan(47) * 1/np.tan(47)) )
# print(f"Q2.4b The sum of this equation is {ans_1 + ans_2}")



# #Question 2.5
# A = (Ax,Ay) =(3.5, 5)
# B = (Bx,By) =(0, 0)
# C = (Cx,Cy) =(0, 7)

# ab = [A[0], B[0]]
# ab_1 = [A[1], B[1]]

# bc = [B[0], C[0]]
# bc_1 = [B[1], C[1]]

# ac = [A[0], C[0]]
# ac_1 = [A[1], C[1]]


# plt.plot(ab, ab_1)
# plt.plot(bc, bc_1)
# plt.plot(ac, ac_1)
# plt.show()




#Question 2.6a (there is no s its a 5)

# A = (Ax,Ay) =(1, 2)
# B = (Bx,By) =(5, 4)
# C = (Cx,Cy) =(3, 8)
# D = (Dx,Dy) =(-1, 6)
#
# AB = (Bx - Ax)**2 + (By - Ay)**2
# BC = (Cx - Bx)**2 + (Cy - By)**2
# CD = (Dx - Cx)**2 + (Dy - Cy)**2
# AD = (Dx - Ax)**2 + (Dy - Ay)**2
# AC = (Cx - Ax)**2 + (Cy - Ay)**2
# BD = (Dx - Bx)**2 + (Dy - By)**2
#
# if AB == BC == CD == AD:
#     if AC == BD:
#         print(f"The quadrilateral with vertices {A}, {B}, {C}, {D}, is a quadrilateral")


# #Question 2.6b
# A = (Ax, Ay)= (5, 1)
# B = (Bx,By) = (-3,-7)
# C = (Cx,Cy)= (7,-1)
#
# for x in range(-100,100):
#     for y in range(-100,100):
#         if math.sqrt((Ax - x)**2 + (Ay - y)**2) == math.sqrt((Bx - x)**2 + (By - y)**2) == math.sqrt((Cx - x)**2 + (Cy - y)**2):
#             print(f"Q2.6b. The value of the coordinates equidistant to A,B and C is {x,y}")






# #Question 2.7
# A = (Ax, Ay) = (-1, 3)
# B = (Bx, By) = (2, 0)
# C = (Cx, Cy) = (5, -1)
# for number in range(-100,100):
#     A = (Ax, Ay) = (-1, 3)
#     B = (Bx, By) = (2, number)
#     C = (Cx, Cy) = (5, -1)
#     area = (1 / 2) * math.fabs(Ax * (By - Cy) + Bx * (Cy - Ay) + Cx * (Ay - By))
#     if area == 0:
#         print(f"Q2.7. The points A,B,C become collinear when B(y) is changed to {number} ")
#     else:
#        continue

# #Question 2.8
# p = 1
# classes = [0,20,40,60,80,100]
# frequency = [17,p,32,24,19]
# avg_list = []
# xf = []
# count = 0
# mean = 50

# for x in frequency:
#     sigma_xf  = 0
#     sigma_f  = 0
#     avg = (classes[count] + classes[count+1]) / 2
#     avg_list.append(int(avg))
#     count = count + 1

# for val in range(0,30):
#     xf.clear()
#     p = val
#     frequency[1] = p
#     for i in range(0, len(avg_list)):
#         xf.append(avg_list[i] * frequency[i])

#     for i in xf:
#         sigma_xf += i


#     for j in frequency:
#         sigma_f += j
    
#     if sigma_xf / sigma_f == 50:
#         print(f"Q2.8 The value of 'p' in this table is {p}")

#     sigma_xf  = 0
#     sigma_f  = 0
    
    

# #Question 2.9
# monthly_expenditure = ['Rent', 'Food', 'Clothing','Education', 'Misc.']
#
# data = [1500, 3600, 1200, 2100, 2400]
#
# fig = plt.figure(figsize=(10, 7))
# plt.pie(data, labels=monthly_expenditure)
#
# plt.show()





# #Question 2.10
# #a
# print("Q2.10")
# a = []
# for num in range(0,20):
#         if num % 2 != 0:
#             a.append("1")
#         else:
#                 continue
# print(f"a) The probability of getting an odd number is {int((len(a)/20)*100)}% ")
#
# b = []
# for num in range(1,20):
#         if num % 2 == 0:
#             b.append(num)
#         if num % 3 == 0:
#             b.append(num)
#         else:
#             continue
# b = list(set(b))
# print(f"b) The probability of getting a number divisible by 2 or 3 is {int((len(b)/20)*100)}% ")
#
# non_prime = []
# for num in range(2,20):
#         for div in range(2,num):
#                 if num % div == 0:
#                         non_prime.append(num)
# non_prime = list(set(non_prime))
# c = []
# for num in range(2,20):
#         if num not in non_prime:
#                 c.append(num)
#
# print(f"c) The probability of getting a prime number {int((len(c)/20)*100)}% ")
#
# d = []
# for num in range(1,20):
#         if num % 10 != 0:
#             d.append(num)
#         else:
#             continue
# d = list(set(d))
# print(f"d) The probability of getting a number not divisible by 10 is {int((len(d)/20)*100)}% ")





# #Question 3.1

# AB = 1
# AC = np.sqrt(2 *(AB**2))

# # as the triangles are equitlateral that makes them similiar, as all angles = 60

# ratio = f"{AB**2}/{int(AC**2)}"
# print("Q3.1 As the 2 triangles are similiar to each other, and as the the ratio of the sides are in the ratio"
#      f" of {ratio}, Hence, ar(ΔABD)= {ratio} ar(ΔCAE)")


#3.2


# #Question 3.3 a

# roof_area = 22*20 
# vessel_volume = (22/7) * (1**2) * 3.5

# rain_fall = (vessel_volume / roof_area) * 100 #converting to cm

# print(f"Q3.3a The rainfall in centimeteres is {rain_fall}cm ")



# # Question 3.3b
#
# R = 20
# r = 8
# h = 16
#
# l = math.sqrt(h**2 + (R-r)**2)
# # total area (for a bucket) = curved area + area of bottom circle
# area = (3.14 * l * (R + r)) + (3.14 * r**2)
# cost_per_metre = 0.15
# cost = area * cost_per_metre
#
# print(f"Q3.3b. The cost of making a bucket with such dimensions with the price of Rs.0.15 for 1 cm^2 of"
#       f" metal is Rs.{cost}")


# #Question 3.4a

# AB = ED = 50
# CD = X
# CE = 1
# AE = 1
# CD = 1
# #AE = BD
# tan30 = round(math.tan(0.523599),2)
# tan60 = round(math.tan(1.0472), 2)

# AE = CE / tan30
# CD = tan60 * AE
# #As AE = BD

# ratio = int(CD/CE ) + 1

# #CD = 50 + CE
# # 50 + CE : CE :: 3:1

# CE = Symbol('CE')
# eq = Eq(50 - 2*CE )
# ans = solve(eq)
# CD = ans[0] + ED
# print(f"Q3.4a The value of the height of the building is {CD}")


# #Question 3.4b
# a = 1
# x = 1
# h = 1
# tan_alpha = 1
# tan_beta = 1
# #tan_alpha = h / a + x
# #tan_beta = h / x 

# x = h / tan_alpha - a
# x = h / tan_beta

# #h / tan_beta = (h / tan_alpha )- a
# #h * (1/tan_beta  - 1/tan-alpha) = -a
# #h = a /(1/tan_beta  - 1/tan-alpha)
# # h = a * tan_alpha * tan_beta / tan_beta - tan_alpha




# #Question 3.5

# income = 385000
# expenses = 90000 + 3500*4 + 20000 + 1600*11
# tax = 13000 + (30/100)*(385000 - 10000 - 5000)
# edu_tax = (2/100) * (13000 + (30/100)*(385000 - 10000 - 5000))

# tax += edu_tax

# print(f"Q3.5 the income tax is {tax}")

