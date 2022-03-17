import unittest
import ChefAndWaterBottles
import BalancedReversals

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

class BalancedReversalsTest(unittest.TestCase):
    def test1(self):
        length = 5
        bin_str = '01100'
        min_bin_str = '00011'

        self.assertEqual(min_bin_str, BalancedReversals.solve(bin_str, length))

    def test2(self):
        length = 4
        bin_str = '0000'
        min_bin_str = '0000'

        self.assertEqual(min_bin_str, BalancedReversals.solve(bin_str, length))


if __name__ == '__main__':
    unittest.main()
