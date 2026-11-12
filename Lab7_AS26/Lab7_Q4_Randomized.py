# Lab 7 - Q4: Randomized Algorithms
import random
import time


# randomized quickselect: k-th smallest (k starts at 1)
def quickselect_349(a_349, k_349):
    while True:
        pivot_349 = random.choice(a_349)               # random pivot
        lows_349 = [x_349 for x_349 in a_349 if x_349 < pivot_349]
        equal_count_349 = len([x_349 for x_349 in a_349 if x_349 == pivot_349])
        highs_349 = [x_349 for x_349 in a_349 if x_349 > pivot_349]
        if k_349 <= len(lows_349):                     # answer is in the low part
            a_349 = lows_349
        elif k_349 <= len(lows_349) + equal_count_349:     # answer is the pivot
            return pivot_349
        else:                                  # answer is in the high part
            k_349 = k_349 - len(lows_349) - equal_count_349
            a_349 = highs_349


# Miller-Rabin primality test
def miller_rabin_349(n_349, rounds_349):
    if n_349 < 4:
        return n_349 == 2 or n_349 == 3
    if n_349 % 2 == 0:
        return False
    d_349 = n_349 - 1                                  # write n-1 = d * 2^r
    r_349 = 0
    while d_349 % 2 == 0:
        d_349 = d_349 // 2
        r_349 += 1
    for _ in range(rounds_349):
        a_349 = random.randint(2, n_349 - 2)           # random witness
        x_349 = pow(a_349, d_349, n_349)
        if x_349 == 1 or x_349 == n_349 - 1:
            continue
        for _ in range(r_349 - 1):
            x_349 = x_349 * x_349 % n_349
            if x_349 == n_349 - 1:
                break
        else:
            return False                       # a proves n is composite
    return True                                # probably prime


# trial division up to sqrt(n)
def trial_division_349(n_349):
    if n_349 < 2:
        return False
    if n_349 % 2 == 0:
        return n_349 == 2
    i_349 = 3
    while i_349 * i_349 <= n_349:
        if n_349 % i_349 == 0:
            return False
        i_349 += 2
    return True


# ---------- 1. quickselect vs sorting ----------
print("Quickselect vs sorted()[k-1], k = n/2")
print("n          quickselect   sorting")
for n_349 in [10**4, 10**5, 10**6]:
    data_349 = [random.randint(0, 10**9) for _ in range(n_349)]
    k_349 = n_349 // 2
    start_349 = time.perf_counter()
    r1_349 = quickselect_349(data_349, k_349)
    t1_349 = time.perf_counter() - start_349
    start_349 = time.perf_counter()
    r2_349 = sorted(data_349)[k_349 - 1]
    t2_349 = time.perf_counter() - start_349
    assert r1_349 == r2_349
    print(f"{n_349:<10} {t1_349:<13.4f} {t2_349:.4f}")

# ---------- 2. Miller-Rabin vs trial division ----------
print("\n20 random 12-digit numbers")
print("number          trial division   Miller-Rabin   same?")
all_same_349 = True
for _ in range(20):
    n_349 = random.randint(10**11, 10**12 - 1)
    start_349 = time.perf_counter()
    a_349 = trial_division_349(n_349)
    t1_349 = time.perf_counter() - start_349
    start_349 = time.perf_counter()
    b_349 = miller_rabin_349(n_349, 20)
    t2_349 = time.perf_counter() - start_349
    if a_349 != b_349:
        all_same_349 = False
    print(f"{n_349:<15} {str(a_349):<6} {t1_349:.5f}s   {str(b_349):<6} {t2_349:.5f}s  {a_349 == b_349}")
print("Both agree on all 20?", all_same_349)

# ---------- 3. Carmichael number 561 with 1 round ----------
count_349 = 0
for _ in range(1000):
    if miller_rabin_349(561, 1):
        count_349 += 1
print("\n561 = 3 * 11 * 17 is NOT prime.")
print("Miller-Rabin (1 round) said 'prime'", count_349, "times out of 1000")