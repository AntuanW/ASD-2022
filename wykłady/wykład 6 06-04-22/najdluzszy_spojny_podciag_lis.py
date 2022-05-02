def lis(A):
    n = len(A)
    maxi = 0
    F = [1]*n
    #F[i] - dł. najdłuższego rosnącego podciągu w tablicy A[0,..,i] kończący się na i
    P = [-1]*n
    for i in range(1, n):
        for j in range(0, i):
            if A[i] > A[j] and F[j]+1 > F[i]:
                F[i] = F[j]+1
                P[i] = j
        if F[i] > F[maxi]:
            maxi = i
    return F[maxi]


def printSol(A, P, i):
    if P[i] != -1:
        printSol(A, P, P[i])
    print(A[i], end=" ")

