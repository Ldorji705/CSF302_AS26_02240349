# Lab 4 - Part A: Modular Exponentiation (a^b mod m)
import time


# check inputs
def check_349(b_349, m_349):
    if m_349 < 1:
        raise ValueError("m must be at least 1")
    if b_349 < 0:
        raise ValueError("exponent must not be negative")


# naive: multiply a, b times
def pow_naive_349(a_349, b_349, m_349):
    check_349(b_349, m_349)
    a_349 = a_349 % m_349                    # negative base: reduce first
    result_349 = 1 % m_349               # b = 0 gives 1 mod m
    for _ in range(b_349):
        result_349 = (result_349 * a_349) % m_349
    return result_349


# binary (square-and-multiply)
def pow_binary_349(a_349, b_349, m_349):
    check_349(b_349, m_349)
    a_349 = a_349 % m_349
    result_349 = 1 % m_349
    while b_349 > 0:
        if b_349 % 2 == 1:           # odd exponent: multiply
            result_349 = (result_349 * a_349) % m_349
        a_349 = (a_349 * a_349) % m_349          # square the base
        b_349 = b_349 // 2               # halve the exponent
    return result_349


# binary with bitwise operations
def pow_bitwise_349(a_349, b_349, m_349):
    check_349(b_349, m_349)
    a_349 = a_349 % m_349
    result_349 = 1 % m_349
    while b_349 > 0:
        if b_349 & 1:                # same as b % 2 == 1
            result_349 = (result_349 * a_349) % m_349
        a_349 = (a_349 * a_349) % m_349
        b_349 >>= 1                  # same as b = b // 2
    return result_349


# compare outputs
print("Compare naive, binary, bitwise, built-in pow")
tests_349 = [(2, 10, 1000), (3, 200, 13), (7, 0, 5), (-5, 3, 7),
         (123456789, 1000, 1000000007), (5, 50, 1)]
for a_349, b_349, m_349 in tests_349:
    r1_349 = pow_naive_349(a_349, b_349, m_349)
    r2_349 = pow_binary_349(a_349, b_349, m_349)
    r3_349 = pow_bitwise_349(a_349, b_349, m_349)
    print(f"{a_349}^{b_349} mod {m_349} = {r1_349}, {r2_349}, {r3_349}  ->  same? {r1_349 == r2_349 == r3_349 == pow(a_349, b_349, m_349)}")

# validation
print("\nValidation")
print("2^0 mod 7 =", pow_bitwise_349(2, 0, 7))          # zero exponent
print("(-2)^3 mod 7 =", pow_bitwise_349(-2, 3, 7))      # negative base
for a_349, b_349, m_349 in [(2, -1, 7), (2, 3, 0)]:             # bad inputs
    try:
        pow_bitwise_349(a_349, b_349, m_349)
    except ValueError as error_349:
        print("error:", error_349)

# timing
print("\nTiming (a = 3, m = 1000000007)")
print("b          naive        binary")
b_349 = 10
while b_349 <= 1000000:
    start_349 = time.perf_counter()
    pow_naive_349(3, b_349, 1000000007)
    t1_349 = time.perf_counter() - start_349

    start_349 = time.perf_counter()
    pow_binary_349(3, b_349, 1000000007)
    t2_349 = time.perf_counter() - start_349

    print(f"{b_349:<10} {t1_349:<12.6f} {t2_349:.6f}")
    b_349 = b_349 * 10

print("\nNaive needs b steps. Binary needs about log2(b) steps.")