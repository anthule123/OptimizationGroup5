
#input 2 điểm A(x1, y1) và B(x2, y2)
#output phương trình đường thẳng đi qua 2 điểm A và B
#với 3 hệ số a,b,c của phương trình ax + by =c

from integer_tuple import isInteger, toIntegers


def lineEquation(point1: tuple, point2: tuple):
    if(isInteger(point1)):
        point1 = toIntegers(point1)
    if(isInteger(point2)):
        point2 = toIntegers(point2)
    x1, y1 = point1
    x2, y2 = point2
    a = y1 - y2
    b = x2 - x1
    c = -x1*y2 + x2*y1
    return (a, b, c)

A = (1.0, 0)
B = (0.0, 1.0)
print(lineEquation(A, B))

