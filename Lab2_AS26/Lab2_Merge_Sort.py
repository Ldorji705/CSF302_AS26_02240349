import random
import time
import matplotlib.pyplot as plt

comparison_count_349 = 0

def merge_sort(arr_349):
    global comparison_count_349
    if len(arr_349) <= 1:
        return arr_349
    mid_349 = len(arr_349) // 2
    left_349 = merge_sort(arr_349[:mid_349])
    right_349 = merge_sort(arr_349[mid_349:])
    return merge(left_349, right_349)

def merge(left_349, right_349):
    global comparison_count_349
    result_349 = []
    i_349 = j_349 = 0
    while i_349 < len(left_349) and j_349 < len(right_349):
        comparison_count_349 += 1
        if left_349[i_349] <= right_349[j_349]:
            result_349.append(left_349[i_349]); i_349 += 1
        else:
            result_349.append(right_349[j_349]); j_349 += 1
    result_349.extend(left_349[i_349:])
    result_349.extend(right_349[j_349:])
    return result_349

def bubble_sort_descending(arr_349):
    a_349 = arr_349.copy()
    steps_349 = 0
    n_349 = len(a_349)
    for i_349 in range(n_349):
        for j_349 in range(0, n_349 - i_349 - 1):
            steps_349 += 1
            if a_349[j_349] < a_349[j_349+1]:
                a_349[j_349], a_349[j_349+1] = a_349[j_349+1], a_349[j_349]
    return a_349, steps_349

def main():
    arr_349 = []
    while True:
        print("\n----- MENU -----")
        print("1. Generate n random numbers")
        print("2. Display array")
        print("3. Sort ascending (Merge Sort)")
        print("4. Sort descending (Bubble Sort)")
        print("5. Time complexity - random data")
        print("6. Time complexity - already sorted data")
        print("7. Time complexity - descending sorted data")
        print("8. Exit")
        choice_349 = input("Enter choice: ")

        if choice_349 == '1':
            n_349 = int(input("Enter n: "))
            arr_349 = [random.randint(1, 1000) for _ in range(n_349)]
            print("Array generated.")

        elif choice_349 == '2':
            print("Array:", arr_349)

        elif choice_349 == '3':
            global comparison_count_349
            comparison_count_349 = 0
            sorted_arr_349 = merge_sort(arr_349)
            print("Sorted (ascending):", sorted_arr_349)
            print("Comparisons used:", comparison_count_349)

        elif choice_349 == '4':
            sorted_arr_349, steps_349 = bubble_sort_descending(arr_349)
            print("Sorted (descending):", sorted_arr_349)
            print("Comparisons used:", steps_349)

        elif choice_349 in ('5', '6', '7'):
            sizes_349 = [100, 500, 1000, 2000, 4000, 8000]
            times_349 = []
            for n_349 in sizes_349:
                if choice_349 == '5':
                    test_arr_349 = [random.randint(1, 100000) for _ in range(n_349)]
                elif choice_349 == '6':
                    test_arr_349 = list(range(n_349))
                else:
                    test_arr_349 = list(range(n_349, 0, -1))

                start_349 = time.time()
                merge_sort(test_arr_349)
                end_349 = time.time()
                times_349.append(end_349 - start_349)

            label_349 = {'5': 'Random Data', '6': 'Already Sorted', '7': 'Descending Sorted'}[choice_349]
            plt.plot(sizes_349, times_349, marker='o', label=label_349)
            plt.xlabel("Input size (n)")
            plt.ylabel("Time (seconds)")
            plt.title(f"Merge Sort Time Complexity - {label_349}")
            plt.legend()
            plt.grid(True)
            plt.savefig(f"merge_sort_{choice_349}.png")
            plt.show()
            print("Graph generated and saved.")

        elif choice_349 == '8':
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()