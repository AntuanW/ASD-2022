#todo

# do poprawy
def zad5(A, k):
    INF = float('inf')
    n = len(A)
    S = [0] * (n + 1)
    for i in range(1, n + 1):
        S[i] = S[i - 1] + A[i - 1]

    def find_sum(i, j):
        nonlocal S
        return S[j + 1] - S[i]

    F = [[None for _ in range(k + 1)] for _ in range(n)]
    for i in range(n):
        F[i][0] = INF
    for i in range(1, k + 1):
        F[0][i] = INF

    def rek(i, t):
        nonlocal F, A
        if F[i][t] is not None: return F[i][t]
        if i == t:
            F[i][t] = min(A[:i])
            return F[i][t]
        else:
            maksi = -INF
            for l in range(t - 1, i):
                res = min(rek(l, t - 1), find_sum(l + 1, i))
                maksi = max(maksi, res)
            F[i][t] = maksi
            return maksi

    rek(n - 1, k)

    return F


x = zad5([3, 5, 7, 1, 4, 6, 1, 3, 4, 5], 4)
for i in range(len(x)):
    print(x[i])