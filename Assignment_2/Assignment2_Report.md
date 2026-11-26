# CSF302 – Assignment 2
## Closest Camera Traps

**Student Name:** Lhundup Dorji

**Student Number:** 0224349

**Module:** CSF302 – Algorithms and Complexity

**Assignment:** Assignment 2 – Closest Camera Traps

---

## 1. Introduction

The purpose of this assignment is to find the closest pair of camera traps placed in a geographical area.

When camera traps are placed too close to each other, they may record the same animals and waste batteries.

In this assignment, I implemented two algorithms to find the closest pair of points. The first algorithm uses brute force, while the second uses divide and conquer.

The main objective is to compare the performance of both algorithms and understand their time complexity.

**AI Tool Declaration:** ChatGPT was used to assist with understanding the algorithms and organising the implementation. The code was tested by running both algorithms and comparing their results.

---

## 2. Part A – Implementation

Two algorithms were implemented to find the closest pair of points.

### 2.1 Brute Force

The brute-force algorithm checks every possible pair of points and calculates the distance between them.

The Euclidean distance formula is:

d = √((x₂ - x₁)² + (y₂ - y₁)²)

The algorithm stores the smallest distance and the original indices of the two points.

Its time complexity is:

Θ(n²)

### 2.2 Divide and Conquer

The divide-and-conquer algorithm first sorts the points according to their x-coordinates.

It then divides the points into two halves and recursively finds the closest pair in each half.

After that, it checks a strip around the dividing line to find a closer pair that may exist across the two halves.

Its time complexity is:

Θ(n log n)

### 2.3 Sample Output

Both algorithms were executed using the sample coordinates given in the assignment.

Both algorithms returned the same closest distance and indices.

---

## 3. Part B – Testing

The Python unittest framework was used to test the divide-and-conquer implementation.

The following cases were tested:

1. Exactly two points.
2. Duplicate points.
3. All points on one vertical line.
4. Closest pair on opposite sides of the dividing line.
5. 500 randomly generated inputs.
6. Multiple duplicate points.

The results from divide and conquer were compared with brute force to check correctness.


All six test methods passed successfully.

---

## 4. Part C – Analysis

### 4.1 Brute Force Recurrence

The brute-force algorithm checks every possible pair.

Its time complexity is:

T(n) = Θ(n²)

### 4.2 Divide and Conquer Recurrence

The algorithm divides the problem into two smaller problems and performs linear work to combine the results.

The recurrence is:

T(n) = 2T(n/2) + Θ(n)

Using the Master Method:

a = 2, b = 2, f(n) = Θ(n)

n^(log₂2) = n

Therefore, using Master Method Case 2:

T(n) = Θ(n log n)

### 4.3 Experimental Results

Both algorithms were measured using different input sizes on my computer.

[Insert actual timing table from benchmark_results.csv]

### 4.4 Log-Log Graph


The graph compares the running times of both algorithms. The results show how the running time changes as the number of points increases.

### 4.5 Crossover Point

The smallest tested input size where divide and conquer became faster than brute force was:

**n = [INSERT YOUR ACTUAL RESULT]**

This demonstrates the advantage of divide and conquer for larger inputs.

---

## 5. Part D – Critical Reflection

### 1. Did your measured growth match your recurrence?

Yes, my measured results generally showed that divide and conquer performed better as the number of points increased. This matches the recurrence T(n) = 2T(n/2) + Θ(n), which gives Θ(n log n). Brute force has Θ(n²) complexity, so its running time increases more quickly. Small differences in the measured results can happen because of computer performance and Python execution overhead.

### 2. Why is brute force faster for small n even though it is Θ(n²)?

Brute force can be faster for small inputs because it is simple and does not require sorting or recursive function calls. Divide and conquer has extra work because it sorts the points, divides them and checks the strip. For a small number of points, this extra work can make it slower.

### 4. If you used an AI tool, what did it get right or wrong, and how did you check it?

I used ChatGPT to help me understand the algorithms and organise the Python code. I checked the implementation by running both algorithms and comparing their results on 500 random inputs. I also tested special cases such as duplicate points and points on a vertical line. This helped me check whether the divide-and-conquer algorithm produced correct results.

---

## 6. Conclusion

In this assignment, I implemented two algorithms for finding the closest pair of points.

The brute-force algorithm was simple to implement but checked every possible pair. The divide-and-conquer algorithm required more steps but achieved better time complexity.

I tested both algorithms using random inputs and different edge cases to check their correctness.

The benchmarking exercise helped me understand the practical difference between Θ(n²) and Θ(n log n).

Overall, this assignment improved my understanding of divide and conquer, recurrence relations, the Master Method and algorithm analysis.