
import random
import time
import csv
import matplotlib.pyplot as plt

from closest import closest_pair
from closest import closest_pair_brute


# Generate random points
def generate_points_349(n_349):

    random.seed(349 + n_349)

    points_349 = []

    for i_349 in range(n_349):

        x_349 = random.randint(0, 100000)
        y_349 = random.randint(0, 100000)

        points_349.append((x_349, y_349))

    return points_349


# Measure the running time
def measure_time_349(function_349, points_349):

    start_349 = time.perf_counter()

    function_349(points_349)

    end_349 = time.perf_counter()

    return end_349 - start_349


# Main benchmark
def run_benchmark_349():

    sizes_349 = [
        1000, 2000, 4000, 8000,
        16000, 32000, 64000
    ]

    results_349 = []

    brute_stopped_349 = False

    print("\nCLOSEST PAIR BENCHMARK")
    print("-" * 65)

    print(
        f"{'Points':<12}"
        f"{'Brute Force':<22}"
        f"{'Divide and Conquer':<22}"
    )

    for n_349 in sizes_349:

        points_349 = generate_points_349(n_349)

        # Measure divide and conquer.
        divide_time_349 = measure_time_349(
            closest_pair, points_349
        )

        brute_time_349 = None

        # Measure brute force.
        if not brute_stopped_349:

            try:

                start_349 = time.perf_counter()

                closest_pair_brute(
                    points_349,
                    time_limit=60
                )

                brute_time_349 = (
                    time.perf_counter() - start_349
                )

            except TimeoutError:

                brute_stopped_349 = True

        results_349.append(
            (n_349, brute_time_349, divide_time_349)
        )

        # Display the results.
        if brute_time_349 is None:
            brute_display_349 = "Stopped (>60 sec)"
        else:
            brute_display_349 = f"{brute_time_349:.6f}"

        print(
            f"{n_349:<12}"
            f"{brute_display_349:<22}"
            f"{divide_time_349:.6f}"
        )

    # Save results to CSV.
    with open(
        "benchmark_results.csv",
        "w",
        newline=""
    ) as file_349:

        writer_349 = csv.writer(file_349)

        writer_349.writerow([
            "Number of Points",
            "Brute Force Time",
            "Divide and Conquer Time"
        ])

        writer_349.writerows(results_349)

    # Find the first tested crossover point.
    crossover_349 = None

    for row_349 in results_349:

        n_349 = row_349[0]
        brute_349 = row_349[1]
        divide_349 = row_349[2]

        if (
            brute_349 is not None
            and divide_349 < brute_349
        ):

            crossover_349 = n_349
            break

    print("\nCrossover Point:")

    if crossover_349 is not None:

        print(
            "Divide and conquer first became faster "
            f"at n = {crossover_349}"
        )

    else:

        print("No crossover found in the tested sizes.")

    # Prepare graph data.
    brute_sizes_349 = []
    brute_times_349 = []

    divide_sizes_349 = []
    divide_times_349 = []

    for row_349 in results_349:

        divide_sizes_349.append(row_349[0])
        divide_times_349.append(row_349[2])

        if row_349[1] is not None:

            brute_sizes_349.append(row_349[0])
            brute_times_349.append(row_349[1])

    # Draw the graph.
    plt.figure(figsize=(9, 6))

    plt.loglog(
        brute_sizes_349,
        brute_times_349,
        marker="o",
        label="Brute Force"
    )

    plt.loglog(
        divide_sizes_349,
        divide_times_349,
        marker="s",
        label="Divide and Conquer"
    )

    plt.xlabel("Number of Points")
    plt.ylabel("Running Time (seconds)")

    plt.title("Closest Pair Algorithm Comparison")

    plt.legend()
    plt.grid(True, which="both")

    plt.tight_layout()

    plt.savefig("closest_pair_graph.png", dpi=300)

    plt.show()

    print("\nFiles created:")
    print("benchmark_results.csv")
    print("closest_pair_graph.png")


if __name__ == "__main__":

    run_benchmark_349()
