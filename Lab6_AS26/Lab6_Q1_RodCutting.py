# Lab 6 - Q1: Rod Cutting
import time

price_349 = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
for i_349 in range(11, 26):              # extend table: 3 * length
    price_349.append(3 * i_349)

calls_349 = 0


# naive recursion
def cut_naive_349(n_349):
    global calls_349
    calls_349 += 1
    if n_349 == 0:
        return 0
    best_349 = 0
    for first_349 in range(1, n_349 + 1):
        money_349 = price_349[first_349] + cut_naive_349(n_349 - first_349)
        if money_349 > best_349:
            best_349 = money_349
    return best_349


# memoization
def cut_memo_349(n_349, memo_349):
    global calls_349
    calls_349 += 1
    if n_349 == 0:
        return 0
    if n_349 in memo_349:                    # reuse saved answer
        return memo_349[n_349]
    best_349 = 0
    for first_349 in range(1, n_349 + 1):
        money_349 = price_349[first_349] + cut_memo_349(n_349 - first_349, memo_349)
        if money_349 > best_349:
            best_349 = money_349
    memo_349[n_349] = best_349                   # save answer
    return best_349


# bottom-up table
def cut_bottom_up_349(n_349):
    best_349 = [0] * (n_349 + 1)
    first_349 = [0] * (n_349 + 1)            # first piece to cut
    steps_349 = 0
    for j_349 in range(1, n_349 + 1):
        for i_349 in range(1, j_349 + 1):
            steps_349 += 1
            money_349 = price_349[i_349] + best_349[j_349 - i_349]
            if money_349 > best_349[j_349]:
                best_349[j_349] = money_349
                first_349[j_349] = i_349
    return best_349, first_349, steps_349


# list the piece lengths
def get_pieces_349(first_349, n_349):
    pieces_349 = []
    while n_349 > 0:
        pieces_349.append(first_349[n_349])
        n_349 = n_349 - first_349[n_349]
    return pieces_349


# revenue and pieces for n = 1 to 10
best_349, first_349, steps_349 = cut_bottom_up_349(10)
print("n   revenue   pieces")
for n_349 in range(1, 11):
    print(n_349, "  ", best_349[n_349], "     ", get_pieces_349(first_349, n_349))

# compare the three versions
print()
print("n    naive calls   naive time   memo calls   memo time   table steps   table time")
for n_349 in [5, 10, 15, 20, 25]:        # n = 25 naive is slow
    calls_349 = 0
    start_349 = time.perf_counter()
    r1_349 = cut_naive_349(n_349)
    t1_349 = time.perf_counter() - start_349
    c1_349 = calls_349

    calls_349 = 0
    start_349 = time.perf_counter()
    r2_349 = cut_memo_349(n_349, {})
    t2_349 = time.perf_counter() - start_349
    c2_349 = calls_349

    start_349 = time.perf_counter()
    best_349, first_349, steps_349 = cut_bottom_up_349(n_349)
    t3_349 = time.perf_counter() - start_349

    assert r1_349 == r2_349 == best_349[n_349]       # all must agree
    print(n_349, "  ", c1_349, "  ", round(t1_349, 5), "  ", c2_349, "  ", round(t2_349, 6),
          "  ", steps_349, "  ", round(t3_349, 6))

print()
print("Naive makes 2^n calls because it solves the same rod lengths many times.")
print("Memo solves each length only once, so it needs about n*(n+1)/2 calls.")
print("Bottom-up does the same n*(n+1)/2 steps but with a loop, no recursion.")