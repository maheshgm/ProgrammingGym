import unittest
import ChefAndWaterBottles

class ChefAndWaterBottlesTest(unittest.TestCase):
    def test1(self):
        N,X,K = 5,2,8
        result = 4
        self.assertEqual(result, ChefAndWaterBottles.solve(N,X,K))

    def test2(self):
        N,X,K = 10,5,4
        result = 0
        self.assertEqual(result, ChefAndWaterBottles.solve(N,X,K))

    def test3(self):
        N,X,K = 3,1,4
        result = 3
        self.assertEqual(result, ChefAndWaterBottles.solve(N,X,K))



if __name__ == '__main__':
    unittest.main()
