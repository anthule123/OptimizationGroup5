import math
from math import sqrt
def getDivisorList(n):
    nSqrt = int(sqrt(n))
    smallDivisorList = [1]
    bigDivisorList = [n]
    for i in range(2, nSqrt + 1):
        if (n % i == 0):
            smallDivisorList = smallDivisorList + [i]
            bigDivisorList = [n//i] + bigDivisorList
    if nSqrt**2 == n:
        smallDivisorList.append(nSqrt)
    ans = smallDivisorList + bigDivisorList
    uniqueList = list(set(ans))
    uniqueList.sort()
    return uniqueList