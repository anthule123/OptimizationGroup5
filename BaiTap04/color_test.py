import unittest
from BaiTap04.Nhom05_BaiTap04_AnHung import *

class TestFunction(unittest.TestCase):
    def testColorProblem(self,N=5,k=2):
        colorProblem = ColorProblem(N, k)
        colorProblem.solve()
        #in ra danh sách các giá trị của x
        ans = []
        for i in range(0, k):
            ans.append([])
            for j in range(1, N+1):
                ans[i].append(colorProblem.x[i][j].x)
        print(ans)
    def test_ThreeSum(self):
        colorProblem = ColorProblem(5, 2)
        print(colorProblem.listOfThreeSum)
    def test_N26_k2(self):
        self.testColorProblem(26, 2)
    def test_N5_k2(self):
        self.testColorProblem(5, 2)