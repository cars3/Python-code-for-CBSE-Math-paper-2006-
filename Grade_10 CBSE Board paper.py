import math
import matplotlib
import numpy as np
# #Question 1.1a
# # adding the two equations and subtracting them separately leads to 2 simpler equations which are
# # x + y = 1,  x - y = 3
# xy_list = []
# for x in range(-10,10):
#     for y in range(-10,10):
#         if x + y == 1:
#             xy_list.append((x,y))
# for (x,y) in xy_list:
#     if x - y == 3:
#         break
# print(f"Q1.1a. The value of the variables which suite these equations are {x} and {y}")
#
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
#
# #Question 1.6
# sum_of_numbers = 0
# for number in range(10,99):
#     if number % 4 == 0:
#         sum_of_numbers += number
# print(f"Q1.6. The sum of all the two digit natural numbers that are divisible by 4 are {sum_of_numbers}")
#
# #Question 1.7
# (principle,down_payment,rate_of_interest) = (2500,520,25/100)
# installment = (principle - down_payment)/4
# interest = rate_of_interest * installment
# sum = 0
# for month in range(0,4):
#    sum += installment + interest
# print(f"Q1.7. The total the sum that will have to be paid (not considering the down payment is) Rs.{sum} and each "
#       f"installment will cost {installment + interest}")
#
# #Question 1.8
# (P,T,R) = (36410,3,10/100)
# Amount = int(P * (1 + R)**T)
# print(f"Q1.8. The amount that the man has to pay is Rs.{Amount} ")
#
# #Question 2.1
import matplotlib.pyplot as plt

x = []
y = []
xx = []
yy = []

for a in range(-20,20):
    for b in range(-20,20):
        if 4*a - b -8 == 0:
            x.append(a)
            y.append(b)

for a in range(-20,20):
    for b in range(-20,20):
        if 2*a - 3*b +6 == 0:
            xx.append(a)
            yy.append(b)

plt.plot(x, y)
plt.plot(xx,yy)
plt.axvline(x=0,color='black')
plt.axhline(y=0,color='black')

plt.title('Question 2.1')
plt.show() #un-hash this line to see the graph itself
print(f"Q2.1 This is the graph along with that the points which form a triangle are (3,4), (0,-3), (0,2) "
      f"with the x axis")

# #Question 2.2
# (s,d,t) = (1,300,1)
# sdt_list = []
# for s in range(1,100):
#     for t in range(1,100):
#         if s == 300/t:
#             if t > 2:
#                 sdt_list.append((s,t))
#         else:
#             continue
# for item in sdt_list:
#     (s1,t1) = item
#     if s1 + 5 == 300 / (t1 - 2):
#         break
# print(f"Q2.2 The original speed of the train is {s1} kmph with this speed, it can cover the distance of {d}"
#       f" km it can cover it in {12} hrs")

#Question 2.3(fail)

# for v in range(1,1000):
#     r = v
#     h = (2/3) * v
#     if (22/7)*(r^2)*(h) == 1617 :
#         print(r,h)
#     else:
#         continue

#Quesion 2.4(a)

for x in range(1,91):
    if (np.sin(x) + np.cos(x) / np.sin(x) - np.cos(x)) + (np.sin(x) - np.cos(x) / np.sin(x) + np.cos(x)) == (2 * ((1/np.cos(x))**2) / (np.tan(x))**2 - 1):
        print(f"Q2.4a. When Theta has a value of{x}, then the following case is true")
    else:
        continue
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
#         continue
# #Question 2.8(need to study)
# #Question 2.9
# from matplotlib import pyplot as plt
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
# #Question 3.3a
# area = 2.2*2.0# in decameter so 100 should be multiplied later
# vessel = (22/7)*(3.5)
#
#
# for num in np.arange(0.0, 5.0, 0.1):
#     if area*num == vessel:
#         print(f"Q3.3a. The water level in cm is {num}cm")
#     else:
#         continue
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










