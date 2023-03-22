"""
  Thông tin nhóm
  Thiều Đình Minh Hùng, 21000006, K66TNT
  Lê Thị Thu An, 18001975, K63TNT
  
  Lớp học phần: MAT 2407 4 TNT
  
  Danh sách bài tập
  - bài 3.
     4. ColorProblem(N: int, k: int)
        Hàm kiểm tra xem với k màu, có thể tô N số từ 1->N 
        bởi k màu sao cho ko có bộ 3 số 1<=a<b<c<=N sao cho a+b=c
        và a,b,c đều được tô cùng một màu.
     5. findNForKColors(k: int)
        Hàm tìm số N lớn nhất nhất sao cho với k màu, 
        có thể tô N số từ 1->N bởi k màu sao cho
        ko có bộ 3 số 1<=a<b<c<=N sao cho a+b=c
        và a,b,c đều được tô cùng một màu.
"""
import gurobipy as gp
from gurobipy import GRB

class ColorProblem:
    def __init__(self, N, k):
        self.N = N
        self.k = k
        self.model = gp.Model("ColorProblem")
        self.colorSet = [i for i in range(k)]
        self.numSet = [i + 1 for i in range(N)]
        self.x = [[self.model.addVar(vtype=GRB.BINARY, name = f'x_{num - 1}_{color}')
              for color in self.colorSet] for num in self.numSet] # biến x_i_j chỉ báo việc màu j được gán cho số i hay không.
    def setOneColorConstraints(self):
        # mỗi số được tô đúng một màu
        for num in self.numSet:
            self.model.addConstr(sum(self.x[num - 1][color] for color in self.colorSet) == 1)
    @property
    def listOfThreeSum(self):
        # tạo list chứa các bộ số a < b < c sao cho a + b = c
        listOfListThreeSum = []
        halfOfN = (self.N + 1) // 2
        rangeOfNumA = [num1 for num1 in range(1, halfOfN)]
        for numA in rangeOfNumA:
            rangeOfNumB = [num2 for num2 in range(numA + 1, self.N - numA + 1)]
            for numB in rangeOfNumB:
                listOfListThreeSum.append([numA, numB, numA + numB])
        return listOfListThreeSum
    
    def setSumColorConstraints(self):
        #Trong 3 số a < b < c mà a + b = c thì mỗi màu dùng không quá 2 lần
        for threeNumber in self.listOfThreeSum:
            for color in self.colorSet:
                self.model.addConstr(sum(self.x[number - 1][color] for number in threeNumber) <= 2)
    
    def setObjective(self):
        self.model.setObjective(0, sense = GRB.MAXIMIZE)
        
    def solve(self):
        self.setOneColorConstraints()
        self.setSumColorConstraints()
        self.setObjective()
        self.model.optimize()
    
modelColor = ColorProblem(11, 3)
print(modelColor.listOfThreeSum)
modelColor.solve()

# Cho k màu, 
# #tìm số N nhỏ nhất sao cho có thể tô màu theo cách trên cho N số từ 1->N.
def findNforKColors(k):
    n = k
    while True:
        modelColor = ColorProblem(n+1, k)
        modelColor.solve()
        #nếu có nghiệm feasible thì 
        if modelColor.model.status == GRB.OPTIMAL:
            n += 1
        else:
            return n
 