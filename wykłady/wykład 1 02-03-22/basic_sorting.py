def insertion_sort(A): #dla N = 10 000  1.92s
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    return A


def selection_sort(A): #dla N = 10 000  1.81s
    n = len(A)
    for i in range(n-1):
        smallest_index = i
        for j in range(i+1, n):
            if A[j] < A[smallest_index]:
                smallest_index = j
        A[i], A[smallest_index] = A[smallest_index], A[i]
    return A


def bubble_sort(arr): #dla N = 10 000  4.32s
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
