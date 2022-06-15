def Floyd_Warshall(G):
    n = len(G)
    M = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j, w in G[i]:
            M[i][j] = w
        M[i][i] = 0

    for t in range(n):
        for u in range(n):
            for v in range(n):
                M[u][v] = min(M[u][v], M[u][t] + M[t][v])
    return M
