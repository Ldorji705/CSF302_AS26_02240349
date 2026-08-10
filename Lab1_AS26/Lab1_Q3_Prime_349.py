import time

# Naive Prime Checking
def naive_prime_349(number_349):
    if number_349 < 2:
        return False
    for i_349 in range(2, number_349):
        if number_349 % i_349 == 0:
            return False
    return True

# Optimized Prime Checking
def optimized_prime_349(number_349):
    if number_349 < 2:
        return False
    i_349 = 2
    while i_349 * i_349 <= number_349:
        if number_349 % i_349 == 0:
            return False
        i_349 += 1
    return True

# Sieve of Eratosthenes
def sieve_349(number_349):
    prime_349 = [True] * (number_349 + 1)
    prime_349[0] = False
    prime_349[1] = False
    i_349 = 2

    while i_349 * i_349 <= number_349:
        if prime_349[i_349]:
            for j_349 in range(i_349 * i_349,
                               number_349 + 1,
                               i_349):
                prime_349[j_349] = False
        i_349 += 1
    return prime_349

# Input sizes
sizes_349 = [10000, 50000, 100000, 500000, 1000000]

for size_349 in sizes_349:
    print("Input Size:", size_349)

    # Naive Method
    start_349 = time.perf_counter()
    for number_349 in range(2, size_349 + 1):
        naive_prime_349(number_349)
    end_349 = time.perf_counter()
    naive_time_349 = end_349 - start_349

    # Optimized Method
    start_349 = time.perf_counter()
    for number_349 in range(2, size_349 + 1):
        optimized_prime_349(number_349)
    end_349 = time.perf_counter()
    optimized_time_349 = end_349 - start_349

    # Sieve Method
    start_349 = time.perf_counter()
    sieve_349(size_349)
    end_349 = time.perf_counter()
    sieve_time_349 = end_349 - start_349

    print("Naive Method:", naive_time_349, "seconds")
    print("Optimized Method:", optimized_time_349, "seconds")
    print("Sieve Method:", sieve_time_349, "seconds")
    print("-------------------------")