"""
  Thông tin nhóm
  Thiều Đình Minh Hùng, 21000006, K66TNT
  Lê Thị Thu An, 18001975, K63TNT
  
  Lớp học phần: MAT 2407 4 TNT
  
  Danh sách bài tập
  - bài 3.
     4. Color(N: int, k: int)
        Hàm kiểm tra xem với k màu, có thể tô N số từ 1->N 
        bởi k màu sao cho ko có bộ 3 số 1<=a<b<c<=N sao cho a+b=c
        và a,b,c đều được tô cùng một màu.
"""
"""
Restricted license - for non-production use only - expires 2024-10-28
Gurobi Optimizer version 10.0.1 build v10.0.1rc0 (win64)
CPU model: Intel(R) Core(TM) i7-5600U CPU @ 2.60GHz, instruction set [SSE2|AVX|AVX2]
Thread count: 2 physical cores, 4 logical processors, using up to 4 threads
Optimize a model with 32 rows, 16 columns and 88 nonzeros
Model fingerprint: 0xf3dcdd6d
Variable types: 0 continuous, 16 integer (16 binary)
Coefficient statistics:
  Matrix range     [1e+00, 1e+00]
  Objective range  [0e+00, 0e+00]
  Bounds range     [1e+00, 1e+00]
  RHS range        [1e+00, 2e+00]
Found heuristic solution: objective -0.0000000
Explored 0 nodes (0 simplex iterations) in 0.00 seconds (0.00 work units)
Thread count was 1 (of 4 available processors)
Solution count 1: -0
No other solutions better than -0
Optimal solution found (tolerance 1.00e-04)
Best objective -0.000000000000e+00, best bound -0.000000000000e+00, gap 0.0000%
x_0_1 = 1.0
x_1_1 = 1.0
x_2_0 = 1.0
x_3_1 = 1.0
x_4_0 = 1.0
x_5_0 = 1.0
x_6_0 = 1.0
x_7_1 = 1.0
Kết quả:
[1, 1, 0, 1, 0, 0, 0, 1]
"""
import gurobipy as gp
from gurobipy import GRB
import numpy as np
class Color:
    def __init__(self, N, k):
        self.N = N
        self.k = k
        self.model = gp.Model("ColorProblem")
        self.colorSet = [i for i in range(k)]
        self.numSet = [i + 1 for i in range(N)]
        self.x = [[self.model.addVar(vtype=GRB.BINARY, 
        name = f'x_{num - 1}_{color}')
              for color in self.colorSet]
               for num in self.numSet] # biến x_i_j chỉ báo việc màu j được gán cho số i hay không.
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
            listOfListThreeSum.extend([[numA, numB, numA + numB] for numB in range(numA + 1, self.N - numA + 1)])
        return listOfListThreeSum
    
    def setSumColorConstraints(self):
        #Trong 3 số a < b < c mà a + b = c thì mỗi màu dùng không quá 2 lần
        sumColorConstrain = [[self.model.addConstr(sum(self.x[number - 1][color] for number in threeNumber) <= 2) for color in self.colorSet] for threeNumber in self.listOfThreeSum]
    def setReflexiveSumColorConstraints(self):
        #thêm điều kiện phá tính đối xứng của bài toán
        sumReflexiveColorConstraint = [[self.model.addConstr(self.x[0][0] == 1)]]
        sumReflexiveColorConstraint.extend([[self.model.addConstr(self.x[number - 1][color] == 0)] for number in self.numSet[1: self.k] for color in self.colorSet[number:]])
    def setObjective(self):
        self.model.setObjective(0, sense = GRB.MAXIMIZE)
    def getSolution(self):
        if self.model.status == GRB.OPTIMAL:
            self.solution = [0]*self.N
            for num in self.numSet:
                for color in self.colorSet:
                    if self.x[num - 1][color].x == 1:
                        print(f'x_{num - 1}_{color} = {self.x[num - 1][color].x}')
                        self.solution[num - 1] = color
        else:
            print('No feasible solution')
        
    def solve(self):
        self.setOneColorConstraints()
        self.setSumColorConstraints()
        self.setReflexiveSumColorConstraints()
        self.setObjective()
        self.model.optimize()
        self.getSolution()
modelColor = Color(69, 4)
modelColor.solve()
print('Kết quả: ')
print(modelColor.solution)