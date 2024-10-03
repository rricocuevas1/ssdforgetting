import unittest

from pipage_rounding import pipage_rounding


class TestPipageRounding(unittest.TestCase):
    def test_no_fractional_values(self):
        result = pipage_rounding([0, 0, 0, 0], 4, 0)
        self.assertEqual(result, [])

    def test_all_fractional_values_one(self):
        result = pipage_rounding([1, 1, 1, 1], 4, 4)
        self.assertEqual(result, [0, 1, 2, 3])

    def test_fractional_values_sum_to_B(self):
        result = pipage_rounding([0.5, 0.5, 0.5, 0.5], 4, 2)
        self.assertEqual(len(result), 2)

    def test_fractional_values_sum_less_than_B(self):
        result = pipage_rounding([0.2, 0.2, 0.2, 0.2], 4, 1)
        self.assertEqual(len(result), 1)

    def test_fractional_values_sum_more_than_B(self):
        result = pipage_rounding([0.6, 0.6, 0.6, 0.6], 4, 2)
        self.assertEqual(len(result), 2)

    def test_fractional_values_with_zeros_and_ones(self):
        result = pipage_rounding([0, 1, 0.5, 0.5], 4, 2)
        self.assertEqual(len(result), 2)
        self.assertIn(1, result)
