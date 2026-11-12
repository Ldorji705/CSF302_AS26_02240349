import time
import math
import random
import matplotlib.pyplot as plt

def is_prime_naive(n_349):
    steps_349 = 0
    if n_349 < 2:
        return False, steps_349
    for i_349 in range(2, n_349):
        steps_349 += 1
        if n_349 % i_349 == 0:
            return False, steps_349
    return True, steps_349

def is_prime_optimized(n_349):
    steps_349 = 0
    if n_349 < 2:
        return False, steps_349
    for i_349 in range(2, int(math.sqrt(n_349)) + 1):
        steps_349 += 1
        if n_349 % i_349 == 0:
            return False, steps_349
    return True, steps_349

def sieve_of_eratosthenes(limit_349):
    is_p_349 = [True] * (limit_349 + 1)
    is_p_349[0] = is_p_349[1] = False
    for i_349 in range(2, int(math.sqrt(limit_349)) + 1):
        if is_p_349[i_349]:
            for j_349 in range(i_349 * i_349, limit_349 + 1, i_349):
                is_p_349[j_349] = False
    return [i_349 for i_349, val_349 in enumerate(is_p_349) if val_349]

def main():
    numbers_349 = []
    print("Enter 10 numbers to test for primality:")
    for i_349 in range(10):
        n_349 = int(input(f"Number {i_349+1}: "))
        numbers_349.append(n_349)

    print(f"\n{'Number':<10}{'Naive?':<10}{'Naive Steps':<14}{'Opt?':<8}{'Opt Steps':<10}")
    naive_steps_list_349, opt_steps_list_349 = [], []

    for n_349 in numbers_349:
        naive_result_349, naive_steps_349 = is_prime_naive(n_349)
        opt_result_349, opt_steps_349 = is_prime_optimized(n_349)
        naive_steps_list_349.append(naive_steps_349)
        opt_steps_list_349.append(opt_steps_349)
        print(f"{n_349:<10}{str(naive_result_349):<10}{naive_steps_349:<14}{str(opt_result_349):<8}{opt_steps_349:<10}")

    limit_349 = max(numbers_349)
    print(f"\nPrimes up to {limit_349} (Sieve): {sieve_of_eratosthenes(limit_349)}")

    plt.plot(numbers_349, naive_steps_list_349, marker='o', label='Naive O(n)')
    plt.plot(numbers_349, opt_steps_list_349, marker='s', label='Optimized O(√n)')
    plt.xlabel("Number (n)")
    plt.ylabel("Step Count")
    plt.title("Naive vs Optimized Primality Test")
    plt.legend()
    plt.grid(True)
    plt.savefig("prime_comparison.png")
    plt.show()

if __name__ == "__main__":
    main()