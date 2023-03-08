import Nhom05_Baitap02
import unittest


## Bai 1:
# 1)
# Hàm trả về tất cả các ô cờ vua có thể có
class TestGetAllCoordinates(unittest.TestCase):
    def test_getAllCoordinates(self):
        ans = Nhom05_Baitap02.getAllCoordinates()
        #assert equal
        self.assertEqual(ans, ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8'])

    def test_getAllWhiteCells(self):
        ans = Nhom05_Baitap02.getAllWhiteCells()
        #assert equal trong đó a2 là trắng
        self.assertEqual(ans,['a2', 'a4', 'a6', 'a8', 'b1', 'b3', 'b5', 'b7', 'c2', 'c4', 'c6', 'c8', 'd1', 'd3', 'd5', 'd7', 'e2', 'e4', 'e6', 'e8', 'f1', 'f3', 'f5', 'f7', 'g2', 'g4', 'g6', 'g8', 'h1', 'h3', 'h5', 'h7'])

    def test_printChessboard(self):
        ans = Nhom05_Baitap02.printChessboard()

class TestGetQueenNextPossiblePositions(unittest.TestCase):
    def test_getQueenNextPossiblePositions(self):
        ans = Nhom05_Baitap02.getQueenNextPossiblePositions('d6')
        listExpectation = ['d1', 'd2', 'd3', 'd4', 'd5', 'd7', 'd8',
                            'a6', 'b6', 'c6', 'e6', 'f6', 'g6', 'h6',
                              'a3', 'b4', 'c5', 'e7', 'f8',
                                'b8', 'c7', 'e5', 'f4', 'g3', 'h2']
        self.assertEqual(set(ans), set(listExpectation))