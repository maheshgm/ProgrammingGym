import unittest
import XORSum

class XORSumTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(0,XORSum.solve(0))
    def test2(self):
        self.assertEqual(1, XORSum.solve(5))

if __name__ == '__main__':
    unittest.main()
