

from Nhom05_BaiTap04_AnHung import ColorProblem
import gurobipy as gp
from gurobipy import GRB

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
        
if __name__ == '__main__':
    print('Solution for k=2 is N='+str(findNforKColors(2)))
    