# Lab 5 - Q2: Counting Sort and Radix Sort
import random
import time
import matplotlib
matplotlib.use("Agg")                    # save plot to file
import matplotlib.pyplot as plt


# stable counting sort by a key (key value is 0..k)
def counting_sort_by_349(items_349, k_349, key_349):
    count_349 = [0] * (k_349 + 1)
    for x_349 in items_349:                      # count each key
        count_349[key_349(x_349)] += 1
    for v_349 in range(1, k_349 + 1):            # prefix sums
        count_349[v_349] += count_349[v_349 - 1]
    out_349 = [None] * len(items_349)
    for x_349 in reversed(items_349):            # backwards = stable
        count_349[key_349(x_349)] -= 1
        out_349[count_349[key_349(x_349)]] = x_349
    return out_349


def counting_sort_349(a_349, k_349):
    return counting_sort_by_349(a_349, k_349, lambda x_349: x_349)


# LSD radix sort: sort digit by digit, last digit first
def radix_sort_349(a_349, base_349):
    biggest_349 = max(a_349)
    exp_349 = 1                              # current digit position
    while biggest_349 // exp_349 > 0:
        a_349 = counting_sort_by_349(a_349, base_349 - 1, lambda x_349: (x_349 // exp_349) % base_349)
        exp_349 *= base_349
    return a_349


# merge sort (use your Lab 1 version if you have it)
def merge_sort_349(a_349):
    if len(a_349) <= 1:
        return a_349
    mid_349 = len(a_349) // 2
    left_349 = merge_sort_349(a_349[:mid_349])
    right_349 = merge_sort_349(a_349[mid_349:])
    out_349 = []
    i_349 = 0
    j_349 = 0
    while i_349 < len(left_349) and j_349 < len(right_349):
        if left_349[i_349] <= right_349[j_349]:
            out_349.append(left_349[i_349])
            i_349 += 1
        else:
            out_349.append(right_349[j_349])
            j_349 += 1
    return out_349 + left_349[i_349:] + right_349[j_349:]


def timed_349(func_349, *args_349):
    start_349 = time.perf_counter()
    result_349 = func_349(*args_349)
    return result_349, time.perf_counter() - start_349


# n fixed, vary k (counting sort vs merge sort)
n_349 = 100000
ks_349 = [10, 1000, 100000, 10000000]
count_times_349 = []
merge_times_k_349 = []
print("n = 100000, vary k")
print("k            counting   merge")
for k_349 in ks_349:
    data_349 = [random.randint(0, k_349) for _ in range(n_349)]
    r1_349, t1_349 = timed_349(counting_sort_349, data_349, k_349)
    r2_349, t2_349 = timed_349(merge_sort_349, data_349)
    assert r1_349 == r2_349 == sorted(data_349)
    count_times_349.append(t1_349)
    merge_times_k_349.append(t2_349)
    print(f"{k_349:<12} {t1_349:<10.4f} {t2_349:.4f}")

# k fixed, vary n (radix sort vs merge sort)
ns_349 = [10000, 50000, 100000, 500000, 1000000]
radix10_times_349 = []
radix256_times_349 = []
merge_times_n_349 = []
print("\nk = 10^9, vary n")
print("n          radix-10   radix-256  merge")
for n_349 in ns_349:
    data_349 = [random.randint(0, 10**9) for _ in range(n_349)]
    r1_349, t1_349 = timed_349(radix_sort_349, data_349, 10)
    r2_349, t2_349 = timed_349(radix_sort_349, data_349, 256)
    r3_349, t3_349 = timed_349(merge_sort_349, data_349)
    assert r1_349 == r2_349 == r3_349 == sorted(data_349)
    radix10_times_349.append(t1_349)
    radix256_times_349.append(t2_349)
    merge_times_n_349.append(t3_349)
    print(f"{n_349:<10} {t1_349:<10.3f} {t2_349:<10.3f} {t3_349:.3f}")

# plots
plt.figure(figsize=(11, 4))
plt.subplot(1, 2, 1)
plt.plot(ks_349, count_times_349, "o-", label="counting sort")
plt.plot(ks_349, merge_times_k_349, "s-", label="merge sort")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("k")
plt.ylabel("seconds")
plt.title("n = 100000, k grows")
plt.legend()
plt.subplot(1, 2, 2)
plt.plot(ns_349, radix10_times_349, "o-", label="radix base 10")
plt.plot(ns_349, radix256_times_349, "^-", label="radix base 256")
plt.plot(ns_349, merge_times_n_349, "s-", label="merge sort")
plt.xscale("log")
plt.yscale("log")
plt.xlabel("n")
plt.ylabel("seconds")
plt.title("k = 10^9, n grows")
plt.legend()
plt.tight_layout()
plt.savefig("q2_plots.png")
print("\nPlot saved to q2_plots.png")

# stability: equal keys must keep original order
keys_349 = [random.randint(0, 4) for _ in range(12)]
pairs_349 = [(keys_349[i_349], i_349) for i_349 in range(12)]          # (key, original index)
result_349 = counting_sort_by_349(pairs_349, 4, lambda p_349: p_349[0])
print("\ninput :", pairs_349)
print("output:", result_349)
stable_349 = True
for i_349 in range(len(result_349) - 1):
    if result_349[i_349][0] == result_349[i_349 + 1][0] and result_349[i_349][1] > result_349[i_349 + 1][1]:
        stable_349 = False
print("Stable?", stable_349)

print("""
When linear sorts win: small k (counting) or few digits (radix, base 256).
When they lose: k much bigger than n (counting), or many digit passes
(radix base 10). Merge sort works on anything comparable.""")