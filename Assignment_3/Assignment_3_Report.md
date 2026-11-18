# CSF302 – Assignment 3
## Improving Quicksort

**Name:** Lhundup Dorji  
**Student ID:** 02240349  
**Module:** CSF302  
**Assignment:** Assignment 3 – Improving Quicksort

### AI Assistance Acknowledgement

I used ChatGPT for guidance in understanding the assignment, implementing and testing the sorting algorithms, troubleshooting Python setup, and interpreting the benchmark results. I ran the programs and used the results from my own execution.

---

## 1. Introduction

The purpose of this assignment is to understand how Quicksort works and how its performance can be improved. In this assignment, I implemented two versions of Quicksort: Basic Quicksort and Improved Quicksort.

The basic version uses the last element as the pivot and applies the Lomuto partition method. The improved version uses a random pivot, insertion sort for smaller partitions, and a loop to process the larger partition.

I also tested both algorithms using different types of input and compared their performance with Python's built-in `sorted()` function.

## 2. Implementation

### 2.1 Basic Quicksort

Basic Quicksort uses the last element of the list as the pivot. The Lomuto partition method places the pivot in its correct position and separates the smaller and larger elements.

After partitioning, the algorithm recursively sorts the left and right partitions.

This implementation works correctly for normal inputs. However, it can become inefficient when the input is already sorted or contains many repeated values because the partitions may become unbalanced.

### 2.2 Improved Quicksort

The improved version includes three main changes:

- **Random pivot:** A random element is selected as the pivot to reduce the chance of repeatedly getting unbalanced partitions.
- **Insertion sort:** Insertion sort is used when a partition becomes small, instead of continuing to perform Quicksort partitioning.
- **Smaller-side recursion:** The algorithm recursively processes the smaller partition and uses a loop for the larger partition. This helps reduce recursion depth.

These improvements make the algorithm more reliable for different types of input.

## 3. Testing Results

I tested both algorithms using seven test cases:

1. Empty list.
2. List containing one element.
3. List containing only equal values.
4. Already sorted list.
5. Reverse sorted list.
6. List containing negative numbers.
7. 500 randomly generated lists.

Both algorithms passed all seven test methods. The results were also checked against Python's `sorted()` function to confirm that the output was correct.

## 4. Performance Analysis

I measured the execution time of both algorithms using random lists, already sorted lists, and lists containing many duplicate values. The list sizes ranged from 1,000 to 64,000 elements.

### 4.1 Benchmark Results

| Input type | List size | Basic Quicksort | Improved Quicksort |
|---|---:|---:|---:|
| Random | 1,000 | 0.000887 s | 0.001136 s |
| Random | 2,000 | 0.002073 s | 0.002600 s |
| Random | 4,000 | 0.004634 s | 0.005985 s |
| Random | 8,000 | 0.009763 s | 0.013234 s |
| Random | 16,000 | 0.021429 s | 0.029671 s |
| Random | 32,000 | 0.044178 s | 0.063837 s |
| Random | 64,000 | 0.093940 s | 0.136136 s |

For random input, Basic Quicksort was faster in my experiment. This is because the improved version performs additional operations, such as random pivot selection and handling smaller partitions with insertion sort.

For already sorted input, Basic Quicksort raised a `RecursionError` at every tested size. Improved Quicksort completed all the tests successfully.

For input containing many duplicate values, Basic Quicksort raised a `RecursionError` at 16,000 elements and above. Improved Quicksort completed all tested sizes.

### 4.2 Worst-Case Recurrence

When Basic Quicksort uses the last element as the pivot on an already sorted list, the pivot is always the largest element. This produces one partition containing almost all the elements and another empty partition.

The recurrence is:

\[
T(n)=T(n-1)+\Theta(n)
\]

Expanding the recurrence gives:

\[
T(n)=\Theta(n^2)
\]

Therefore, Basic Quicksort has quadratic worst-case time complexity for this input pattern. It also creates deep recursive calls, which can cause a `RecursionError` in Python.

## 5. Finding the Best Cutoff

I tested six different cutoff values using 100,000 random integers to find which cutoff gave the best execution time.

| Cutoff | Execution time |
|---:|---:|
| 1 | 0.247642 s |
| 4 | 0.235417 s |
| 8 | 0.222581 s |
| 16 | **0.213908 s** |
| 32 | 0.226256 s |
| 64 | 0.247377 s |

The cutoff of **16** gave the lowest execution time in my experiment. Therefore, I selected 16 as the default cutoff for Improved Quicksort.

A very small cutoff causes more Quicksort partitioning, while a very large cutoff makes insertion sort handle bigger partitions. The cutoff of 16 gave the best balance among the tested values.

## 6. Comparison with Python sorted()

I also compared Improved Quicksort using the selected cutoff of 16 with Python's built-in `sorted()` function.

| Sorting method | Execution time |
|---|---:|
| Improved Quicksort (cutoff 16) | 0.213908 s |
| Python `sorted()` | 0.017696 s |

Python's built-in `sorted()` was approximately 12.1 times faster in this experiment.

This is because Python uses Timsort, which is highly optimised and takes advantage of existing ordered sections in the data. The built-in implementation also benefits from efficient internal code. The experiment shows the overall performance difference, although it does not separate the effects of the algorithm from the implementation language.


### Part D: Critical Reflection

**1. Why did the basic quicksort fail on sorted data, and which assumption of the average-case analysis did real data break?**

The basic quicksort uses the last element as its pivot. When the input is already sorted, the pivot is always the largest element. This creates one large partition and one empty partition. As a result, the algorithm repeatedly processes almost the entire remaining list. Its running time becomes O(n²), and the recursion can exceed Python's recursion limit. The average-case analysis assumes that partitions are reasonably balanced, but this assumption did not hold for the already sorted data.

**2. Insertion sort is Θ(n²). Why does using it for small parts make quicksort faster?**

Although insertion sort has O(n²) time complexity, it performs well on small lists because it is simple and has very little overhead. It does not need recursive calls or complicated partitioning. In my experiment, cutoff 16 gave the best result of 0.213908 seconds for 100,000 random values. It was faster than the other tested cutoff values.

**3. Why is `sorted()` still faster than your best version? How much of the difference comes from the algorithm and how much from the language?**

Python's `sorted()` was faster because it uses Timsort, which is highly optimised and can take advantage of existing ordered sections in the data. It is also implemented efficiently in CPython, while my quicksort implementation uses Python-level code. In my experiment, `sorted()` took 0.017696 seconds, while improved quicksort took 0.213908 seconds. This shows that both the sorting algorithm and implementation language contribute to the performance difference. I cannot determine the exact contribution of each from this experiment alone.

## 8. Conclusion

In this assignment, I implemented and tested Basic Quicksort and Improved Quicksort. Both algorithms passed the correctness tests. However, the performance tests showed that Basic Quicksort can fail on already sorted input and large duplicate-heavy lists because of unbalanced partitions and excessive recursion.

Improved Quicksort handled all the tested input sizes successfully. The cutoff experiment showed that 16 was the best value among the tested cutoffs. However, Python's built-in `sorted()` was still significantly faster.

Overall, this assignment helped me understand the importance of pivot selection, recursion depth, insertion sort for small partitions, and testing algorithms with different types of input.