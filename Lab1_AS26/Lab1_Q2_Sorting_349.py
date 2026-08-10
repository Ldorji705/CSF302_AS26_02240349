import random
import time


# Bubble Sort
def bubble_sort_349(data_349):
    for i_349 in range(len(data_349)):
        for j_349 in range(len(data_349) - 1 - i_349):
            if data_349[j_349] > data_349[j_349 + 1]:
                temp_349 = data_349[j_349]
                data_349[j_349] = data_349[j_349 + 1]
                data_349[j_349 + 1] = temp_349

# Merge Sort
def merge_sort_349(data_349):
    if len(data_349) <= 1:
        return data_349
    middle_349 = len(data_349) // 2
    left_349 = merge_sort_349(data_349[:middle_349])
    right_349 = merge_sort_349(data_349[middle_349:])

    result_349 = []

    i_349 = 0
    j_349 = 0

    while i_349 < len(left_349) and j_349 < len(right_349):
        if left_349[i_349] < right_349[j_349]:
            result_349.append(left_349[i_349])
            i_349 += 1
        else:
            result_349.append(right_349[j_349])
            j_349 += 1

    result_349 += left_349[i_349:]
    result_349 += right_349[j_349:]
    return result_349

sizes_349 = [100, 500, 1000, 2000, 4000, 8000]
runs_349 = 5

for size_349 in sizes_349:
    # Generate random array
    data_349 = []
    for i_349 in range(size_349):
        data_349.append(random.randint(1, 100000))

    # Bubble Sort
    total_bubble_349 = 0
    for i_349 in range(runs_349):
        bubble_data_349 = data_349.copy()
        start_349 = time.perf_counter()
        bubble_sort_349(bubble_data_349)
        end_349 = time.perf_counter()
        total_bubble_349 += end_349 - start_349
    average_bubble_349 = total_bubble_349 / runs_349

    # Merge Sort
    total_merge_349 = 0
    for i_349 in range(runs_349):
        start_349 = time.perf_counter()
        merge_sort_349(data_349)
        end_349 = time.perf_counter()
        total_merge_349 += end_349 - start_349
    average_merge_349 = total_merge_349 / runs_349

    print("Input Size:", size_349)
    print("Bubble Sort:", average_bubble_349, "seconds")
    print("Merge Sort:", average_merge_349, "seconds")
    print("-------------------------")