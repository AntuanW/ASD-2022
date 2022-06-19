def find_subtraction(A, x): #A[j] - A[i] = x
    n = len(A)
    if n == 0 or n == 1:
        return False
    j = 1
    i = 0
    while i < n and j < n and A[j] - A[i] != x:
        if A[j] - A[i] < x:
            j += 1
        elif A[j] - A[i] > x:
            i += 1
    if i < n and j < n and A[j] - A[i] == x:
        return A[j], A[i]
    else:
        return False


def find_sum(A, x): #A[j] + A[i] = x
    n = len(A)
    if n == 0 or n == 1:
        return False
    j = n-1
    i = 0
    while i != j and A[i] + A[j] != x:
        if A[i] + A[j] < x:
            i += 1
        elif A[i] + A[j] > x:
            j -= 1
    if A[i] + A[j] == x:
        return A[i], A[j]
    else:
        return False
