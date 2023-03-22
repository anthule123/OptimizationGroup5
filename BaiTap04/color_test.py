import unittest
from BaiTap04.Nhom05_BaiTap04_AnHung import *
import gurobipy as gp
class TestFunction(unittest.TestCase):
    def testColorProblem(self,N=5,k=2):
        colorProblem = ColorProblem(N, k)
        colorProblem.solve()
        

    def test_ThreeSum(self):
        colorProblem = ColorProblem(5, 2)
        print(colorProblem.listOfThreeSum)
    def test_N26_k2(self):
        self.testColorProblem(26, 2)
    def test_N5_k2(self):
        self.testColorProblem(5, 2)
    def test_N8_k2(self):
        self.testColorProblem(8, 2)
    def test_N9_k2(self):
        self.testColorProblem(9, 2)
