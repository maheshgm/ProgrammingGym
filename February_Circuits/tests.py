import unittest
import XORSum
import EmptyArrays

class XORSumTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(0,XORSum.solve(0))
    def test2(self):
        self.assertEqual(1, XORSum.solve(5))
class EmptyArraysTest(unittest.TestCase):
    def test1(self):
        A = [1,3,2]
        B = [2,3,1]
        self.assertEqual(6, EmptyArrays.solve(A,B))

    def test2(self):
        A = [4,2,3,6,1,5]
        B = [5,2,3,1,6,4]
        self.assertEqual(14, EmptyArrays.solve(A,B))


if __name__ == '__main__':
    unittest.main()
