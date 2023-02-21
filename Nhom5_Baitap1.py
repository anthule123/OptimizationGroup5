import math
from math import sqrt
def getDivisorList(n):
    nSqrt = int(sqrt(n))
    smallDivisorList = [1]
    bigDivisorList = [n]
    for i in range(2, nSqrt):
        if (n % i == 0):
            smallDivisorList = smallDivisorList + [i]
            bigDivisorList = [n//i] + bigDivisorList
    if nSqrt**2 == n:
        smallDivisorList.append(nSqrt)
    return smallDivisorList + bigDivisorList

print(getDivisorList(2*3*5*7*11*13*17*19*23*29-1))