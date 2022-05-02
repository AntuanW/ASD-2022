def klocki(A):
    def czy_zawiera(i, j):  # czy i mozna polozyc na j
        return j[1] >= i[1] and j[0] <= i[0]

    n = len(A)
    F = [1] * n
    P = [None] * n
    for i in range(1, n):
        res = 1
        res_idx = None
        for j in range(i):
            if czy_zawiera(A[i], A[j]) and res < F[j] + 1:
                res = F[j] + 1
                res_idx = j
        F[i] = res
        P[i] = res_idx
    best_idx = 0
    for i in range(n):
        if F[best_idx] < F[i]:
            best_idx = i
    R = [1] * n
    curr = best_idx
    while curr is not None:
        R[curr] = 0
        curr = P[curr]

    return n - F[best_idx], R


A = [(1, 2), (3, 4), (1, 4), (2, 4), (3, 5), (3, 5), (4, 5), (0, 3)]
print(klocki(A))
