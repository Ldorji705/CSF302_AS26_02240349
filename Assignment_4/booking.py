
from itertools import combinations
from bisect import bisect_right


def greedy_earliest_finish(requests):
    """Select compatible bookings in earliest finishing order."""

    sorted_requests_349 = sorted(
        enumerate(requests),
        key=lambda item_349: (
            item_349[1][1],
            item_349[1][0],
            item_349[0]
        )
    )

    total_fee_349 = 0
    chosen_349 = []
    last_finish_349 = float("-inf")

    for index_349, request_349 in sorted_requests_349:
        start_349, finish_349, fee_349 = request_349

        if start_349 >= last_finish_349:
            chosen_349.append(index_349)
            total_fee_349 += fee_349
            last_finish_349 = finish_349

    return total_fee_349, chosen_349


def greedy_highest_fee(requests):
    """Select compatible bookings in highest fee order."""

    sorted_requests_349 = sorted(
        enumerate(requests),
        key=lambda item_349: (
            -item_349[1][2],
            item_349[1][1],
            item_349[1][0],
            item_349[0]
        )
    )

    total_fee_349 = 0
    chosen_349 = []
    selected_requests_349 = []

    for index_349, request_349 in sorted_requests_349:
        start_349, finish_349, fee_349 = request_349

        compatible_349 = all(
            finish_349 <= other_start_349
            or other_finish_349 <= start_349
            for other_start_349, other_finish_349
            in selected_requests_349
        )

        if compatible_349:
            chosen_349.append(index_349)
            selected_requests_349.append((start_349, finish_349))
            total_fee_349 += fee_349

    chosen_349.sort(
        key=lambda index_349: (
            requests[index_349][0],
            requests[index_349][1],
            index_349
        )
    )

    return total_fee_349, chosen_349


def best_schedule(requests):
    """Find the maximum total fee using dynamic programming."""

    if not requests:
        return 0, []

    sorted_requests_349 = sorted(
        enumerate(requests),
        key=lambda item_349: (
            item_349[1][1],
            item_349[1][0],
            item_349[0]
        )
    )

    number_349 = len(sorted_requests_349)

    finish_times_349 = [
        item_349[1][1] for item_349 in sorted_requests_349
    ]

    previous_349 = []

    for position_349 in range(number_349):
        start_349 = sorted_requests_349[position_349][1][0]

        previous_count_349 = bisect_right(
            finish_times_349,
            start_349,
            0,
            position_349
        )

        previous_349.append(previous_count_349)

    dp_349 = [0] * (number_349 + 1)

    for position_349 in range(1, number_349 + 1):
        fee_349 = sorted_requests_349[position_349 - 1][1][2]

        include_349 = (
            fee_349 + dp_349[previous_349[position_349 - 1]]
        )

        exclude_349 = dp_349[position_349 - 1]

        dp_349[position_349] = max(include_349, exclude_349)

    chosen_349 = []
    position_349 = number_349

    while position_349 > 0:
        fee_349 = sorted_requests_349[position_349 - 1][1][2]

        include_349 = (
            fee_349 + dp_349[previous_349[position_349 - 1]]
        )

        exclude_349 = dp_349[position_349 - 1]

        if include_349 > exclude_349:
            original_index_349 = sorted_requests_349[position_349 - 1][0]
            chosen_349.append(original_index_349)
            position_349 = previous_349[position_349 - 1]
        else:
            position_349 -= 1

    chosen_349.reverse()

    return dp_349[number_349], chosen_349


def brute_force(requests):
    """Check every possible subset to find the maximum total fee."""

    number_349 = len(requests)
    best_fee_349 = 0
    best_chosen_349 = []

    for subset_size_349 in range(number_349 + 1):
        for subset_349 in combinations(range(number_349), subset_size_349):

            selected_349 = sorted(
                subset_349,
                key=lambda index_349: (
                    requests[index_349][0],
                    requests[index_349][1],
                    index_349
                )
            )

            compatible_349 = True

            for position_349 in range(len(selected_349) - 1):
                current_index_349 = selected_349[position_349]
                next_index_349 = selected_349[position_349 + 1]

                current_finish_349 = requests[current_index_349][1]
                next_start_349 = requests[next_index_349][0]

                if current_finish_349 > next_start_349:
                    compatible_349 = False
                    break

            if compatible_349:
                total_fee_349 = sum(
                    requests[index_349][2]
                    for index_349 in subset_349
                )

                if total_fee_349 > best_fee_349:
                    best_fee_349 = total_fee_349
                    best_chosen_349 = list(selected_349)

    return best_fee_349, best_chosen_349


if __name__ == "__main__":
    requests_349 = [
        (9, 12, 3000),
        (10, 16, 8000),
        (13, 17, 4000),
        (12, 14, 2500),
        (16, 18, 2000)
    ]

    print("Booking the Hall - Example")
    print("Earliest finish:", greedy_earliest_finish(requests_349))
    print("Highest fee:", greedy_highest_fee(requests_349))
    print("Dynamic programming:", best_schedule(requests_349))
    print("Brute force:", brute_force(requests_349))
