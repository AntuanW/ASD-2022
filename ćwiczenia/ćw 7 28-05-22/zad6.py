def find_spot(A):
    def partition(A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1

    def select(A, p, k, r):
        if p == r:
            return A[p]
        if p < r:
            q = partition(A, p, r)
            if q == k:
                return A[q]
            elif q < k:
                return select(A, q + 1, k, r)
            else:
                return select(A, p, k, q - 1)

    n = len(A)
    if n%2 == 1:
        return select(A, 0, n//2, n-1)
    else:
        return (select(A, 0, n//2 - 1, n-1) + select(A, 0, n//2, n-1))/2
