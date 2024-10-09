import unittest
import numpy as np

from query_based_amnesia import compute_frequency, query_based_amnesia


class TestComputeFrequency(unittest.TestCase):
    def test_no_queries(self):
        result = compute_frequency(5, [])
        expected = np.zeros(5, dtype=int)
        np.testing.assert_array_equal(result, expected)

    def test_single_query(self):
        result = compute_frequency(5, [[1]])
        expected = np.array([0, 1, 0, 0, 0])
        np.testing.assert_array_equal(result, expected)

    def test_multiple_queries(self):
        result = compute_frequency(5, [[1], [3]])
        expected = np.array([0, 1, 0, 1, 0])
        np.testing.assert_array_equal(result, expected)

    def test_overlapping_queries(self):
        result = compute_frequency(5, [[1], [1], [3]])
        expected = np.array([0, 2, 0, 1, 0])
        np.testing.assert_array_equal(result, expected)


class TestQueryBasedAmnesia(unittest.TestCase):
    # TODO: Uncomment this test case when the error handling is implemented
    # def test_no_queries(self):
    #     result = query_based_amnesia(5, 3, [])
    #     # With no queries, the result should be empty or some error handling could be checked
    #     self.assertEqual(result, [])

    def test_budget_zero(self):
        result = query_based_amnesia(5, 0, [[1], [2]])
        self.assertEqual(result, [])

    def test_budget_larger_than_indices(self):
        with self.assertRaises(ValueError):
            query_based_amnesia(5, 6, [[0], [1], [2]])

    def test_valid_query_selection(self):
        queries = [[0], [1], [2], [3]]
        budget = 2
        result = query_based_amnesia(4, budget, queries)
        self.assertEqual(len(result), budget)
        for index in result:
            self.assertIn(index, range(4))  # Check that selected indices are within valid range


if __name__ == '__main__':
    unittest.main()
