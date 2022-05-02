def find_sum(A, T):
    n = len(A)
    F = [[False for _ in range(T+1)] for _ in range(n)] #F[i][j] - czy mozna zsumowac elementy z A[0, ..., i] do sumy j
    if A[0] <= T:
        F[0][A[0]] = True
    for i in range(n):
        F[i][0] = True
    for i in range(1, n):
        for j in range(1, T+1):
            F[i][j] = F[i-1][j]
            if j - A[i] >= 0 and F[i-1][j-A[i]]:
                F[i][j] = True
    return F[n-1][T]


def find_sum_with_numbers(A, T):
    n = len(A)
    F = [[False for _ in range(T + 1)] for _ in range(n)]
    P = [[(-1, -1, -1) for _ in range(T + 1)] for _ in range(n)]

    for i in range(n):
        F[i][0] = True
        P[i][0] = (-1, -1, -1)
    if A[0] <= T:
        F[0][A[0]] = True
        P[0][A[0]] = (0, 0, A[0])

    for i in range(1, n):
        for j in range(1, T+1):
            F[i][j] = F[i-1][j]
            P[i][j] = P[i-1][j]
            if j - A[i] >= 0 and j - A[i] <= T and F[i-1][j-A[i]]:
                F[i][j] = True
                P[i][j] = (i-1, j-A[i], A[i])
    if not F[n-1][T]:
        return False
    else:
        res = []
        current = P[n-1][T]
        while current != (-1, -1, -1):
            res.append(current[2])
            current = P[current[0]][current[1]]
        return res
