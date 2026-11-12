# Lab 5 - Q1: Quicksort Variants
import random
import time

count_349 = 0    # comparison counter


# Lomuto partition (pivot = last element)
def lomuto_349(a_349, lo_349, hi_349):
    global count_349
    pivot_349 = a_349[hi_349]
    i_349 = lo_349 - 1                           # end of "<= pivot" zone
    for j_349 in range(lo_349, hi_349):
        count_349 += 1
        if a_349[j_349] <= pivot_349:
            i_349 += 1
            a_349[i_349], a_349[j_349] = a_349[j_349], a_349[i_349]
    a_349[i_349 + 1], a_349[hi_349] = a_349[hi_349], a_349[i_349 + 1]    # pivot to final place
    return i_349, i_349 + 2                      # left ends at i, right starts at i+2


# Hoare partition (pivot = middle element)
def hoare_349(a_349, lo_349, hi_349):
    global count_349
    pivot_349 = a_349[(lo_349 + hi_349) // 2]
    i_349 = lo_349 - 1
    j_349 = hi_349 + 1
    while True:
        i_349 += 1                           # move i right
        count_349 += 1
        while a_349[i_349] < pivot_349:
            i_349 += 1
            count_349 += 1
        j_349 -= 1                           # move j left
        count_349 += 1
        while a_349[j_349] > pivot_349:
            j_349 -= 1
            count_349 += 1
        if i_349 >= j_349:
            return j_349, j_349 + 1              # left ends at j, right starts at j+1
        a_349[i_349], a_349[j_349] = a_349[j_349], a_349[i_349]


# Randomised: random pivot, then Lomuto
def randomised_349(a_349, lo_349, hi_349):
    r_349 = random.randint(lo_349, hi_349)
    a_349[r_349], a_349[hi_349] = a_349[hi_349], a_349[r_349]            # move random pivot to the end
    return lomuto_349(a_349, lo_349, hi_349)


# Three-way (Dutch national flag): [ < pivot | == pivot | > pivot ]
def three_way_349(a_349, lo_349, hi_349):
    global count_349
    pivot_349 = a_349[(lo_349 + hi_349) // 2]
    lt_349 = lo_349                              # a[lo..lt-1]  < pivot
    i_349 = lo_349                               # a[lt..i-1]  == pivot
    gt_349 = hi_349                              # a[gt+1..hi]  > pivot
    while i_349 <= gt_349:
        count_349 += 1
        if a_349[i_349] < pivot_349:
            a_349[lt_349], a_349[i_349] = a_349[i_349], a_349[lt_349]
            lt_349 += 1
            i_349 += 1
        else:
            count_349 += 1
            if a_349[i_349] > pivot_349:
                a_349[i_349], a_349[gt_349] = a_349[gt_349], a_349[i_349]
                gt_349 -= 1
            else:                        # equal: leave in middle
                i_349 += 1
    return lt_349 - 1, gt_349 + 1


# driver: recurse on SMALLER part, loop on LARGER part
def quicksort_349(a_349, lo_349, hi_349, partition_349):
    while lo_349 < hi_349:
        left_end_349, right_start_349 = partition_349(a_349, lo_349, hi_349)
        if left_end_349 - lo_349 < hi_349 - right_start_349:
            quicksort_349(a_349, lo_349, left_end_349, partition_349)       # left is smaller
            lo_349 = right_start_349
        else:
            quicksort_349(a_349, right_start_349, hi_349, partition_349)    # right is smaller
            hi_349 = left_end_349


# make test data
def make_input_349(kind_349, n_349):
    if kind_349 == "random":
        return [random.randint(0, 1000000) for _ in range(n_349)]
    if kind_349 == "sorted":
        return list(range(n_349))
    if kind_349 == "reverse":
        return list(range(n_349, 0, -1))
    return [random.randint(0, 9) for _ in range(n_349)]     # duplicates


variants_349 = {"Lomuto": lomuto_349, "Hoare": hoare_349,
            "Randomised": randomised_349, "Three-way": three_way_349}
sizes_349 = [1000, 2000, 4000, 8000, 16000]

for kind_349 in ["random", "sorted", "reverse", "duplicates"]:
    print("\nInput:", kind_349, "  (comparisons and seconds)")
    print("n      ", "".join(f"{name_349:^22}" for name_349 in variants_349))
    for n_349 in sizes_349:
        data_349 = make_input_349(kind_349, n_349)
        row_349 = f"{n_349:<7}"
        for name_349, partition_349 in variants_349.items():
            a_349 = data_349[:]                  # fresh copy
            count_349 = 0
            start_349 = time.perf_counter()
            quicksort_349(a_349, 0, n_349 - 1, partition_349)
            secs_349 = time.perf_counter() - start_349
            assert a_349 == sorted(data_349)     # check result
            row_349 += f"{count_349:>13,} {secs_349:>7.3f}s "
        print(row_349)

print("""
Which variant is Theta(n^2), and why:
- Lomuto (last pivot) on sorted and reverse input: pivot is always the
  max or min, so every split is 0 and n-1.
- Lomuto and Randomised on many duplicates: equal values all go to one
  side, so each group of equal values is sorted slowly (random pivot
  does not help).
- Hoare: stops on equal values and uses a middle pivot, so it stays n log n.
- Three-way: removes all equal values at once, best on duplicates.""")