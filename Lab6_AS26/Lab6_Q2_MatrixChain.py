# Lab 6 - Q2: Matrix Chain Multiplication
import random


# bottom-up DP
def matrix_chain_349(dims_349):
    n_349 = len(dims_349) - 1
    cost_349 = [[0] * (n_349 + 1) for _ in range(n_349 + 1)]    # minimum cost
    split_349 = [[0] * (n_349 + 1) for _ in range(n_349 + 1)]   # best split point

    for length_349 in range(2, n_349 + 1):
        for i_349 in range(1, n_349 - length_349 + 2):
            j_349 = i_349 + length_349 - 1
            cost_349[i_349][j_349] = float("inf")
            for k_349 in range(i_349, j_349):                   # try each split
                c_349 = cost_349[i_349][k_349] + cost_349[k_349 + 1][j_349] + dims_349[i_349 - 1] * dims_349[k_349] * dims_349[j_349]
                if c_349 < cost_349[i_349][j_349]:
                    cost_349[i_349][j_349] = c_349
                    split_349[i_349][j_349] = k_349
    return cost_349, split_349


# build bracket string
def brackets_349(split_349, i_349, j_349):
    if i_349 == j_349:
        return "A" + str(i_349)
    k_349 = split_349[i_349][j_349]
    return "(" + brackets_349(split_349, i_349, k_349) + brackets_349(split_349, k_349 + 1, j_349) + ")"


# brute force
def brute_force_349(dims_349, i_349, j_349):
    if i_349 == j_349:
        return 0
    best_349 = float("inf")
    for k_349 in range(i_349, j_349):
        c_349 = (brute_force_349(dims_349, i_349, k_349) + brute_force_349(dims_349, k_349 + 1, j_349)
             + dims_349[i_349 - 1] * dims_349[k_349] * dims_349[j_349])
        if c_349 < best_349:
            best_349 = c_349
    return best_349


# cost of ((A1 A2) A3) A4 ...
def left_to_right_349(dims_349):
    total_349 = 0
    for k_349 in range(1, len(dims_349) - 1):
        total_349 += dims_349[0] * dims_349[k_349] * dims_349[k_349 + 1]
    return total_349


# tests: two given + 5 random chains
tests_349 = [[30, 35, 15, 5, 10, 20, 25],          # expected 15125
         [5, 4, 6, 2, 7]]
for _ in range(5):
    how_many_349 = random.randint(3, 8)
    tests_349.append([random.randint(5, 50) for _ in range(how_many_349 + 1)])

for dims_349 in tests_349:
    n_349 = len(dims_349) - 1
    cost_349, split_349 = matrix_chain_349(dims_349)
    brute_349 = brute_force_349(dims_349, 1, n_349)
    print("dims:", dims_349)
    print("  DP minimum cost   :", cost_349[1][n_349])
    print("  brute force cost  :", brute_349, "-> same?", cost_349[1][n_349] == brute_349)
    print("  best brackets     :", brackets_349(split_349, 1, n_349))
    print("  left-to-right cost:", left_to_right_349(dims_349))
    print()