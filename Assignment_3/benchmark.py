
import random
import time
import csv
import statistics
import matplotlib.pyplot as plt

from sorts import quicksort_basic, quicksort_improved


# Settings
SIZES_349 = [1000, 2000, 4000, 8000, 16000, 32000, 64000]
CUTOFFS_349 = [1, 4, 8, 16, 32, 64]
REPEATS_349 = 3


# Measure the running time of a sorting algorithm
def measure_time_349(sort_function_349, numbers_349):

    times_349 = []

    for repeat_349 in range(REPEATS_349):

        test_list_349 = numbers_349.copy()

        start_349 = time.perf_counter()

        try:
            sort_function_349(test_list_349)

            end_349 = time.perf_counter()

            times_349.append(end_349 - start_349)

        except RecursionError:

            return None

    return statistics.median(times_349)


# Create the three types of input data
def create_data_349(size_349):

    random_data_349 = [
        random.randint(0, 1000000)
        for i_349 in range(size_349)
    ]

    sorted_data_349 = sorted(random_data_349)

    duplicate_data_349 = [
        random.randint(0, 9)
        for i_349 in range(size_349)
    ]

    return {
        "Random": random_data_349,
        "Already sorted": sorted_data_349,
        "Many duplicates": duplicate_data_349
    }


# Part C: Compare basic and improved quicksort
def run_main_benchmark_349():

    print("\nPART C: QUICKSORT PERFORMANCE COMPARISON")
    print("=" * 65)

    results_349 = []

    for size_349 in SIZES_349:

        print(f"\nTesting list size: {size_349:,}")

        datasets_349 = create_data_349(size_349)

        for data_name_349, numbers_349 in datasets_349.items():

            basic_time_349 = measure_time_349(
                quicksort_basic, numbers_349
            )

            improved_time_349 = measure_time_349(
                quicksort_improved, numbers_349
            )

            basic_status_349 = (
                "Success" if basic_time_349 is not None
                else "RecursionError"
            )

            improved_status_349 = (
                "Success" if improved_time_349 is not None
                else "RecursionError"
            )

            results_349.append([
                data_name_349,
                size_349,
                basic_time_349,
                basic_status_349,
                improved_time_349,
                improved_status_349
            ])

            basic_display_349 = (
                f"{basic_time_349:.6f} seconds"
                if basic_time_349 is not None
                else "RecursionError"
            )

            improved_display_349 = (
                f"{improved_time_349:.6f} seconds"
                if improved_time_349 is not None
                else "RecursionError"
            )

            print(f"  Data type: {data_name_349}")
            print(f"  Basic:    {basic_display_349}")
            print(f"  Improved: {improved_display_349}")

    # Save the results to CSV
    with open(
        "benchmark_results.csv",
        "w",
        newline=""
    ) as file_349:

        writer_349 = csv.writer(file_349)

        writer_349.writerow([
            "Data Type",
            "List Size",
            "Basic Time",
            "Basic Status",
            "Improved Time",
            "Improved Status"
        ])

        writer_349.writerows(results_349)

    # Create a separate graph for each input type
    for data_name_349 in [
        "Random",
        "Already sorted",
        "Many duplicates"
    ]:

        basic_sizes_349 = []
        basic_times_349 = []

        improved_sizes_349 = []
        improved_times_349 = []

        for row_349 in results_349:

            if row_349[0] == data_name_349:

                if row_349[2] is not None:

                    basic_sizes_349.append(row_349[1])
                    basic_times_349.append(row_349[2])

                if row_349[4] is not None:

                    improved_sizes_349.append(row_349[1])
                    improved_times_349.append(row_349[4])

        plt.figure(figsize=(9, 5))

        if basic_sizes_349:
            plt.plot(
                basic_sizes_349,
                basic_times_349,
                marker="o",
                label="Basic Quicksort"
            )

        if improved_sizes_349:
            plt.plot(
                improved_sizes_349,
                improved_times_349,
                marker="s",
                label="Improved Quicksort"
            )

        plt.title(f"Quicksort Performance: {data_name_349}")
        plt.xlabel("Number of Elements")
        plt.ylabel("Time (seconds)")
        plt.xscale("log", base=2)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        filename_349 = (
            data_name_349.lower()
            .replace(" ", "_")
        )

        plt.savefig(
            f"{filename_349}_performance.png"
        )

        plt.close()

    print("\nMain benchmark completed.")
    print("Results saved in benchmark_results.csv")
    print("Three performance graphs have been created.")


# Part C: Find the best insertion sort cutoff
def run_cutoff_benchmark_349():

    print("\nCUTOFF EXPERIMENT")
    print("=" * 65)

    random_data_349 = [
        random.randint(0, 1000000)
        for i_349 in range(100000)
    ]

    cutoff_results_349 = []

    for cutoff_349 in CUTOFFS_349:

        sorting_function_349 = (
            lambda numbers_349, c_349=cutoff_349:
            quicksort_improved(numbers_349, cutoff=c_349)
        )

        elapsed_349 = measure_time_349(
            sorting_function_349,
            random_data_349
        )

        cutoff_results_349.append([
            cutoff_349,
            elapsed_349
        ])

        print(
            f"Cutoff {cutoff_349}: "
            f"{elapsed_349:.6f} seconds"
        )

    # Find the fastest cutoff
    best_cutoff_349, best_time_349 = min(
        cutoff_results_349,
        key=lambda result_349: result_349[1]
    )

    # Measure Python's built-in sorted()
    python_time_349 = measure_time_349(
        sorted,
        random_data_349
    )

    # Save cutoff results
    with open(
        "cutoff_results.csv",
        "w",
        newline=""
    ) as file_349:

        writer_349 = csv.writer(file_349)

        writer_349.writerow([
            "Cutoff",
            "Improved Quicksort Time"
        ])

        writer_349.writerows(cutoff_results_349)

    # Create cutoff graph
    plt.figure(figsize=(9, 5))

    plt.plot(
        [row_349[0] for row_349 in cutoff_results_349],
        [row_349[1] for row_349 in cutoff_results_349],
        marker="o"
    )

    plt.title("Effect of Insertion Sort Cutoff")
    plt.xlabel("Cutoff Value")
    plt.ylabel("Time (seconds)")
    plt.xticks(CUTOFFS_349)
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("cutoff_comparison.png")
    plt.close()

    print("\nBEST CUTOFF RESULT")
    print("-" * 40)
    print(f"Best cutoff: {best_cutoff_349}")
    print(f"Improved quicksort: {best_time_349:.6f} seconds")
    print(f"Python sorted():    {python_time_349:.6f} seconds")

    print("\nCutoff experiment completed.")
    print("Results saved in cutoff_results.csv")
    print("Graph saved as cutoff_comparison.png")


if __name__ == "__main__":

    random.seed(349)

    run_main_benchmark_349()

    run_cutoff_benchmark_349()
