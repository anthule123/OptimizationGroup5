# %%
import gurobipy as gp
from gurobipy import GRB
import numpy as np

# %%
class LinearRegression:
    def __init__(self, data):
        self.data = data
        self.n = len(data)
        self.model = gp.Model('Linear Regression')
        #loại liên tục
        self.a = self.model.addVar(
                                  vtype=GRB.CONTINUOUS,
                                   name='a')
        self.b = self.model.addVar(
                                    vtype=GRB.CONTINUOUS,
                                    name='b')
    def setObjective(self):
        self.model.setObjective(
                                gp.quicksum(
                                    (self.data[i][1]-self.a*self.data[i][0]-self.b)**2 
                                    for i in range(self.n)),
                                GRB.MINIMIZE)
    def solve(self):
        self.setObjective()
        self.model.optimize()
        

# %%
#tạo dữ liệu độ dài 10, random quanh đường thẳng y = 2x 
data = [ [i, 2*i + np.random.normal(0, 1)] for i in range(10)]
data = np.array(data)
print(data)

# %%
linearRegression = LinearRegression(data)
linearRegression.solve()
print('a = ', linearRegression.a.x)
print('b = ', linearRegression.b.x)

# %%
#plot dữ liệu
import matplotlib.pyplot as plt
plt.scatter(data[:, 0], data[:, 1])
#x từ min(data[:, 0]) đến max(data[:, 0])
x = np.linspace(min(data[:, 0]), max(data[:, 0]), 100)
y = linearRegression.a.x*x + linearRegression.b.x
plt.plot(x, y, 'r')
plt.show()



