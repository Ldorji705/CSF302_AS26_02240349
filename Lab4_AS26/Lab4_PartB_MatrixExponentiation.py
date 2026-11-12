# Lab 4 - Part B: Matrix Modular Exponentiation (A^n mod m)
import time


# multiply two square matrices, each entry mod m
def mat_mult_349(A_349, B_349, m_349):
    size_349 = len(A_349)
    C_349 = [[0] * size_349 for _ in range(size_349)]
    for i_349 in range(size_349):
        for j_349 in range(size_349):
            total_349 = 0
            for k_349 in range(size_349):
                total_349 += A_349[i_349][k_349] * B_349[k_349][j_349]     # row i x column j
            C_349[i_349][j_349] = total_349 % m_349
    return C_349


# identity matrix (1 on diagonal)
def identity_349(size_349, m_349):
    I_349 = [[0] * size_349 for _ in range(size_349)]
    for i_349 in range(size_349):
        I_349[i_349][i_349] = 1 % m_349
    return I_349


# naive: multiply A, n times
def mat_pow_naive_349(A_349, n_349, m_349):
    result_349 = identity_349(len(A_349), m_349)
    for _ in range(n_349):
        result_349 = mat_mult_349(result_349, A_349, m_349)
    return result_349


# binary: repeated squaring
def mat_pow_binary_349(A_349, n_349, m_349):
    result_349 = identity_349(len(A_349), m_349)
    base_349 = [[x_349 % m_349 for x_349 in row_349] for row_349 in A_349]
    while n_349 > 0:
        if n_349 & 1:                              # odd: multiply
            result_349 = mat_mult_349(result_349, base_349, m_349)
        base_349 = mat_mult_349(base_349, base_349, m_349)         # square
        n_349 >>= 1                                # halve
    return result_349


# Fibonacci: [[1,1],[1,0]]^n has F(n) in the top-right corner
def fib_349(n_349, m_349):
    return mat_pow_binary_349([[1, 1], [1, 0]], n_349, m_349)[0][1]


# walks of exactly k edges from u to v = (A^k)[u][v]
def count_walks_349(adj_349, u_349, v_349, k_349, m_349):
    return mat_pow_binary_349(adj_349, k_349, m_349)[u_349][v_349]


# compare naive and binary
print("Compare naive and binary")
tests_349 = [([[1, 1], [1, 0]], 10, 1000),
         ([[2, 3], [1, 4]], 15, 97),
         ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 8, 1000)]
for A_349, n_349, m_349 in tests_349:
    print("A =", A_349, " n =", n_349, " m =", m_349,
          " same?", mat_pow_naive_349(A_349, n_349, m_349) == mat_pow_binary_349(A_349, n_349, m_349))

# Fibonacci
print("\nFirst 15 Fibonacci numbers:", [fib_349(i_349, 1000000007) for i_349 in range(15)])
print("F(10^18) mod (10^9 + 7) =", fib_349(10**18, 10**9 + 7))

# walks in a directed graph
print("\nWalks from vertex 0 to vertex 3")
# edges: 0->1, 0->2, 1->2, 2->0, 2->3, 3->1
adj_349 = [[0, 1, 1, 0],
       [0, 0, 1, 0],
       [1, 0, 0, 1],
       [0, 1, 0, 0]]
for k_349 in [1, 2, 3, 10]:
    print("exactly", k_349, "edges:", count_walks_349(adj_349, 0, 3, k_349, 10**9 + 7))

# benchmark
print("\nBenchmark (seconds), m = 1000000007")
print("d    n       naive       binary")
m_349 = 10**9 + 7
for d_349 in [2, 4, 8, 16, 32]:
    A_349 = [[i_349 + j_349 + 1 for j_349 in range(d_349)] for i_349 in range(d_349)]
    for e_349 in [4, 8, 12]:                       # n = 2^4, 2^8, 2^12
        n_349 = 2 ** e_349
        start_349 = time.perf_counter()
        mat_pow_binary_349(A_349, n_349, m_349)
        t2_349 = time.perf_counter() - start_349
        if d_349 ** 3 * n_349 <= 20000000:             # skip very slow naive runs
            start_349 = time.perf_counter()
            mat_pow_naive_349(A_349, n_349, m_349)
            t1_349 = f"{time.perf_counter() - start_349:.5f}"
        else:
            t1_349 = "skipped"
        print(f"{d_349:<4} {n_349:<7} {t1_349:<11} {t2_349:.5f}")