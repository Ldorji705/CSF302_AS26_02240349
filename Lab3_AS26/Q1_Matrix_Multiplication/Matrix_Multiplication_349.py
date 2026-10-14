"""
Q1: Traditional Matrix Multiplication vs Strassen's Algorithm
Student suffix used in identifiers: 349

Run:
    python3 Matrix_Multiplication_349.py
"""

import random as random_349
import time as time_349


def Is_Power_Of_Two_349(Number_349):
    return Number_349 > 0 and (Number_349 & (Number_349 - 1)) == 0


def Add_Matrices_349(Matrix_A_349, Matrix_B_349):
    Size_349 = len(Matrix_A_349)
    return [[Matrix_A_349[Row_349][Col_349] + Matrix_B_349[Row_349][Col_349]
             for Col_349 in range(Size_349)] for Row_349 in range(Size_349)]


def Subtract_Matrices_349(Matrix_A_349, Matrix_B_349):
    Size_349 = len(Matrix_A_349)
    return [[Matrix_A_349[Row_349][Col_349] - Matrix_B_349[Row_349][Col_349]
             for Col_349 in range(Size_349)] for Row_349 in range(Size_349)]


def Traditional_Multiply_349(Matrix_A_349, Matrix_B_349):
    """Multiply two square matrices using three nested loops: O(n^3)."""
    Size_349 = len(Matrix_A_349)
    Result_349 = [[0] * Size_349 for _ in range(Size_349)]

    for Row_349 in range(Size_349):
        for Col_349 in range(Size_349):
            for Inner_349 in range(Size_349):
                Result_349[Row_349][Col_349] += (
                    Matrix_A_349[Row_349][Inner_349] * Matrix_B_349[Inner_349][Col_349]
                )
    return Result_349


def Strassen_Multiply_349(Matrix_A_349, Matrix_B_349):
    """Strassen's divide-and-conquer algorithm."""
    Size_349 = len(Matrix_A_349)

    if Size_349 == 1:
        return [[Matrix_A_349[0][0] * Matrix_B_349[0][0]]]

    Half_349 = Size_349 // 2

    A11_349 = [Row_349[:Half_349] for Row_349 in Matrix_A_349[:Half_349]]
    A12_349 = [Row_349[Half_349:] for Row_349 in Matrix_A_349[:Half_349]]
    A21_349 = [Row_349[:Half_349] for Row_349 in Matrix_A_349[Half_349:]]
    A22_349 = [Row_349[Half_349:] for Row_349 in Matrix_A_349[Half_349:]]

    B11_349 = [Row_349[:Half_349] for Row_349 in Matrix_B_349[:Half_349]]
    B12_349 = [Row_349[Half_349:] for Row_349 in Matrix_B_349[:Half_349]]
    B21_349 = [Row_349[:Half_349] for Row_349 in Matrix_B_349[Half_349:]]
    B22_349 = [Row_349[Half_349:] for Row_349 in Matrix_B_349[Half_349:]]

    M1_349 = Strassen_Multiply_349(Add_Matrices_349(A11_349, A22_349), Add_Matrices_349(B11_349, B22_349))
    M2_349 = Strassen_Multiply_349(Add_Matrices_349(A21_349, A22_349), B11_349)
    M3_349 = Strassen_Multiply_349(A11_349, Subtract_Matrices_349(B12_349, B22_349))
    M4_349 = Strassen_Multiply_349(A22_349, Subtract_Matrices_349(B21_349, B11_349))
    M5_349 = Strassen_Multiply_349(Add_Matrices_349(A11_349, A12_349), B22_349)
    M6_349 = Strassen_Multiply_349(Subtract_Matrices_349(A21_349, A11_349), Add_Matrices_349(B11_349, B12_349))
    M7_349 = Strassen_Multiply_349(Subtract_Matrices_349(A12_349, A22_349), Add_Matrices_349(B21_349, B22_349))

    C11_349 = Add_Matrices_349(Subtract_Matrices_349(Add_Matrices_349(M1_349, M4_349), M5_349), M7_349)
    C12_349 = Add_Matrices_349(M3_349, M5_349)
    C21_349 = Add_Matrices_349(M2_349, M4_349)
    C22_349 = Add_Matrices_349(Subtract_Matrices_349(Add_Matrices_349(M1_349, M3_349), M2_349), M6_349)

    Result_349 = [[0] * Size_349 for _ in range(Size_349)]
    for Row_349 in range(Half_349):
        for Col_349 in range(Half_349):
            Result_349[Row_349][Col_349] = C11_349[Row_349][Col_349]
            Result_349[Row_349][Col_349 + Half_349] = C12_349[Row_349][Col_349]
            Result_349[Row_349 + Half_349][Col_349] = C21_349[Row_349][Col_349]
            Result_349[Row_349 + Half_349][Col_349 + Half_349] = C22_349[Row_349][Col_349]
    return Result_349


def Main_349():
    print("Q1: Matrix Multiplication")
    Size_349 = int(input("Enter matrix size (2, 4, 8, 16, ...): "))
    if not Is_Power_Of_Two_349(Size_349):
        print("Please enter a positive power of 2.")
        return

    Matrix_A_349 = [[random_349.randint(1, 9) for _ in range(Size_349)] for _ in range(Size_349)]
    Matrix_B_349 = [[random_349.randint(1, 9) for _ in range(Size_349)] for _ in range(Size_349)]

    if Size_349 <= 8:
        print("\\nMatrix A:")
        for Row_349 in Matrix_A_349:
            print(Row_349)
        print("\\nMatrix B:")
        for Row_349 in Matrix_B_349:
            print(Row_349)

    Start_Traditional_349 = time_349.perf_counter()
    Result_Traditional_349 = Traditional_Multiply_349(Matrix_A_349, Matrix_B_349)
    Time_Traditional_349 = time_349.perf_counter() - Start_Traditional_349

    Start_Strassen_349 = time_349.perf_counter()
    Result_Strassen_349 = Strassen_Multiply_349(Matrix_A_349, Matrix_B_349)
    Time_Strassen_349 = time_349.perf_counter() - Start_Strassen_349

    print("\\nTraditional result:")
    for Row_349 in Result_Traditional_349 if Size_349 <= 8 else Result_Traditional_349[:4]:
        print(Row_349 if Size_349 <= 8 else Row_349[:4])

    print("\\nStrassen result:")
    for Row_349 in Result_Strassen_349 if Size_349 <= 8 else Result_Strassen_349[:4]:
        print(Row_349 if Size_349 <= 8 else Row_349[:4])

    print("\\nDo the results match?", Result_Traditional_349 == Result_Strassen_349)
    print(f"Traditional time: {Time_Traditional_349:.6f} seconds")
    print(f"Strassen time: {Time_Strassen_349:.6f} seconds")
    # Conclusion: Both methods should give the same result. Strassen is theoretically
    # faster for large matrices, but its extra additions can slow it down for small inputs.


if __name__ == "__main__":
    Main_349()
