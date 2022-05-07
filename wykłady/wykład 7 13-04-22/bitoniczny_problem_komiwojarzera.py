def bitoniczny_komi(D):
    INF = float('inf')
    n = len(D)
    F = [[INF for _ in range(n)] for _ in range(n)]

    def tspf(i, j):
        nonlocal D, F
        if F[i][j] != INF: return F[i][j]
        if i == j-1:
            best = INF
            for k in range(j-1):
                best = min(best, tspf(k, j-1) + D[k][j])
                F[j-1][j] = best
        else:
            F[i][j] = tspf(i, j-1) + D[j-1][j]
        return F[i][j]

    return F[0][n-1]
