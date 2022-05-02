def counting_sort_numbers(A, k):
    n = len(A)
    C = [0]*k
    B = [0]*n
    for x in A:
        C[x] += 1
    for i in range(1, k):
        C[i] = C[i] + C[i-1]
    for i in range(n-1, -1, -1):
        B[ C[ A[i] ] - 1 ] = A[i]
        C[ A[i] ] -= 1
    for i in range(n):
        A[i] = B[i]


def counting_sort(A, k, index):
    n = len(A)
    C = [0] * k
    B = [0] * n
    for x in range(n):
        C[ A[x][index] ]  += 1
    for i in range(1, k):
        C[i] = C[i] + C[i - 1]
    for i in range(n - 1, -1, -1):
        B[C[A[i][index]] - 1] = A[i]
        C[A[i][index]] -= 1
    for i in range(n):
        A[i] = B[i]
