# Same as section 1, except we change the expected value to induce failure

import unittest
from my_calculations import Calculations

class TestCalculations(unittest.TestCase):

    def test_sum(self):
        calculation = Calculations(8, 2)
        self.assertEqual(calculation.get_sum(), 11, 'The sum is wrong')

if __name__ == '__main__':
    unittest.main()