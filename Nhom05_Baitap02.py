"""
  Thông tin nhóm
  Thiều Đình Minh Hùng, 21000006, K66TNT
  Lê Thị Thu An, K63TNT
  
  Lớp học phần: MAT 2407 4 TNT
  
  Danh sách bài tập
  - Bài 1. getAllCoordinates(), getAllWhiteCells(), printChessboard()
  - Bài 2. getRandomElement(listX: list)
  - Bài 3. getUniqueElements(listA: list, listB: list)
  - Bài 4. getQueenNextPossiblePositions(PresentPosition: str)
"""
# Bai 1:
# 1)
# Hàm trả về tất cả các ô cờ vua có thể có
listRow = [i for i in range(1, 9)]
listColumn = [chr(j+ord("a")) for j in range(0, 8)]

def getAllCoordinates():
  listAllCoordinates = []
  for col in listColumn:
    for row in listRow:
      listAllCoordinates.append(col+str(row))
  return listAllCoordinates
print(getAllCoordinates()) #['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8']
# 2)
# Hàm trả về tất cả các ô trắng
def getAllWhiteCells():
  listAllCoordinates = getAllCoordinates()
  listAllWhiteCells = []
  for cell in listAllCoordinates:
    if (ord(cell[0]) + int(cell[1])) % 2 == 1:
      listAllWhiteCells.append(cell)
  return listAllWhiteCells
print(getAllWhiteCells()) #['a2', 'a4', 'a6', 'a8', 'b1', 'b3', 'b5', 'b7', 'c2', 'c4', 'c6', 'c8', 'd1', 'd3', 'd5', 'd7', 'e2', 'e4', 'e6', 'e8', 'f1', 'f3', 'f5', 'f7', 'g2', 'g4', 'g6', 'g8', 'h1', 'h3', 'h5', 'h7']
# 3)
# Hàm in ra tất cả các ô trên bàn cờ sắp theo góc nhìn của bên trắng
def printChessboard():
  listAllCells = getAllCoordinates()
  ListofrowList = []
  for row_i in listRow:
    ListRow_i = []
    for col_j in listColumn:
      ListRow_i.append(listAllCells[(ord(col_j)-ord("a"))*8 + row_i - 1])
    ListofrowList.append(ListRow_i)
  rowList = [" ".join(ListofrowList[i]) for i in range(0, 8)]
  for k in range(0, len(rowList)):
    print(rowList[7 - k])
      
printChessboard()
"""
a8 b8 c8 d8 e8 f8 g8 h8
a7 b7 c7 d7 e7 f7 g7 h7
a6 b6 c6 d6 e6 f6 g6 h6
a5 b5 c5 d5 e5 f5 g5 h5
a4 b4 c4 d4 e4 f4 g4 h4
a3 b3 c3 d3 e3 f3 g3 h3
a2 b2 c2 d2 e2 f2 g2 h2
a1 b1 c1 d1 e1 f1 g1 h1  
"""
# Bài 2:
# Hàm trả về một phần tử ngẫu nhiên trong một list
import random
def getRandomElement(listX: list):
  IndexList = [i for i in range(0, len(listX))]
  IndexRandom = random.choice(IndexList)
  return listX[IndexRandom]
print(getRandomElement([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])) # 1

print(getRandomElement(['a1', 'b5', 'c6', 'f7', 'g3'])) # f7

# Bài 3:
# Hàm lọc ra các phần tử nằm trong listA mà không nằm trong listB
def getUniqueElements(listA: list, listB: list):
  listC = []
  for i in range(len(listA)):
    if (listA[i] in listB) == False:
      listC.append(listA[i])
  return listC
listA1 = [5, 7, 13, 6, 4, 9, 8, 14]
listB1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(getUniqueElements(listA1, listB1)) # [13, 14]

# Bài 4:
# Hàm xác định vị trí có thể của quân hậu ở nước đi tiếp theo
def getColumn(Position: str):
  listAllCells = getAllCoordinates()
  if Position not in listAllCells:
    raise ValueError("Position is not valid")
  else:
    PositionList = list(Position)
    Column = PositionList[0]
    return Column
def getRow(Position: str):
  listAllCells = getAllCoordinates()
  if Position not in listAllCells:
    raise ValueError("Position is not valid")
  else:
    PositionList = list(Position)
    Row = int(PositionList[1])
    return Row
def getQueenNextPossiblePositions(PresentPosition: str):
  listAllCells = getAllCoordinates()
  if PresentPosition not in listAllCells:
    raise ValueError("Position is not valid")
  else:
    presentColumn = getColumn(PresentPosition)
    presentRow = getRow(PresentPosition)
    listNextPossiblePositions = []
    for i in listRow:
      listNextPossiblePositions.append(presentColumn + str(i))
    listNextPossiblePositions.remove(PresentPosition)
    for j in listColumn:
      listNextPossiblePositions.append(j + str(presentRow))
    listNextPossiblePositions.remove(PresentPosition)
    for k in listRow:
      if chr(ord(presentColumn) + k - presentRow) in listColumn:
        listNextPossiblePositions.append(chr(ord(presentColumn) + k - presentRow) + str(k))
    listNextPossiblePositions.remove(PresentPosition)
    for l in listRow:
      if chr(ord(presentColumn) - l + presentRow) in listColumn:
        listNextPossiblePositions.append(chr(ord(presentColumn) - l + presentRow) + str(l))
    listNextPossiblePositions.remove(PresentPosition)
    return listNextPossiblePositions
print(getQueenNextPossiblePositions("d6")) # ['d1', 'd2', 'd3', 'd4', 'd5', 'd7', 'd8', 'a6', 'b6', 'c6', 'e6', 'f6', 'g6', 'h6', 'a3', 'b4', 'c5', 'e7', 'f8', 'h2', 'g3', 'f4', 'e5', 'c7', 'b8']
print(getQueenNextPossiblePositions("a1")) # ['a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'c1', 'd1', 'e1', 'f1', 'g1', 'h1', 'b2', 'c3', 'd4', 'e5', 'f6', 'g7', 'h8']
print(getQueenNextPossiblePositions("c8")) # ['c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'a8', 'b8', 'd8', 'e8', 'f8', 'g8', 'h8', 'a6', 'b7', 'h3', 'g4', 'f5', 'e6', 'd7']

