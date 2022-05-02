def sort(A):
    def insert(A, x):
        A.append(x)
        n = len(A)
        if n == 1:
            return
        i = n - 2
        while i >= 0 and A[i][0] > x[0]:
            A[i + 1] = A[i]
            i -= 1
        A[i + 1] = x

    def bin_search(A, low, high, key):
        if high >= low:
            mid = low + (high - low) // 2
            if A[mid][0] == key:
                return mid
            elif A[mid][0] > key:
                return bin_search(A, low, mid - 1, key)
            else:
                return bin_search(A, mid + 1, high, key)
        else:
            return -1


    B = []
    n = len(A)
    for i in range(n):
        index = bin_search(B, 0, len(B)-1, A[i])
        if index == -1:
            insert(B, [A[i], 1])
        else:
            B[index][1] += 1

    curr = 0
    for i in range(len(B)):
        for _ in range(B[i][1]):
            A[curr] = B[i][0]
            curr += 1
