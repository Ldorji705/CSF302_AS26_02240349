# Lab 7 - Q2: Huffman Coding
import heapq


# count how often each character appears
def count_frequencies_349(text_349):
    freq_349 = {}
    for ch_349 in text_349:
        freq_349[ch_349] = freq_349.get(ch_349, 0) + 1
    return freq_349


# build the tree: always join the two smallest
# a node is either a character, or a pair (left, right)
def build_tree_349(freq_349):
    heap_349 = []
    tie_349 = 0                                    # tie-breaker for equal frequencies
    for ch_349 in freq_349:
        heap_349.append((freq_349[ch_349], tie_349, ch_349))
        tie_349 += 1
    heapq.heapify(heap_349)
    while len(heap_349) > 1:
        f1_349, _, left_349 = heapq.heappop(heap_349)
        f2_349, _, right_349 = heapq.heappop(heap_349)
        heapq.heappush(heap_349, (f1_349 + f2_349, tie_349, (left_349, right_349)))
        tie_349 += 1
    return heap_349[0][2]


# walk the tree: left = 0, right = 1
def make_codes_349(node_349, prefix_349, table_349):
    if isinstance(node_349, str):                  # leaf: a character
        table_349[node_349] = prefix_349 if prefix_349 != "" else "0"
    else:
        make_codes_349(node_349[0], prefix_349 + "0", table_349)
        make_codes_349(node_349[1], prefix_349 + "1", table_349)


def encode_349(text_349, table_349):
    return "".join(table_349[ch_349] for ch_349 in text_349)


# decode: read bits until they match a code
def decode_349(bits_349, table_349):
    reverse_349 = {}
    for ch_349 in table_349:
        reverse_349[table_349[ch_349]] = ch_349
    text_349 = ""
    current_349 = ""
    for bit_349 in bits_349:
        current_349 += bit_349
        if current_349 in reverse_349:
            text_349 += reverse_349[current_349]
            current_349 = ""
    return text_349


# three sample text files
files_349 = {
    "text1.txt": "huffman coding gives short codes to common letters and long codes "
                 "to rare letters so the whole file becomes smaller. " * 5,
    "text2.txt": "aaaaaaaaaaaaaaaaaaaabbbbbbbbbbccccdde " * 10,
    "text3.txt": "The quick brown fox jumps over the lazy dog. Pack my box with "
                 "five dozen liquor jugs! 0123456789 XYZ? " * 4,
}
for name_349 in files_349:
    open(name_349, "w").write(files_349[name_349])

print("File        chars   fixed bits   huffman bits   ratio   saved")
for name_349 in files_349:
    text_349 = open(name_349).read()
    freq_349 = count_frequencies_349(text_349)
    tree_349 = build_tree_349(freq_349)
    table_349 = {}
    make_codes_349(tree_349, "", table_349)
    bits_349 = encode_349(text_349, table_349)
    back_349 = decode_349(bits_349, table_349)
    assert back_349 == text_349                        # decoded text must match
    fixed_349 = 8 * len(text_349)
    ratio_349 = len(bits_349) / fixed_349
    print(f"{name_349:<10} {len(text_349):>6} {fixed_349:>12} {len(bits_349):>14} {ratio_349:>7.3f} {100 * (1 - ratio_349):>6.1f}%")
    if name_349 == "text1.txt":
        first_table_349 = table_349
        first_freq_349 = freq_349

print("\nCode table for text1.txt")
print("char  count  code")
for ch_349 in sorted(first_table_349, key=lambda c_349: len(first_table_349[c_349])):
    print(f"{repr(ch_349):<5} {first_freq_349[ch_349]:>5}  {first_table_349[ch_349]}")
print("\nDecoded text equals the original for all files.")
print("(Ratio does not count the space needed to store the code table.)")