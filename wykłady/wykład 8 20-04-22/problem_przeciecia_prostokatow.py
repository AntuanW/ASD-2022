#todo

"""
-                       P1 P2 P3 P4 P5 P6
P0                      P2 P3 P4 P5 P6
P0 P1                   P3 P4 P5 P6
P0 P1 P2                P4 P5 P6
P0 P1 P2 P3             P5 P6
P0 P1 P2 P3 P4          P6
P0 P1 P2 P3 P4 P5       -
"""


def delete_rectangle(T):
    INF = float('inf')

    def common(a, b):
        #funkcja zwracajace przeciecie 2 prostokatow
        return ((-1, 1), (1, -1))
    def area(a, b):
        return abs(a[0] - b[0])*abs(a[1] - b[1])

    n = len(T)
    A = [None]*n
    A[0] = ((-INF, INF), (INF, -INF))
    B = [None]*n
    B[n-1] = ((-INF, INF), (INF, -INF))

    for i in range(1, n):
        A[i] = common(A[i-1], T[i-1])
        B[n-i-1] = common(B[n - i], T[n-i])

    a, b = common(A[0], B[0])
    best = area(a, b)
    delete = 0
    for i in range(1, n):
        a, b = common(A[i], B[i])
        if area(a, b) > best:
            best = area(a, b)
            delete = i
    return delete
