def Stack():
    return []


def IsEmpty(S):
    if len(S) == 0:
        return True
    return False


def push(S, x):
    S.append(x)


def remove(S):
    return S.pop()


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1


def quick_sort(T, l, r):
    S = Stack()
    push(S, (l, r))
    while not IsEmpty(S):
        l, r = remove(S)
        if l < r:
            x = partition(T, l, r)
            push(S, (l, x-1))
            push(S, (x+1, r))
