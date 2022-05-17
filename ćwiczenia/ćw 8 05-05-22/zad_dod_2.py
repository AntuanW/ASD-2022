def czy_nieskierowany(G):
    n = len(G)

    M = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in G[i]:
            M[i][j] = 1

    T = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            T[i][j] = M[j][i]

    for i in range(n):
        for j in range(n):
            if T[i][j] != M[i][j]:
                return False
    return True
