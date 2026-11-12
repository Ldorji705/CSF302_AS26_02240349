# Lab 7 - Q3: Shortest Paths and Minimum Spanning Trees
import heapq
import random
import time

# sample weighted directed graph file: first line "V E", then "u v weight"
open("graph.txt", "w").write(
    "5 9\n0 1 10\n0 2 3\n1 2 1\n1 3 2\n2 1 4\n2 3 8\n2 4 2\n3 4 7\n4 3 9\n")


# read graph from file: adj[u] = list of (v, weight)
def read_graph_349(path_349):
    lines_349 = open(path_349).read().splitlines()
    v_count_349, e_count_349 = [int(x_349) for x_349 in lines_349[0].split()]
    adj_349 = [[] for _ in range(v_count_349)]
    for line_349 in lines_349[1:1 + e_count_349]:
        u_349, v_349, w_349 = [int(x_349) for x_349 in line_349.split()]
        adj_349[u_349].append((v_349, w_349))
    return v_count_349, adj_349


# Dijkstra with a binary heap
def dijkstra_349(v_count_349, adj_349, source_349):
    dist_349 = [float("inf")] * v_count_349
    parent_349 = [-1] * v_count_349
    done_349 = [False] * v_count_349                   # finished vertices
    dist_349[source_349] = 0
    heap_349 = [(0, source_349)]
    while heap_349:
        d_349, u_349 = heapq.heappop(heap_349)
        if done_349[u_349]:
            continue
        done_349[u_349] = True                         # distance is now final
        for v_349, w_349 in adj_349[u_349]:
            if not done_349[v_349] and d_349 + w_349 < dist_349[v_349]:
                dist_349[v_349] = d_349 + w_349
                parent_349[v_349] = u_349
                heapq.heappush(heap_349, (dist_349[v_349], v_349))
    return dist_349, parent_349


def get_path_349(parent_349, v_349):
    path_349 = []
    while v_349 != -1:
        path_349.append(v_349)
        v_349 = parent_349[v_349]
    path_349.reverse()
    return path_349


# Kruskal: sort edges, add if no cycle (union-find)
def find_349(group_349, x_349):
    while group_349[x_349] != x_349:
        group_349[x_349] = group_349[group_349[x_349]]             # shorten the path
        x_349 = group_349[x_349]
    return x_349


def kruskal_349(v_count_349, edges_349):
    group_349 = list(range(v_count_349))
    total_349 = 0
    for u_349, v_349, w_349 in sorted(edges_349, key=lambda e_349: e_349[2]):
        a_349 = find_349(group_349, u_349)
        b_349 = find_349(group_349, v_349)
        if a_349 != b_349:                             # different trees: join
            group_349[a_349] = b_349
            total_349 += w_349
    return total_349


# Prim: grow one tree using a heap
def prim_349(v_count_349, adj_349):
    seen_349 = [False] * v_count_349
    heap_349 = [(0, 0)]
    total_349 = 0
    while heap_349:
        w_349, u_349 = heapq.heappop(heap_349)
        if seen_349[u_349]:
            continue
        seen_349[u_349] = True
        total_349 += w_349
        for v_349, wt_349 in adj_349[u_349]:
            if not seen_349[v_349]:
                heapq.heappush(heap_349, (wt_349, v_349))
    return total_349


# random connected undirected graph with v_count vertices, e_count edges
def random_graph_349(v_count_349, e_count_349):
    used_349 = set()
    edges_349 = []
    for v_349 in range(1, v_count_349):                # random tree = connected
        u_349 = random.randint(0, v_349 - 1)
        used_349.add((u_349, v_349))
        edges_349.append((u_349, v_349, random.randint(1, 100)))
    while len(edges_349) < e_count_349:
        u_349 = random.randint(0, v_count_349 - 1)
        v_349 = random.randint(0, v_count_349 - 1)
        if u_349 != v_349 and (min(u_349, v_349), max(u_349, v_349)) not in used_349:
            used_349.add((min(u_349, v_349), max(u_349, v_349)))
            edges_349.append((u_349, v_349, random.randint(1, 100)))
    return edges_349


def make_adj_349(v_count_349, edges_349):
    adj_349 = [[] for _ in range(v_count_349)]
    for u_349, v_349, w_349 in edges_349:
        adj_349[u_349].append((v_349, w_349))
        adj_349[v_349].append((u_349, w_349))
    return adj_349


# Bellman-Ford (handles negative edges), used to show the right answer
def bellman_ford_349(v_count_349, edge_list_349, source_349):
    dist_349 = [float("inf")] * v_count_349
    dist_349[source_349] = 0
    for _ in range(v_count_349 - 1):
        for u_349, v_349, w_349 in edge_list_349:
            if dist_349[u_349] + w_349 < dist_349[v_349]:
                dist_349[v_349] = dist_349[u_349] + w_349
    return dist_349


# ---------- 1. Dijkstra from a file ----------
v_count_349, adj_349 = read_graph_349("graph.txt")
dist_349, parent_349 = dijkstra_349(v_count_349, adj_349, 0)
print("Dijkstra from vertex 0")
for v_349 in range(v_count_349):
    print(f"  to {v_349}: distance {dist_349[v_349]}, path {get_path_349(parent_349, v_349)}")

# ---------- 3. both MST algorithms agree ----------
same_349 = True
for _ in range(200):
    n_349 = random.randint(5, 30)
    e_349 = random.randint(n_349 - 1, n_349 * (n_349 - 1) // 2)
    edges_349 = random_graph_349(n_349, e_349)
    if kruskal_349(n_349, edges_349) != prim_349(n_349, make_adj_349(n_349, edges_349)):
        same_349 = False
print("\nKruskal and Prim give the same weight on 200 random graphs?", same_349)

# ---------- 4. timing, V = 1000 ----------
print("\nTiming for V = 1000 (seconds)")
print("graph    edges     Kruskal   Prim")
n_349 = 1000
for name_349, e_349 in [("sparse", 3 * n_349), ("dense", n_349 * n_349 // 4)]:
    edges_349 = random_graph_349(n_349, e_349)
    adj_349 = make_adj_349(n_349, edges_349)
    start_349 = time.perf_counter()
    w1_349 = kruskal_349(n_349, edges_349)
    t1_349 = time.perf_counter() - start_349
    start_349 = time.perf_counter()
    w2_349 = prim_349(n_349, adj_349)
    t2_349 = time.perf_counter() - start_349
    assert w1_349 == w2_349
    print(f"{name_349:<8} {e_349:<9} {t1_349:<9.4f} {t2_349:.4f}")

# ---------- 5. negative edge breaks Dijkstra ----------
print("\nNegative edge example: 0->1 (4), 0->2 (5), 2->1 (-3)")
neg_edges_349 = [(0, 1, 4), (0, 2, 5), (2, 1, -3)]
neg_adj_349 = [[(1, 4), (2, 5)], [], [(1, -3)]]
d_dijkstra_349, _ = dijkstra_349(3, neg_adj_349, 0)
d_correct_349 = bellman_ford_349(3, neg_edges_349, 0)
print("  Dijkstra distances   :", d_dijkstra_349)
print("  Correct distances    :", d_correct_349)
print("  Vertex 1 is wrong: Dijkstra locks it at 4 before it sees 0->2->1 = 2.")