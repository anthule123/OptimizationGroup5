

#viết 1 hàm kiểm tra xem các thành phần trong 
#1 iterable có phải là số nguyên không

def isInteger(iterable):
    for i in iterable:
        if i  != int(i):
            return False
    return True

def toIntegers(iterable):
    A = tuple(int(i) for i in iterable)
    return A

# print(isInteger([1,2.5]))
# print(isInteger([1,2,3,4,5,6,7,8,9,10]))
# print(isInteger([1,-1]))