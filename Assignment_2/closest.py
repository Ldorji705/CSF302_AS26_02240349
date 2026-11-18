
import math
import time


# Brute force algorithm
def closest_pair_brute(points, time_limit=None):

    n_349 = len(points)

    # Check that there are at least two points.
    if n_349 < 2:
        raise ValueError("At least two points are required.")

    # Start the timer.
    start_time_349 = time.perf_counter()

    smallest_distance_349 = float("inf")

    best_i_349 = -1
    best_j_349 = -1

    # Check every possible pair.
    for i_349 in range(n_349):

        # Check whether the time limit has been exceeded.
        if time_limit is not None:
            elapsed_time_349 = time.perf_counter() - start_time_349

            if elapsed_time_349 > time_limit:
                raise TimeoutError(
                    "Brute-force function exceeded the time limit."
                )

        for j_349 in range(i_349 + 1, n_349):

            # Get the coordinates.
            x1_349 = points[i_349][0]
            y1_349 = points[i_349][1]

            x2_349 = points[j_349][0]
            y2_349 = points[j_349][1]

            # Calculate the distance.
            dx_349 = x2_349 - x1_349
            dy_349 = y2_349 - y1_349

            distance_349 = math.sqrt(
                dx_349 ** 2 + dy_349 ** 2
            )

            # Store the smallest distance.
            candidate_349 = (
                distance_349,
                i_349,
                j_349
            )

            current_best_349 = (
                smallest_distance_349,
                best_i_349,
                best_j_349
            )

            if candidate_349 < current_best_349:

                smallest_distance_349 = distance_349
                best_i_349 = i_349
                best_j_349 = j_349

    return (
        smallest_distance_349,
        best_i_349,
        best_j_349
    )


# Divide and conquer helper function
def closest_recursive_349(x_sorted_349, y_sorted_349):

    n_349 = len(x_sorted_349)

    # Base case: if there are 3 or fewer points,
    # check them directly.
    if n_349 <= 3:

        best_349 = (float("inf"), -1, -1)

        for i_349 in range(n_349):

            for j_349 in range(i_349 + 1, n_349):

                point1_349 = x_sorted_349[i_349]
                point2_349 = x_sorted_349[j_349]

                dx_349 = point1_349[0] - point2_349[0]
                dy_349 = point1_349[1] - point2_349[1]

                distance_squared_349 = (
                    dx_349 ** 2 + dy_349 ** 2
                )

                index1_349 = min(
                    point1_349[2], point2_349[2]
                )

                index2_349 = max(
                    point1_349[2], point2_349[2]
                )

                candidate_349 = (
                    distance_squared_349,
                    index1_349,
                    index2_349
                )

                if candidate_349 < best_349:
                    best_349 = candidate_349

        return best_349

    # Divide the points into two halves.
    middle_349 = n_349 // 2

    left_x_349 = x_sorted_349[:middle_349]
    right_x_349 = x_sorted_349[middle_349:]

    # Find which points belong to the left half.
    left_indices_349 = set()

    for point_349 in left_x_349:
        left_indices_349.add(point_349[2])

    # Divide the y-sorted points into two groups.
    left_y_349 = []
    right_y_349 = []

    for point_349 in y_sorted_349:

        if point_349[2] in left_indices_349:
            left_y_349.append(point_349)
        else:
            right_y_349.append(point_349)

    # Solve the left and right halves.
    left_best_349 = closest_recursive_349(
        left_x_349, left_y_349
    )

    right_best_349 = closest_recursive_349(
        right_x_349, right_y_349
    )

    # Choose the smaller result.
    best_349 = min(left_best_349, right_best_349)

    # Find the dividing line.
    middle_x_349 = x_sorted_349[middle_349][0]

    smallest_distance_349 = math.sqrt(best_349[0])

    # Collect points close to the dividing line.
    strip_349 = []

    for point_349 in y_sorted_349:

        if abs(point_349[0] - middle_x_349) <= smallest_distance_349:
            strip_349.append(point_349)

    # Check nearby points in the strip.
    for i_349 in range(len(strip_349)):

        # Only check the next seven points.
        for j_349 in range(
            i_349 + 1,
            min(i_349 + 8, len(strip_349))
        ):

            # Stop if the y-distance is too large.
            dy_349 = strip_349[j_349][1] - strip_349[i_349][1]

            if dy_349 ** 2 > best_349[0]:
                break

            point1_349 = strip_349[i_349]
            point2_349 = strip_349[j_349]

            dx_349 = point1_349[0] - point2_349[0]
            dy_349 = point1_349[1] - point2_349[1]

            distance_squared_349 = (
                dx_349 ** 2 + dy_349 ** 2
            )

            index1_349 = min(
                point1_349[2], point2_349[2]
            )

            index2_349 = max(
                point1_349[2], point2_349[2]
            )

            candidate_349 = (
                distance_squared_349,
                index1_349,
                index2_349
            )

            if candidate_349 < best_349:
                best_349 = candidate_349

    return best_349


# Main divide and conquer function
def closest_pair(points):

    n_349 = len(points)

    if n_349 < 2:
        raise ValueError("At least two points are required.")

    # Add the original index to every point.
    indexed_points_349 = []

    for i_349 in range(n_349):

        x_349 = points[i_349][0]
        y_349 = points[i_349][1]

        indexed_points_349.append((x_349, y_349, i_349))

    # Sort points by x-coordinate.
    x_sorted_349 = sorted(
        indexed_points_349,
        key=lambda point_349: (
            point_349[0], point_349[1], point_349[2]
        )
    )

    # Sort points by y-coordinate.
    y_sorted_349 = sorted(
        indexed_points_349,
        key=lambda point_349: (
            point_349[1], point_349[0], point_349[2]
        )
    )

    # Find the closest pair recursively.
    result_349 = closest_recursive_349(
        x_sorted_349, y_sorted_349
    )

    # Return the actual distance and original indices.
    return (
        math.sqrt(result_349[0]),
        result_349[1],
        result_349[2]
    )


# Example to test both algorithms
if __name__ == "__main__":

    points_349 = [
        (2, 3),
        (12, 30),
        (40, 50),
        (5, 1),
        (12, 10),
        (3, 4)
    ]

    print("Camera Trap Points:")
    print(points_349)

    print("\nBrute Force Result:")
    print(closest_pair_brute(points_349))

    print("\nDivide and Conquer Result:")
    print(closest_pair(points_349))
