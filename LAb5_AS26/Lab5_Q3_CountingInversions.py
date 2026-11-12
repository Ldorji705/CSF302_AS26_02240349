# CSF302_AS26_02240349 - Lab5_Q3_CountingInversions
# Lab 5 - Q3: Counting Inversions
# inversion = pair (i, j) with i < j but a[i] > a[j]
import random
import time


# brute force: check every pair, O(n^2)
def inversions_brute_349(a_349):
    total_349 = 0
    for i_349 in range(len(a_349)):
        for j_349 in range(i_349 + 1, len(a_349)):
            if a_349[i_349] > a_349[j_349]:
                total_349 += 1
    return total_349


# merge sort that also counts, O(n log n). Returns (sorted list, count)
def inversions_merge_349(a_349):
    if len(a_349) <= 1:
        return a_349, 0
    mid_349 = len(a_349) // 2
    left_349, count_left_349 = inversions_merge_349(a_349[:mid_349])
    right_349, count_right_349 = inversions_merge_349(a_349[mid_349:])
    out_349 = []
    i_349 = 0
    j_349 = 0
    cross_349 = 0                            # inversions between the halves
    while i_349 < len(left_349) and j_349 < len(right_349):
        if left_349[i_349] <= right_349[j_349]:
            out_349.append(left_349[i_349])
            i_349 += 1
        else:
            out_349.append(right_349[j_349])
            j_349 += 1
            cross_349 += len(left_349) - i_349       # right[j] < all remaining left items
    out_349 += left_349[i_349:] + right_349[j_349:]
    return out_349, count_left_349 + count_right_349 + cross_349


# check both methods agree
same_349 = True
for n_349 in [0, 1, 2, 10, 100, 500, 1000, 2000]:
    a_349 = [random.randint(0, 50) for _ in range(n_349)]
    if inversions_brute_349(a_349) != inversions_merge_349(a_349)[1]:
        same_349 = False
print("Both methods agree?", same_349)

# timing (skip brute force if it would pass 60 seconds)
print("\nn          brute        merge")
last_n_349 = 0
last_time_349 = 0
for n_349 in [1000, 10000, 100000, 1000000]:
    a_349 = [random.randint(0, 1000000) for _ in range(n_349)]

    start_349 = time.perf_counter()
    inversions_merge_349(a_349)
    t_merge_349 = time.perf_counter() - start_349

    # brute force time grows like n^2: predict from last run
    if last_n_349 > 0 and last_time_349 * (n_349 / last_n_349) ** 2 > 60:
        brute_349 = "> 60s (skip)"
    else:
        start_349 = time.perf_counter()
        inversions_brute_349(a_349)
        last_time_349 = time.perf_counter() - start_349
        last_n_349 = n_349
        brute_349 = f"{last_time_349:.3f}"
    print(f"{n_349:<10} {brute_349:<12} {t_merge_349:.3f}")

# Kendall tau distance between two users' rankings of 10 movies
print("\nRank 10 movies. Type 10 numbers (1-10, each once): the rank you")
print("give to movie 1, movie 2, ..., movie 10.")


def read_ranking_349(user_349):
    while True:
        text_349 = input("User " + str(user_349) + ": ")
        ranks_349 = [int(x_349) for x_349 in text_349.split() if x_349.isdigit()]
        if sorted(ranks_349) == list(range(1, 11)):
            return ranks_349
        print("Enter each number from 1 to 10 exactly once.")


rank1_349 = read_ranking_349(1)
rank2_349 = read_ranking_349(2)

# list movies in user 1's order, then look at user 2's ranks in that order
order_349 = sorted(range(10), key=lambda m_349: rank1_349[m_349])
sequence_349 = [rank2_349[m_349] for m_349 in order_349]
distance_349 = inversions_merge_349(sequence_349)[1]   # each inversion = 1 disagreement
print("\nKendall tau distance:", distance_349, "out of 45 pairs")
print("Similarity:", round(100 * (1 - distance_349 / 45)), "%")