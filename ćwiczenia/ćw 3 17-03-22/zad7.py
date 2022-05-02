def hoare_partition(A, p, r):
    pivot = A[p]
    i = p - 1
    j = r + 1
    while True:
        i += 1
        while A[i] < pivot:
            i += 1

        j -= 1
        while A[j] > pivot:
            j -= 1

        if i >= j:
            return j

        A[i], A[j] = A[j], A[i]


def quicksort(A, p, r):
    if p < r:
        pivot = hoare_partition(A, p, r)
        quicksort(A, p, pivot)
        quicksort(A, pivot+1, r)

