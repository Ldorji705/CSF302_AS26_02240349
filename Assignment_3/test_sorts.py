
import unittest
import random

from sorts import quicksort_basic, quicksort_improved


class TestSortingAlgorithms349(unittest.TestCase):

    # Test both algorithms using the same input
    def check_both_sorts_349(self, numbers_349):

        expected_349 = sorted(numbers_349)

        # Test basic quicksort
        basic_list_349 = numbers_349.copy()

        basic_result_349 = quicksort_basic(basic_list_349)

        self.assertEqual(basic_result_349, expected_349)
        self.assertEqual(basic_list_349, expected_349)

        # Test improved quicksort
        improved_list_349 = numbers_349.copy()

        improved_result_349 = quicksort_improved(improved_list_349)

        self.assertEqual(improved_result_349, expected_349)
        self.assertEqual(improved_list_349, expected_349)

    # Test 500 random lists
    def test_500_random_lists_349(self):

        random.seed(349)

        for i_349 in range(500):

            size_349 = random.randint(0, 50)

            numbers_349 = [
                random.randint(-1000, 1000)
                for j_349 in range(size_349)
            ]

            with self.subTest(test_number=i_349):
                self.check_both_sorts_349(numbers_349)

    # Test an empty list
    def test_empty_list_349(self):

        self.check_both_sorts_349([])

    # Test a list containing one element
    def test_one_element_349(self):

        self.check_both_sorts_349([100])

    # Test a list containing equal values
    def test_all_equal_349(self):

        self.check_both_sorts_349([500] * 100)

    # Test an already sorted list
    def test_already_sorted_349(self):

        numbers_349 = list(range(100))

        self.check_both_sorts_349(numbers_349)

    # Test a reverse sorted list
    def test_reverse_sorted_349(self):

        numbers_349 = list(range(100, 0, -1))

        self.check_both_sorts_349(numbers_349)

    # Test negative numbers
    def test_negative_numbers_349(self):

        numbers_349 = [
            -50, -10, -100, -5, 0,
            10, -25, 50, -1, 25
        ]

        self.check_both_sorts_349(numbers_349)


if __name__ == "__main__":

    unittest.main(verbosity=2)
