def longest_common_sub(A, B):
    n = len(A)
    F = [[0 for _ in range(n+1)] for _ in range(n+1)]   # F[i][j] - dl najdluzszego wspolnego podciagu dla A[0, .., i-1] oraz B[0, ..., j-1]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if A[i-1] == B[j-1]:
                F[i][j] = F[i-1][j-1] + 1
            else:
                F[i][j] = max(F[i-1][j], F[i][j-1])
    return F[n][n]

def lcs_path(A, B):
    n = len(A)
    F = [[0 for _ in range(n+1)] for _ in range(n+1)]   # F[i][j] - dl najdluzszego wspolnego podciagu dla A[0, .., i-1] oraz B[0, ..., j-1]
    P = [[None for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if A[i-1] == B[j-1]:
                F[i][j] = F[i-1][j-1] + 1
                P[i][j] = (i-1, j-1, A[i-1])
            else:
                if F[i-1][j] >= F[i][j-1]:
                    F[i][j] = F[i-1][j]
                    P[i][j] = (i-1, j, None)
                else:
                    F[i][j] = F[i][j-1]
                    P[i][j] = (i, j-1, None)
    res = []
    curr = P[n][n]
    while curr != None:
        if curr[2] != None:
            res.append(curr[2])
        curr = P[curr[0]][curr[1]]
    return res[::-1]
