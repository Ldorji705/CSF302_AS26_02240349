import random

def generate_matrix(n_349):
    matrix_349 = []
    for i_349 in range(n_349):
        row_349 = []
        for j_349 in range(n_349):
            row_349.append(random.randint(1, 10))
        matrix_349.append(row_349)
    return matrix_349

def display_matrix(m_349):
    for row_349 in m_349:
        print(row_349)

def multiply_matrices(A_349, B_349, n_349):
    C_349 = []
    for i_349 in range(n_349):
        row_349 = []
        for j_349 in range(n_349):
            row_349.append(0)
        C_349.append(row_349)

    operations_349 = 0
    for i_349 in range(n_349):
        for j_349 in range(n_349):
            for k_349 in range(n_349):
                C_349[i_349][j_349] = C_349[i_349][j_349] + A_349[i_349][k_349] * B_349[k_349][j_349]
                operations_349 = operations_349 + 2
    return C_349, operations_349

# ---- Main program ----
n_349 = int(input("Enter matrix size (power of 2, e.g. 2, 4, 8): "))

A_349 = generate_matrix(n_349)
B_349 = generate_matrix(n_349)

print("Matrix A:")
display_matrix(A_349)

print("Matrix B:")
display_matrix(B_349)

C_349, operations_349 = multiply_matrices(A_349, B_349, n_349)

print("Result Matrix C = A x B:")
display_matrix(C_349)

print("Total operations:", operations_349)

