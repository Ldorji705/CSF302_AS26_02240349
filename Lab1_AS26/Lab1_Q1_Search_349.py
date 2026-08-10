import random
import time


# Linear Search
def linear_search_349(data_349, target_349):
    for i_349 in range(len(data_349)):
        if data_349[i_349] == target_349:
            return i_349
    return -1

# Binary Search
def binary_search_349(data_349, target_349):
    left_349 = 0
    right_349 = len(data_349) - 1
    while left_349 <= right_349:
        middle_349 = (left_349 + right_349) // 2
        if data_349[middle_349] == target_349:
            return middle_349
        elif data_349[middle_349] < target_349:
            left_349 = middle_349 + 1
        else:
            right_349 = middle_349 - 1
    return -1

# Input sizes
sizes_349 = [1000, 5000, 10000, 50000, 100000, 500000, 1000000]

# Number of runs
runs_349 = 5

for size_349 in sizes_349:

    # Generate random dataset
    data_349 = []
    for i_349 in range(size_349):
        data_349.append(random.randint(1, 1000000))
    # Select target
    target_349 = data_349[-1]
    # Linear Search
    total_linear_time_349 = 0
    for i_349 in range(runs_349):
        start_349 = time.perf_counter()
        linear_search_349(data_349, target_349)
        end_349 = time.perf_counter()
        total_linear_time_349 += end_349 - start_349
    average_linear_time_349 = total_linear_time_349 / runs_349

    # Sort before Binary Search
    data_349.sort()

    # Binary Search
    total_binary_time_349 = 0
    for i_349 in range(runs_349):
        start_349 = time.perf_counter()
        binary_search_349(data_349, target_349)
        end_349 = time.perf_counter()
        total_binary_time_349 += end_349 - start_349
    average_binary_time_349 = total_binary_time_349 / runs_349

    # Display results
    print("Input Size:", size_349)
    print("Linear Search Average Time:",
          average_linear_time_349, "seconds")
    print("Binary Search Average Time:",
          average_binary_time_349, "seconds")
    print("-----------------------------")