
"""
CSF302 Assignment 4 - Booking the Hall
Name: Lhundup Dorji
Student ID: 02240349

Part C: Experimental comparison of greedy algorithms.
"""

import csv
import random
from statistics import mean

from booking import (
    greedy_earliest_finish,
    greedy_highest_fee,
    best_schedule
)


def generate_requests_349(number_349):
    """Generate random booking requests."""

    requests_349 = []

    for _349 in range(number_349):
        start_349 = random.randint(0, 100)
        finish_349 = random.randint(start_349 + 1, 120)
        fee_349 = random.randint(100, 10000)

        requests_349.append(
            (start_349, finish_349, fee_349)
        )

    return requests_349


def run_analysis_349():
    """Compare both greedy algorithms with the optimal solution."""

    random.seed(349)

    number_of_trials_349 = 1000
    number_of_requests_349 = 50

    earliest_ratios_349 = []
    highest_fee_ratios_349 = []

    csv_rows_349 = []

    for trial_349 in range(1, number_of_trials_349 + 1):

        requests_349 = generate_requests_349(
            number_of_requests_349
        )

        earliest_result_349 = greedy_earliest_finish(requests_349)
        highest_result_349 = greedy_highest_fee(requests_349)
        optimal_result_349 = best_schedule(requests_349)

        optimal_fee_349 = optimal_result_349[0]

        earliest_ratio_349 = (
            earliest_result_349[0] / optimal_fee_349
        )

        highest_ratio_349 = (
            highest_result_349[0] / optimal_fee_349
        )

        earliest_ratios_349.append(earliest_ratio_349)
        highest_fee_ratios_349.append(highest_ratio_349)

        csv_rows_349.append([
            trial_349,
            optimal_fee_349,
            earliest_result_349[0],
            round(earliest_ratio_349, 6),
            highest_result_349[0],
            round(highest_ratio_349, 6)
        ])

    average_earliest_349 = mean(earliest_ratios_349)
    worst_earliest_349 = min(earliest_ratios_349)

    average_highest_349 = mean(highest_fee_ratios_349)
    worst_highest_349 = min(highest_fee_ratios_349)

    with open(
        "revenue_ratios.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as csv_file_349:

        csv_writer_349 = csv.writer(csv_file_349)

        csv_writer_349.writerow([
            "Trial",
            "Optimal Revenue",
            "Earliest Finish Revenue",
            "Earliest Finish Ratio",
            "Highest Fee Revenue",
            "Highest Fee Ratio"
        ])

        csv_writer_349.writerows(csv_rows_349)

    print("=" * 55)
    print("PART C: REVENUE RATIO EXPERIMENT")
    print("=" * 55)

    print("Number of trials:", number_of_trials_349)
    print("Bookings per trial:", number_of_requests_349)

    print("\nEARLIEST-FINISH GREEDY")
    print(
        f"Average revenue ratio: "
        f"{average_earliest_349:.4f} "
        f"({average_earliest_349 * 100:.2f}%)"
    )
    print(
        f"Worst revenue ratio: "
        f"{worst_earliest_349:.4f} "
        f"({worst_earliest_349 * 100:.2f}%)"
    )

    print("\nHIGHEST-FEE GREEDY")
    print(
        f"Average revenue ratio: "
        f"{average_highest_349:.4f} "
        f"({average_highest_349 * 100:.2f}%)"
    )
    print(
        f"Worst revenue ratio: "
        f"{worst_highest_349:.4f} "
        f"({worst_highest_349 * 100:.2f}%)"
    )

    print("\nCSV file saved as revenue_ratios.csv")
    print("=" * 55)


if __name__ == "__main__":
    run_analysis_349()
