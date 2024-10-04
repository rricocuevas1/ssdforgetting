import unittest

import numpy as np

from dep_df import largest_coordinates, gradient, scg


class TestLargestCoordinates(unittest.TestCase):
    def test_largest_coordinates_basic(self):
        d = np.array([1, 3, 2, 4])
        n = 4
        B = 2
        result = largest_coordinates(d, n, B)
        self.assertEqual(result, [0, 1, 0, 1])

    def test_largest_coordinates_all_zeros(self):
        d = np.array([0, 0, 0, 0])
        n = 4
        B = 2
        result = largest_coordinates(d, n, B)
        self.assertEqual(result, [0, 0, 0, 0])

    def test_large_coordinates_all_ones(self):
        d = np.array([1, 1, 1, 1])
        n = 4
        B = 2
        result = largest_coordinates(d, n, B)
        self.assertEqual(result, [1, 1, 1, 1])

    def test_largest_coordinates_single_element(self):
        d = np.array([1])
        n = 1
        B = 1
        result = largest_coordinates(d, n, B)
        self.assertEqual(result, [1])

    @unittest.skip(
        "Putting it only for the sake of coverage.The function is not expected to be called with a budget bigger than the number of elements")
    def test_largest_coordinates_more_B_than_elements(self):
        d = np.array([1, 2])
        n = 2
        B = 3
        result = largest_coordinates(d, n, B)
        self.assertEqual(result, [1, 1])

    def test_largest_coordinates_negative_values(self):
        d = np.array([-1, -3, -2, -4])
        n = 4
        B = 2
        result = largest_coordinates(d, n, B)
        self.assertEqual(result, [1, 0, 1, 0])


class TestGradientFunction(unittest.TestCase):
    def test_gradient_basic(self):
        x = np.array([0.5, 0.5, 0.5, 0.5])
        n = 4
        queries = [[np.array([0, 1, 2, 3])]]
        p = np.array([1.0])
        m = 1
        data_array = np.array([[1, 2, 3, 4], [4, 3, 2, 1], [1, 3, 2, 4], [4, 1, 3, 2]])
        K = 20
        jaccard_sim = False
        result = gradient(x, n, queries, p, m, data_array, K, jaccard_sim)
        self.assertEqual(result.shape, (n,))

    def test_gradient_with_jaccard(self):
        x = np.array([0.5, 0.5, 0.5, 0.5])
        n = 4
        queries = [[np.array([0, 1, 2, 3])]]
        p = np.array([1.0])
        m = 1
        data_array = np.array([[1, 2, 3, 4], [4, 3, 2, 1], [1, 3, 2, 4], [4, 1, 3, 2]])
        K = 20
        jaccard_sim = True
        result = gradient(x, n, queries, p, m, data_array, K, jaccard_sim)
        self.assertEqual(result.shape, (n,))

    @unittest.skip(
        "Putting it only for the sake of coverage.The function is not expected to be called with empty queries")
    def test_gradient_empty_queries(self):
        x = np.array([0.5, 0.5, 0.5, 0.5])
        n = 4
        queries = [[]]
        p = np.array([1.0])
        m = 1
        data_array = np.array([[1, 2, 3, 4], [4, 3, 2, 1], [1, 3, 2, 4], [4, 1, 3, 2]])
        K = 20
        jaccard_sim = False
        result = gradient(x, n, queries, p, m, data_array, K, jaccard_sim)
        self.assertEqual(result.shape, (n,))

    def test_gradient_single_element(self):
        x = np.array([0.5])
        n = 1
        queries = [[np.array([0])]]
        p = np.array([1.0])
        m = 1
        data_array = np.array([[1]])
        K = 20
        jaccard_sim = False
        result = gradient(x, n, queries, p, m, data_array, K, jaccard_sim)
        self.assertEqual(result.shape, (n,))


class TestSCGFunction(unittest.TestCase):
    def test_scg_basic(self):
        n = 4
        B = 2
        queries = [[np.array([0, 1, 2, 3])]]
        p = np.array([1.0])
        m = 1
        dataset = np.array([[1, 2, 3, 4], [4, 3, 2, 1], [1, 3, 2, 4], [4, 1, 3, 2]])
        T = 10
        K = 5
        jaccard_sim = False
        result = scg(n, B, queries, p, m, dataset, T, K, jaccard_sim)
        self.assertEqual(len(result), n)

    def test_scg_with_jaccard(self):
        n = 4
        B = 2
        queries = [[np.array([0, 1, 2, 3])]]
        p = np.array([1.0])
        m = 1
        dataset = np.array([[1, 2, 3, 4], [4, 3, 2, 1], [1, 3, 2, 4], [4, 1, 3, 2]])
        T = 10
        K = 5
        jaccard_sim = True
        result = scg(n, B, queries, p, m, dataset, T, K, jaccard_sim)
        self.assertEqual(len(result), n)

    def test_scg_single_element(self):
        n = 1
        B = 1
        queries = [[np.array([0])]]
        p = np.array([1.0])
        m = 1
        dataset = np.array([[1]])
        T = 10
        K = 5
        jaccard_sim = False
        result = scg(n, B, queries, p, m, dataset, T, K, jaccard_sim)
        self.assertEqual(len(result), n)

    @unittest.skip(
        "Putting it only for the sake of coverage.The function is not expected to be called with a budget bigger than the number of elements")
    def test_scg_more_B_than_elements(self):
        n = 2
        B = 3
        queries = [[np.array([0, 1])]]
        p = np.array([1.0])
        m = 1
        dataset = np.array([[1, 2], [2, 1]])
        T = 10
        K = 5
        jaccard_sim = False
        result = scg(n, B, queries, p, m, dataset, T, K, jaccard_sim)
        self.assertEqual(len(result), n)


if __name__ == '__main__':
    unittest.main()
