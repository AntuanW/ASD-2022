from zad3testy import runtests


def iamlate( T, V, q, l):
    n = len(T) + 1
    T.append(l)
    V.append(0)
    INF = float("inf")
    F = [[INF for _ in range(q+1)] for _ in range(n)]
    P = [[None for _ in range(q+1)] for _ in range(n)]
    for i in range(min(V[0], q) + 1):
        F[0][i] = 1
    for i in range(1, n):
        for e in range(q+1):
            best = INF
            for j in range(i):
                if q >= e - min(V[i], q) -T[j] + T[i] >= 0:
                    if best > F[j][e - min(V[i], q) -T[j] + T[i]]:
                        best = F[j][e - min(V[i], q) -T[j] + T[i]]
                        F[i][e] = best + 1
                        P[i][e] = (j, F[j][e - min(V[i], q) -T[j] + T[i]], True)
    best = INF
    for i in range(q+1):
        if F[n-1][i] < best:
            best = F[n-1][i]
            idx = i
    if best == INF: return []
    res = []
    curr = P[n-1][idx]
    while curr != None:
        if curr[2]:
            res.append(idx)
        idx = curr[0]
        curr = P[curr[0]][curr[1]]
    res.append(0)
    res = res[::-1]
    res.pop()
    return res


runtests( iamlate )
