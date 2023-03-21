
import gurobipy as gp
from gurobipy import GRB

model = gp.Model("ColorProblem")
x =[[model.addVar(vtype=GRB.BINARY, 
                 name = f'x_{i}_{j}')
                   for i in range(0, 6)]
                     for j in range(0, 2)]

threeSum = [[1,2,3],
            [1,3,4],
            [1,4,5],
            [2,3,5],
]
for num in range(1, 6):
    model.addConstr(x[0][num]
                     + x[1][num] == 1)
for threeNumber in threeSum:
    for l in range(0, 2):
        model.addConstr(x[l][threeNumber[0]]
                         + x[l][threeNumber[1]]
                           + x[l][threeNumber[2]] <= 2)
#tổng tất cả = N
model.addConstr(sum(x[l][i] for l in range(2) for i in range(1, 6)) == 5)
model.setObjective(1, sense = GRB.MINIMIZE)
model.optimize()
#print solution
for v in model.getVars():
    print(v.varName, v.x)