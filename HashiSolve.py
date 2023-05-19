# Github Education
# Github Copilot

import gurobipy as gp
from gurobipy import GRB
class Point:
    def __init__(self, x, y):
        self.xCoordinate = x
        self.yCoordinate = y
        return None
class Segment:
    def __init__(self, point1:Point, point2:Point):
        self.point1 = point1
        self.point2 = point2
        return None
    def IsIntersect(self, another):
        # Return True if two segments intersect inside.
        # Return False if two segments do not intersect.
        pass
        
class HashiPuzzle:
    def __init__(self, listPoints:list, goalOrderList:list):
        self.listPoints = listPoints
        self.goalOrderList = goalOrderList
        self.model = gp.Model("HashiProblem")
    def getAdjacentPoints(self, index):
        # Return a list of adjacent points of point.
        point = self.listPoints[index]
        sameRowPointstoLeftList = [x for x in self.listPoints if x.xCoordinate == point.xCoordinate and x.yCoordinate < point.yCoordinate]
        sameRowPointstoRightList = [x for x in self.listPoints if x.xCoordinate == point.xCoordinate and x.yCoordinate > point.yCoordinate]
        sameColumnPointstoUpList = [x for x in self.listPoints if x.yCoordinate == point.yCoordinate and x.xCoordinate < point.xCoordinate]
        sameColumnPointstoDownList = [x for x in self.listPoints if x.yCoordinate == point.yCoordinate and x.xCoordinate > point.xCoordinate]
        adjacentPointstoLeftList = []
        adjacentPointstoRightList = []
        adjacentPointstoUpList = []
        adjacentPointstoDownList = []
        if len(sameRowPointstoLeftList) != 0:
            adjacentPointstoLeftList.append(max(sameRowPointstoLeftList, key = lambda x: x.yCoordinate))
        if len(sameRowPointstoRightList) != 0:
            adjacentPointstoRightList.append(min(sameRowPointstoRightList, key = lambda x: x.yCoordinate))
        if len(sameColumnPointstoUpList) != 0:
            adjacentPointstoUpList.append(max(sameColumnPointstoUpList, key = lambda x: x.xCoordinate))
        if len(sameColumnPointstoDownList) != 0:
            adjacentPointstoDownList.append(min(sameColumnPointstoDownList, key = lambda x: x.xCoordinate))
        adjacentPointsList = adjacentPointstoLeftList + adjacentPointstoRightList + adjacentPointstoUpList + adjacentPointstoDownList
        adjacentPointsIndexList = [self.listPoints.index(x) for x in adjacentPointsList]
        return adjacentPointsIndexList
    def setBridgeVariables(self):
        self.bridgeVars = [[self.model.addVar(vtype=GRB.INTEGER, name = f'bridge_{i}_{j}', ub = 2, lb = 0) for j in range(len(self.listPoints))] for i in range(len(self.listPoints))]
        self.bridgeVarsReflexiveConstraint = [[self.model.addConstr(self.bridgeVars[i][j] == self.bridgeVars[j][i]) for j in range(len(self.listPoints))] for i in range(len(self.listPoints))]
    def setBridgeCheckingVariable(self):
        self.bridgeCheckingVars = [[self.model.addVar(vtype=GRB.BINARY, name = f'bridgeChecking_{i}_{j}') for j in range(len(self.listPoints))] for i in range(len(self.listPoints))]
        self.bridgeCheckingVarsUpperConstraint = [[self.model.addConstr(self.bridgeVars[i][j] - self.bridgeCheckingVars[i][j] >= 0) for j in range(len(self.listPoints))] for i in range(len(self.listPoints))]
        self.bridgeCheckingVarsLowerConstraint = [[self.model.addConstr(2 * self.bridgeCheckingVars[i][j] - self.bridgeVars[i][j] >= 0) for j in range(len(self.listPoints))] for i in range(len(self.listPoints))]
    def setTotalBridgeConstraint(self):
        self.totalBridgeConstraint = [self.model.addConstr(sum([self.bridgeVars[i][j] for j in range(len(self.listPoints))]) == self.goalOrderList[i]) for i in range(len(self.listPoints))]
    def setNoIntersectionConstraint(self):
        # Set the constraint that no two bridges intersect inside.
        pass
    def CheckTheConnectivity(self):
        # Return True if the puzzle is connected.
        # Return False if the puzzle is not connected.
        pass
    def solve(self):
        self.model.setParam('OutputFlag', 0)
        self.setBridgeVariables()
        self.setBridgeCheckingVariable()
        self.setTotalBridgeConstraint()
        self.model.optimize()
        return None