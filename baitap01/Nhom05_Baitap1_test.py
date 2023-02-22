
import unittest

from Nhom05_Baitap1 import getDivisorList

class TestGetDivisors(unittest.TestCase):
    def testNumber(self, n = 5):
        ans =  getDivisorList(n)
        print(ans)
    def testNumber1(self):
        self.testNumber(1)
    def testNumber2(self):
        self.testNumber(2)
    def testNumber3(self):
        self.testNumber(3)
    def testNumber20(self):
        self.testNumber(20)
    def testNumber100(self):
        self.testNumber(100)

    