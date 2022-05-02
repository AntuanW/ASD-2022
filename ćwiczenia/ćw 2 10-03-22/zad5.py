def leader(A):

    n = len(A)
    counter = 1
    candidate = A[0]

    for i in range(1, n):
        if A[i] == candidate:
            counter += 1
        else:
            counter -= 1
            if counter == 0:
                candidate = A[i]
                counter += 1

    counter = 0
    for i in range(n):
        if A[i] == candidate:
            counter += 1

    if counter >= n//2 + 1:
        return candidate
    else:
        return False
