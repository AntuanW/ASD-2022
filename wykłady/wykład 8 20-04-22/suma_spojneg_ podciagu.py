def ssp(A):
    n = len(A)
    F = [0]*n
    F[0] = A[0]
    for i in range(1, n):
        F[i] = max(F[i-1] + A[i], A[i])
    return max(F)

A = [1, 3, -7, -2, 1, 9, -3, 2, -100, 4]
print(ssp(A))