# Github Copilot
# Github Education

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
