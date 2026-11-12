# Lab 7 - Q1: Activity Selection and Knapsack
import random


# greedy activity selection: sort by a rule, pick if it fits
def select_349(activities_349, rule_349):
    if rule_349 == "finish":                       # earliest finish time
        order_349 = sorted(activities_349, key=lambda a_349: a_349[1])
    elif rule_349 == "start":                      # earliest start time
        order_349 = sorted(activities_349, key=lambda a_349: a_349[0])
    else:                                      # shortest duration
        order_349 = sorted(activities_349, key=lambda a_349: a_349[1] - a_349[0])
    chosen_349 = []
    last_finish_349 = float("-inf")
    for start_349, finish_349 in order_349:
        if start_349 >= last_finish_349:               # no overlap
            chosen_349.append((start_349, finish_349))
            last_finish_349 = finish_349
    return chosen_349


# fractional knapsack: best value/weight first, may cut an item
def fractional_knapsack_349(items_349, capacity_349):
    order_349 = sorted(items_349, key=lambda it_349: it_349[0] / it_349[1], reverse=True)
    total_349 = 0
    left_349 = capacity_349
    for value_349, weight_349 in order_349:
        take_349 = min(weight_349, left_349)               # take all or a fraction
        total_349 += value_349 * take_349 / weight_349
        left_349 -= take_349
    return total_349


# same greedy rule for 0/1 knapsack: whole items only
def greedy_01_349(items_349, capacity_349):
    order_349 = sorted(items_349, key=lambda it_349: it_349[0] / it_349[1], reverse=True)
    total_349 = 0
    left_349 = capacity_349
    for value_349, weight_349 in order_349:
        if weight_349 <= left_349:
            total_349 += value_349
            left_349 -= weight_349
    return total_349


# 0/1 knapsack by DP (optimal)
def dp_01_349(items_349, capacity_349):
    best_349 = [0] * (capacity_349 + 1)
    for value_349, weight_349 in items_349:
        for w_349 in range(capacity_349, weight_349 - 1, -1):
            best_349[w_349] = max(best_349[w_349], best_349[w_349 - weight_349] + value_349)
    return best_349[capacity_349]


# ---------- activity selection ----------
print("Enter activities as start,finish pairs, e.g.  1,4 3,5 0,6 5,7")
text_349 = input("(press Enter for a sample): ").strip()
if text_349 == "":
    activities_349 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9),
                  (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
else:
    activities_349 = [tuple(int(x_349) for x_349 in pair_349.split(",")) for pair_349 in text_349.split()]
print("Activities:", activities_349)
print("Selected (earliest finish):", select_349(activities_349, "finish"))

# random testing: find inputs where another rule is worse
print()
for rule_349 in ["start", "shortest"]:
    while True:
        acts_349 = []
        for _ in range(6):
            s_349 = random.randint(0, 10)
            acts_349.append((s_349, s_349 + random.randint(1, 8)))
        if len(select_349(acts_349, rule_349)) < len(select_349(acts_349, "finish")):
            break
    print("Rule:", rule_349)
    print("  input           :", acts_349)
    print("  this rule gives :", len(select_349(acts_349, rule_349)), select_349(acts_349, rule_349))
    print("  earliest finish :", len(select_349(acts_349, "finish")), select_349(acts_349, "finish"))

# ---------- knapsack ----------
print("\nFractional knapsack, items (value, weight), capacity 50:")
items_349 = [(60, 10), (100, 20), (120, 30)]
print("  best value =", fractional_knapsack_349(items_349, 50))

print("\nGreedy vs DP on random 0/1 knapsack inputs")
worst_349 = 1.0
worst_case_349 = None
for _ in range(5000):
    n_349 = random.randint(2, 8)
    items_349 = [(random.randint(1, 30), random.randint(1, 20)) for _ in range(n_349)]
    capacity_349 = random.randint(5, 40)
    g_349 = greedy_01_349(items_349, capacity_349)
    best_349 = dp_01_349(items_349, capacity_349)
    if best_349 > 0 and g_349 / best_349 < worst_349:
        worst_349 = g_349 / best_349
        worst_case_349 = (items_349, capacity_349, g_349, best_349)
print("  worst ratio found (greedy / optimal) =", round(worst_349, 3))
print("  items, capacity, greedy, optimal    =", worst_case_349)
print("  bad case by hand: items [(2,1),(10,10)], capacity 10 ->",
      "greedy", greedy_01_349([(2, 1), (10, 10)], 10), ", optimal", dp_01_349([(2, 1), (10, 10)], 10))