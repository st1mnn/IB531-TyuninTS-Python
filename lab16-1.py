import math


A = 10**-1
B = 2.1
C = 0.1
D = -3.12


X = (A**B + (B**A)*math.log(C) - C*math.log10(math.sqrt(A))) / (2*B+D)


print(X)
