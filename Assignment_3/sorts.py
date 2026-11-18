
import random


# Basic quicksort using the last element as pivot
def quicksort_basic(a):

    def partition_349(low_349, high_349):

        pivot_349 = a[high_349]

        i_349 = low_349 - 1

        # Move smaller elements to the left side
        for j_349 in range(low_349, high_349):

            if a[j_349] <= pivot_349:

                i_349 += 1

                a[i_349], a[j_349] = a[j_349], a[i_349]

        # Put the pivot in its correct position
        a[i_349 + 1], a[high_349] = (
            a[high_349], a[i_349 + 1]
        )

        return i_349 + 1

    def quicksort_recursive_349(low_349, high_349):

        if low_349 < high_349:

            pivot_index_349 = partition_349(
                low_349, high_349
            )

            quicksort_recursive_349(
                low_349, pivot_index_349 - 1
            )

            quicksort_recursive_349(
                pivot_index_349 + 1, high_349
            )

    quicksort_recursive_349(0, len(a) - 1)

    return a


# Insertion sort for small sections
def insertion_sort_349(a, low_349, high_349):

    for i_349 in range(low_349 + 1, high_349 + 1):

        key_349 = a[i_349]

        j_349 = i_349 - 1

        while j_349 >= low_349 and a[j_349] > key_349:

            a[j_349 + 1] = a[j_349]

            j_349 -= 1

        a[j_349 + 1] = key_349


# Improved quicksort using a random pivot
def quicksort_improved(a, cutoff=16):

    if cutoff < 1:
        raise ValueError("Cutoff must be at least 1.")

    def quicksort_recursive_349(low_349, high_349):

        while low_349 < high_349:

            # Use insertion sort for small sections
            if high_349 - low_349 + 1 <= cutoff:

                insertion_sort_349(
                    a, low_349, high_349
                )

                return

            # Choose a random pivot
            random_index_349 = random.randint(
                low_349, high_349
            )

            pivot_349 = a[random_index_349]

            # Three-way partitioning
            smaller_349 = low_349
            current_349 = low_349
            larger_349 = high_349

            while current_349 <= larger_349:

                if a[current_349] < pivot_349:

                    a[smaller_349], a[current_349] = (
                        a[current_349], a[smaller_349]
                    )

                    smaller_349 += 1
                    current_349 += 1

                elif a[current_349] > pivot_349:

                    a[current_349], a[larger_349] = (
                        a[larger_349], a[current_349]
                    )

                    larger_349 -= 1

                else:

                    current_349 += 1

            # Recursively sort the smaller section
            # and loop through the larger section
            left_size_349 = smaller_349 - low_349
            right_size_349 = high_349 - larger_349

            if left_size_349 < right_size_349:

                quicksort_recursive_349(
                    low_349, smaller_349 - 1
                )

                low_349 = larger_349 + 1

            else:

                quicksort_recursive_349(
                    larger_349 + 1, high_349
                )

                high_349 = smaller_349 - 1

    quicksort_recursive_349(0, len(a) - 1)

    return a


# Example to test both sorting algorithms
if __name__ == "__main__":

    numbers_349 = [
        500, 100, 300, 100, 500,
        200, 100, 400, 300, 500
    ]

    basic_numbers_349 = numbers_349.copy()
    improved_numbers_349 = numbers_349.copy()

    print("Original transactions:")
    print(numbers_349)

    print("\nBasic Quicksort:")
    print(quicksort_basic(basic_numbers_349))

    print("\nImproved Quicksort:")
    print(quicksort_improved(improved_numbers_349))
