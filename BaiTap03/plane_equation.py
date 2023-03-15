
# Write a Python program to find the
# equation of a plane passing through
# three points. ax + by + cz = d
from integer_tuple import isInteger, toIntegers


def planeEquation(point1: tuple, 
                  point2: tuple,
                  point3: tuple):
    if(isInteger(point1)):
        point1 = toIntegers(point1)
    if(isInteger(point2)):
        point2 = toIntegers(point2)
    if(isInteger(point3)):
        point3 = toIntegers(point3)
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    x3, y3, z3 = point3
    a = y1*(z2 - z3) + y2*(z3 - z1) + y3*(z1 - z2)
    b = z1*(x2 - x3) + z2*(x3 - x1) + z3*(x1 - x2)
    c = x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)
    d = x1*(y2*z3 - y3*z2) + x2*(y3*z1 - y1*z3) + x3*(y1*z2 - y2*z1)
    return (a, b, c, d)

A = (1, 0,0)
B = (0, 1,0)
C = (0, 0,1)
print(planeEquation(A, B,C))

A = (3,0,0)
B = (3,1,0)
C = (3,0,1)
print(planeEquation(A, B,C))
