def square_Matrix_Multiply(A, B):

    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range (n):
        for j in range (n):
            C[i][j] = 0
            for k in range (n):
                C[i][j] = C[i][j] + A [i][k] * B[k][j]
    return (C)

A = [
        [1,2],
        [3,4]
     ]

B = [
        [5,6],
        [7,8]

    ]
C = [
        [0,0],
        [0,0]
    ]


print(square_Matrix_Multiply(A, B))