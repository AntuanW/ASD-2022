def matrix_chain_order(p):  #p[1, ..., n]: macierz i ma wymiary p[i-1] x p[i]
    n = len(p) - 1
    m = [[0 for _ in range(n+1)] for _ in range(n+1)]   # m[i][j] optymalne wymnozenie macierzy od i do j
    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i+l-1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q

    return m[1][n]
