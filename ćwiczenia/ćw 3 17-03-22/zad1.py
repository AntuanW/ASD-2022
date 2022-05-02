def quick_sort(T, left, right):
    def partition(A, p, r):
        x = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1

    while left < right:
        x = partition(T, left, right)
        if x - left < right - x:
            quick_sort(T, left, x-1)
            left = x + 1
        else:
            quick_sort(T, x+1, right)
            right = x-1
