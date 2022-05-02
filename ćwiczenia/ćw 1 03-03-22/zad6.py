def binary_search(A, x):
    n = len(A)
    l = 0
    r = n - 1
    while l <= r:
        mid = (l+r)//2
        if A[mid] < x:
            l = mid + 1
        elif A[mid] > x:
            r = mid - 1
        else:
            return mid
    return False
