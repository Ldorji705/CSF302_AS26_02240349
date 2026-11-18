
import unittest
import random

from closest import closest_pair
from closest import closest_pair_brute


class TestClosestPair_349(unittest.TestCase):

    # Test 1: Exactly two points
    def test_two_points_349(self):

        points_349 = [
            (0, 0),
            (3, 4)
        ]

        result_349 = closest_pair(points_349)

        self.assertEqual(result_349, (5.0, 0, 1))

    # Test 2: Duplicate points
    def test_duplicate_points_349(self):

        points_349 = [
            (1, 2),
            (5, 6),
            (1, 2)
        ]

        result_349 = closest_pair(points_349)

        self.assertEqual(result_349, (0.0, 0, 2))

    # Test 3: All points on one vertical line
    def test_vertical_line_349(self):

        points_349 = [
            (5, 1),
            (5, 8),
            (5, 3),
            (5, 12),
            (5, 4)
        ]

        result_349 = closest_pair(points_349)

        self.assertEqual(result_349, (1.0, 2, 4))

    # Test 4: Closest pair on opposite sides
    def test_opposite_sides_349(self):

        points_349 = [
            (0, 0),
            (2, 4),
            (2.5, 0),
            (5, 4)
        ]

        result_349 = closest_pair(points_349)

        self.assertEqual(result_349, (2.5, 0, 2))

    # Test 5: 500 random inputs
    def test_random_points_349(self):

        random.seed(349)

        for test_number_349 in range(500):

            # Generate between 2 and 50 points.
            n_349 = random.randint(2, 50)

            points_349 = []

            for i_349 in range(n_349):

                x_349 = random.randint(-1000, 1000)
                y_349 = random.randint(-1000, 1000)

                points_349.append((x_349, y_349))

            # Compare both algorithms.
            brute_result_349 = closest_pair_brute(points_349)

            divide_result_349 = closest_pair(points_349)

            self.assertEqual(
                divide_result_349,
                brute_result_349,
                "Random test failed"
            )

    # Test 6: Many duplicate points
    def test_many_duplicates_349(self):

        points_349 = [(4, 4)] * 20

        result_349 = closest_pair(points_349)

        self.assertEqual(result_349, (0.0, 0, 1))


if __name__ == "__main__":

    unittest.main(verbosity=2)
