"""
  Thông tin nhóm
  Thiều Đình Minh Hùng, 21000006, K66TNT
  Lê Thị Thu An, 18001975, K63TNT
  
  Lớp học phần: MAT 2407 4 TNT
  
  Danh sách bài tập
  - bài 2.
     a) lineEquation(point1: tuple, point2: tuple)
     b) planeEquation(point1: tuple, point2: tuple, point3: tuple)

"""
#Bài 2
#hàm tìm phương trình đường thẳng đi qua 2 điểm A và B
#với 3 hệ số a,b,c của phương trình ax + by = c
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
#ví dụ
A = (1.0, 0)
B = (0.0, 1.0)
print(lineEquation(A, B))
#hàm kiểm tra xem các thành phần trong 1 iterable có phải là số nguyên không
def isInteger(iterable):
    for i in iterable:
        if i  != int(i):
            return False
    return True
def toIntegers(iterable):
    A = tuple(int(i) for i in iterable)
    return A
#Bài 1.b. hàm tìm phương trình mặt phẳng đi qua 3 điểm A, B, C
#với 4 hệ số a, b, c, d của phương trình ax + by + cz = d
def planeEquation(point1: tuple, point2: tuple, point3: tuple):
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
#ví dụ
A = (1, 0, 0)
B = (0, 1, 0)
C = (0, 0, 1)
print(planeEquation(A, B, C))

