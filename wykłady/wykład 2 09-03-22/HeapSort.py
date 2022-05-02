def heap_sort(A):
    def left(i): return 2*i + 1
    def right(i): return 2*i + 2
    def parent(i): return (i-1)//2

    def heapify(A, n, i):
        l = left(i)
        r = right(i)
        max_ind = i
        if l < n and A[l] > A[max_ind]:
            max_ind = l
        if r < n and A[r] > A[max_ind]:
            max_ind = r
        if max_ind != i:
            A[i], A[max_ind] = A[max_ind], A[i]
            heapify(A, n, max_ind)
        return

    def build_heap(A):
        n = len(A)
        for i in range(parent(n-1), -1, -1):
            heapify(A, n, i)
        return

    n = len(A)
    build_heap(A)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)
    return


T = [3,5,2,423,5,23,1,6,7,34,5,6,1,3,5,6,3,2,8]
heap_sort(T)
print(T)