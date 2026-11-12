# Lab 6 - Q4: Optimal Binary Search Tree

p_349 = [0, 0.15, 0.10, 0.05, 0.10, 0.20]       # key probabilities (p[0] unused)
q_349 = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]    # dummy key probabilities
n_349 = 5

cost_349 = [[0.0] * (n_349 + 1) for _ in range(n_349 + 2)]     # expected cost
weight_349 = [[0.0] * (n_349 + 1) for _ in range(n_349 + 2)]   # total probability
root_349 = [[0] * (n_349 + 1) for _ in range(n_349 + 2)]       # best root

# empty trees (dummy key only)
for i_349 in range(1, n_349 + 2):
    cost_349[i_349][i_349 - 1] = q_349[i_349 - 1]
    weight_349[i_349][i_349 - 1] = q_349[i_349 - 1]

# build trees of 1 key, 2 keys, ... n keys
for length_349 in range(1, n_349 + 1):
    for i_349 in range(1, n_349 - length_349 + 2):
        j_349 = i_349 + length_349 - 1
        weight_349[i_349][j_349] = weight_349[i_349][j_349 - 1] + p_349[j_349] + q_349[j_349]
        cost_349[i_349][j_349] = float("inf")
        for r_349 in range(i_349, j_349 + 1):            # try each root
            total_349 = cost_349[i_349][r_349 - 1] + cost_349[r_349 + 1][j_349] + weight_349[i_349][j_349]
            if total_349 < cost_349[i_349][j_349]:
                cost_349[i_349][j_349] = total_349
                root_349[i_349][j_349] = r_349

print("Expected search cost:", round(cost_349[1][n_349], 2))   # 2.75


# print tree, indent = depth
def print_tree_349(i_349, j_349, indent_349, label_349):
    if j_349 < i_349:                                # dummy key
        print(indent_349 + label_349 + ": d" + str(j_349))
        return
    r_349 = root_349[i_349][j_349]
    print(indent_349 + label_349 + ": k" + str(r_349))
    print_tree_349(i_349, r_349 - 1, indent_349 + "    ", "left")
    print_tree_349(r_349 + 1, j_349, indent_349 + "    ", "right")


print_tree_349(1, n_349, "", "root")