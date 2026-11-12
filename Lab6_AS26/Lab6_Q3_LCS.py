# Lab 6 - Q3: Longest Common Subsequence
import random
import time


# fill table
def lcs_table_349(X_349, Y_349):
    table_349 = [[0] * (len(Y_349) + 1) for _ in range(len(X_349) + 1)]
    for i_349 in range(1, len(X_349) + 1):
        for j_349 in range(1, len(Y_349) + 1):
            if X_349[i_349 - 1] == Y_349[j_349 - 1]:                # match: use diagonal
                table_349[i_349][j_349] = table_349[i_349 - 1][j_349 - 1] + 1
            else:                                   # no match: take best
                table_349[i_349][j_349] = max(table_349[i_349 - 1][j_349], table_349[i_349][j_349 - 1])
    return table_349


def print_table_349(table_349, X_349, Y_349):
    print("     -  " + "  ".join(Y_349))
    for i_349 in range(len(X_349) + 1):
        letter_349 = "-" if i_349 == 0 else X_349[i_349 - 1]
        print(letter_349, " ", "  ".join(str(v_349) for v_349 in table_349[i_349]))


# walk back to get one LCS
def get_lcs_349(table_349, X_349, Y_349):
    i_349 = len(X_349)
    j_349 = len(Y_349)
    result_349 = ""
    while i_349 > 0 and j_349 > 0:
        if X_349[i_349 - 1] == Y_349[j_349 - 1]:
            result_349 = X_349[i_349 - 1] + result_349
            i_349 -= 1
            j_349 -= 1
        elif table_349[i_349 - 1][j_349] >= table_349[i_349][j_349 - 1]:
            i_349 -= 1
        else:
            j_349 -= 1
    return result_349


# length only, two rows
def lcs_length_two_rows_349(X_349, Y_349):
    previous_349 = [0] * (len(Y_349) + 1)
    for i_349 in range(1, len(X_349) + 1):
        current_349 = [0] * (len(Y_349) + 1)
        for j_349 in range(1, len(Y_349) + 1):
            if X_349[i_349 - 1] == Y_349[j_349 - 1]:
                current_349[j_349] = previous_349[j_349 - 1] + 1
            else:
                current_349[j_349] = max(previous_349[j_349], current_349[j_349 - 1])
        previous_349 = current_349
    return previous_349[len(Y_349)]


# are letters of small found in order inside big?
def is_subsequence_349(small_349, big_349):
    pos_349 = 0
    for letter_349 in big_349:
        if pos_349 < len(small_349) and letter_349 == small_349[pos_349]:
            pos_349 += 1
    return pos_349 == len(small_349)


# brute force: try all 2^n subsequences
def lcs_brute_force_349(X_349, Y_349):
    best_349 = 0
    for mask_349 in range(2 ** len(X_349)):
        sub_349 = ""
        for i_349 in range(len(X_349)):
            if (mask_349 >> i_349) & 1:                     # bit on = keep letter
                sub_349 += X_349[i_349]
        if len(sub_349) > best_349 and is_subsequence_349(sub_349, Y_349):
            best_349 = len(sub_349)
    return best_349


# diff: "  " same, "-" removed, "+" added
def diff_349(old_349, new_349):
    table_349 = lcs_table_349(old_349, new_349)
    i_349 = len(old_349)
    j_349 = len(new_349)
    result_349 = []
    while i_349 > 0 and j_349 > 0:
        if old_349[i_349 - 1] == new_349[j_349 - 1]:
            result_349.append("  " + old_349[i_349 - 1])
            i_349 -= 1
            j_349 -= 1
        elif table_349[i_349][j_349 - 1] >= table_349[i_349 - 1][j_349]:
            result_349.append("+ " + new_349[j_349 - 1])
            j_349 -= 1
        else:
            result_349.append("- " + old_349[i_349 - 1])
            i_349 -= 1
    while i_349 > 0:
        result_349.append("- " + old_349[i_349 - 1])
        i_349 -= 1
    while j_349 > 0:
        result_349.append("+ " + new_349[j_349 - 1])
        j_349 -= 1
    result_349.reverse()                                # built backwards
    return result_349


# run everything
X_349 = "ABCBDAB"
Y_349 = "BDCABA"
table_349 = lcs_table_349(X_349, Y_349)
print("Table for X =", X_349, " Y =", Y_349)
print_table_349(table_349, X_349, Y_349)
print("One LCS:", get_lcs_349(table_349, X_349, Y_349), " length:", table_349[len(X_349)][len(Y_349)])
print("Two-row version length:", lcs_length_two_rows_349(X_349, Y_349))

# DP vs brute force timing
print()
print("Length   DP time      brute force time   same answer?")
for n_349 in range(5, 19):
    a_349 = "".join(random.choice("ABCD") for _ in range(n_349))
    b_349 = "".join(random.choice("ABCD") for _ in range(n_349))

    start_349 = time.perf_counter()
    r1_349 = lcs_table_349(a_349, b_349)[n_349][n_349]
    t1_349 = time.perf_counter() - start_349

    start_349 = time.perf_counter()
    r2_349 = lcs_brute_force_349(a_349, b_349)
    t2_349 = time.perf_counter() - start_349

    print(n_349, "     ", round(t1_349, 6), "   ", round(t2_349, 6), "       ", r1_349 == r2_349)

# diff of two small files
print()
print("Diff of old.txt and new.txt:")
open("old.txt", "w").write("apple\nbanana\ncherry\ngrape\n")
open("new.txt", "w").write("apple\nblueberry\ncherry\ngrape\nmango\n")
old_lines_349 = open("old.txt").read().splitlines()
new_lines_349 = open("new.txt").read().splitlines()
for line_349 in diff_349(old_lines_349, new_lines_349):
    print(line_349)