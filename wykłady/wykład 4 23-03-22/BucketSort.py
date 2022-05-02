def bucket_sort(A):
    def insertion_sort(A):
        for j in range(1, len(A)):
            key = A[j]
            i = j-1
            while i >= 0 and A[i] > key:
                A[i+1] = A[i]
                i -= 1
            A[i+1] = key
    n = len(A)
    B = [[] for _ in range(n+1)]
    minimal = min(A)
    size = (max(A) - minimal)/n
    for i in A:
        bucket_index = int((i - minimal)//size)
        B[bucket_index].append(i)
    curr_index = 0
    for x in B:
        n = len(x)
        if n != 0:
            insertion_sort(x)
            for i in range(n):
                A[curr_index] = x[i]
                curr_index += 1