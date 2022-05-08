def zad_5(A, k):  # A = [a1, a2, a3, ..., an]

    def find_sum(i, j):  # suma od a1 do aj
        nonlocal prefix
        if i == 1:
            return prefix[j - 1]
        else:
            return prefix[j - 1] - prefix[i - 2]

    def rek(i, t):
        nonlocal F, INF
        if F[i][t] is not None: return F[i][t]
        for o in range(1, t):
            best = min(rek(i - o, t - 1), find_sum(i - o + 1, i))
        F[i][t] = best
        return F[i][t]

    INF = float('inf')
    n = len(A)
    prefix = [A[0]] * n
    for i in range(1, len(A)):
        prefix[i] = prefix[i - 1] + A[i]

    F = [[None for _ in range(k + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        F[i][1] = find_sum(1, i)

    for i in range(1, k + 1):
        F[i][i] = min(A[:i])

    for i in range(n + 1):
        F[i][0] = INF

    for i in range(k + 1):
        F[0][i] = INF

    F[n][k] = rek(n, k)

    return F[n][k]


A = [5, 6, 1, 3, 12, 1, 6, 5, 8, 2, 7]
k = 3
x = zad_5(A, k)
print(x)