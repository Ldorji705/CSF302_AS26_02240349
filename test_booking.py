
"""
CSF302 Assignment 4 - Booking the Hall
Name: Lhundup Dorji
Student ID: 02240349

Unit tests for the booking algorithms.
"""

import random
import unittest

from booking import (
    greedy_earliest_finish,
    greedy_highest_fee,
    best_schedule,
    brute_force
)


class TestBookingAlgorithms349(unittest.TestCase):

    def check_valid_schedule_349(self, requests_349, result_349):
        total_fee_349, chosen_349 = result_349

        self.assertTrue(
            all(0 <= index_349 < len(requests_349) for index_349 in chosen_349)
        )

        self.assertEqual(
            len(chosen_349),
            len(set(chosen_349))
        )

        calculated_fee_349 = sum(
            requests_349[index_349][2]
            for index_349 in chosen_349
        )

        self.assertEqual(total_fee_349, calculated_fee_349)

        selected_349 = sorted(
            [requests_349[index_349] for index_349 in chosen_349],
            key=lambda request_349: request_349[0]
        )

        for position_349 in range(len(selected_349) - 1):
            self.assertLessEqual(
                selected_349[position_349][1],
                selected_349[position_349 + 1][0]
            )

    def test_no_requests_349(self):
        requests_349 = []

        self.assertEqual(best_schedule(requests_349), (0, []))
        self.assertEqual(brute_force(requests_349), (0, []))
        self.assertEqual(greedy_earliest_finish(requests_349), (0, []))
        self.assertEqual(greedy_highest_fee(requests_349), (0, []))

    def test_one_request_349(self):
        requests_349 = [(9, 12, 3000)]

        self.assertEqual(best_schedule(requests_349), (3000, [0]))
        self.assertEqual(brute_force(requests_349), (3000, [0]))

    def test_all_overlapping_349(self):
        requests_349 = [
            (9, 15, 3000),
            (10, 16, 5000),
            (11, 14, 4000),
            (12, 17, 6000)
        ]

        self.assertEqual(best_schedule(requests_349)[0], 6000)
        self.assertEqual(brute_force(requests_349)[0], 6000)

    def test_none_overlapping_349(self):
        requests_349 = [
            (9, 10, 1000),
            (10, 11, 2000),
            (11, 12, 3000),
            (12, 13, 4000)
        ]

        self.assertEqual(best_schedule(requests_349)[0], 10000)
        self.assertEqual(brute_force(requests_349)[0], 10000)

    def test_back_to_back_requests_349(self):
        requests_349 = [
            (9, 12, 3000),
            (12, 14, 2500),
            (14, 16, 4000)
        ]

        self.assertEqual(best_schedule(requests_349)[0], 9500)
        self.assertEqual(brute_force(requests_349)[0], 9500)

    def test_500_random_inputs_349(self):
        random.seed(349)

        for test_number_349 in range(500):
            number_of_requests_349 = random.randint(0, 10)
            requests_349 = []

            for _349 in range(number_of_requests_349):
                start_349 = random.randint(0, 20)
                finish_349 = random.randint(start_349 + 1, 25)
                fee_349 = random.randint(100, 10000)

                requests_349.append(
                    (start_349, finish_349, fee_349)
                )

            dp_result_349 = best_schedule(requests_349)
            brute_result_349 = brute_force(requests_349)

            self.assertEqual(
                dp_result_349[0],
                brute_result_349[0],
                msg=(
                    f"Random test {test_number_349} failed: "
                    f"{requests_349}"
                )
            )

            self.check_valid_schedule_349(
                requests_349,
                dp_result_349
            )

    def test_equal_fees_greedy_is_optimal_349(self):
        random.seed(349)

        for test_number_349 in range(500):
            number_of_requests_349 = random.randint(0, 10)
            requests_349 = []

            for _349 in range(number_of_requests_349):
                start_349 = random.randint(0, 20)
                finish_349 = random.randint(start_349 + 1, 25)

                requests_349.append((start_349, finish_349, 1000))

            greedy_result_349 = greedy_earliest_finish(requests_349)
            optimal_result_349 = best_schedule(requests_349)

            self.assertEqual(
                greedy_result_349[0],
                optimal_result_349[0],
                msg=f"Equal-fee test failed: {requests_349}"
            )

            self.check_valid_schedule_349(
                requests_349,
                greedy_result_349
            )

    def test_greedy_schedules_are_valid_349(self):
        requests_349 = [
            (9, 12, 3000),
            (10, 16, 8000),
            (13, 17, 4000),
            (12, 14, 2500),
            (16, 18, 2000)
        ]

        self.check_valid_schedule_349(
            requests_349,
            greedy_earliest_finish(requests_349)
        )

        self.check_valid_schedule_349(
            requests_349,
            greedy_highest_fee(requests_349)
        )


if __name__ == "__main__":
    unittest.main()
