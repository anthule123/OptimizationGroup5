# Github Copilot
# Github Education

import gurobipy as gp
from gurobipy import GRB

class ColorProblem:
    def __init__(self, N, k):
        self.N = N
        self.k = k
        self.model = gp.Model("ColorProblem")
        self.x = [[self.model.addVar(vtype=GRB.BINARY, lb = 0, ub= 1, name = f'x_{i}_{j}') for i in range(0, self.N)] for j in range(0, self.k)]
        return None
    def setOneColorConstraints(self):
        for i in range(1, self.N + 1):
            return self.model.addConstr(sum(self.x[j][i] for j in range(self.k)) == 1)
    @property
    def getListOfSumThreeLists(self):
        listOfThreeSumLists = []
        halfOfN = (self.N + 1) // 2
        for numA in range(1, halfOfN):
            for numB in range(numA + 1, self.N - numA + 1):
                numC = numA + numB
                listOfThreeSumLists.append([numA, numB, numC])
        return listOfThreeSumLists
    def setSumColorConstraints(self):
        listOfThreeNumSumLists = self.getListOfSumThreeLists
        for listIndice in range(len(listOfThreeNumSumLists)):
            sumList = listOfThreeNumSumLists[listIndice]
            for l in range(0, self.k):
                return self.model.addConstr(sum(self.x[l][sumList[s] - 1] for s in range(3)) <= 2)
    def setObjective(self):
        self.model.setObjective(sum(self.x[0][i] for i in range(self.N)), sense = GRB.MINIMIZE)
    def solve(self):
        self.setOneColorConstraints()
        self.setSumColorConstraints()
        self.setObjective()
        self.model.optimize()

ModelColor = ColorProblem(26, 2)
print(ModelColor.getListOfSumThreeLists)
ModelColor.solve()
        