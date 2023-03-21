# Github Copilot
# Github Education

import gurobipy as gp
from gurobipy import GRB

class ColorProblem:
    def __init__(self, N, k):
        self.N = N
        self.k = k
        self.model = gp.Model("ColorProblem")
        self.x = [[self.model.addVar(vtype=GRB.BINARY,
                                      name = f'x_{i}_{j}')
                                        for i in range(0, self.N + 1)]
                                          for j in range(0, self.k)]
        for color in range(0, self.k):
            self.model.addConstr(self.x[color][0]==0)
        self.listOfThreeSum = []
        self.setListOfThreeSum()
        return None
    def setOneColorConstraints(self):
        for i in range(1, self.N + 1):
            return self.model.addConstr(sum(self.x[j][i] 
                                            for j in range(self.k)) == 1)
    def setListOfThreeSum(self):
        halfOfN = (self.N + 1) // 2
        for numA in range(1, halfOfN):
            for numB in range(numA + 1, self.N - numA + 1):
                numC = numA + numB
                self.listOfThreeSum.append([numA, numB, numC])
    def setSumColorConstraints(self):
        for threeNumber in self.listOfThreeSum:
            for l in range(0, self.k):
                self.model.addConstr(sum(self.x[l][number] 
                                         for number in threeNumber)
                                          <= 2)
        self.model.addConstr(self.x[0][1] + self.x[0][2] + self.x[0][3] <= 2)
    def setNNumbersConstraints(self):
        #tổng tất cả các màu phải bằng N
        self.model.addConstr(sum(self.x[l][i] 
                                        for l in range(self.k)
                                            for i in range(1, self.N + 1)) 
                                            == self.N)

    def setObjective(self):
        self.model.setObjective(sum(self.x[0][i] for i in range(1, self.N + 1)),
                                sense = GRB.MINIMIZE)
    def solve(self):
        self.setOneColorConstraints()
        self.setSumColorConstraints()
        self.setNNumbersConstraints()
        self.setObjective()
        self.model.optimize()
        

modelColor = ColorProblem(26, 2)
print(modelColor.listOfThreeSum)
modelColor.solve()
        