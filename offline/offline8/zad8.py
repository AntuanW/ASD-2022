#Antoni Wójcik
"""
Tworzę graf pełny, wagą krawędzi jest długość budowy.
Algorytm sortuje krawedzie rosnąco wagami, uzyskuje w ten sposób tablicę e0, e1, ..., em-1.
Nastepnie dla kazdego podzbioru ei, ..., em-1 znajduje MST zapamiętując max wagę (min waga to bedzie ei - krawedz zawsze bedzie wzieta do MST).
Na bieżąco szukam najmniejszej różnicy wag.
Złożoność O(n^4 log n)
"""

from zad8testy import runtests


def highway( A ):
    class Node:
        def __init__(self):
            self.parent = self
            self.rank = 0
            self.visited = False

    def find(x):
        while x.parent != x:
            x.parent = x.parent.parent
            x = x.parent
        return x

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if x.rank > y.rank:
            y.parent = x
        else:
            x.parent = y
            if x.rank == y.rank:
                y.rank += 1
        return

    def ceil(n):
        return int(-1 * n // 1 * -1)

    def MST(E, idx, m, n, V):
        max_edge = -1
        for i in range(n):
            V[i] = Node()

        for i in range(idx, m):
            weight, u, v = E[i]
            u = V[u]
            v = V[v]
            if find(u) != find(v):
                u.visited = True
                v.visited = True
                union(u, v)
                if weight > max_edge:
                    max_edge = weight

        for i in V:
            if not i.visited:
                return float('inf')

        return max_edge


    INF = float('inf')
    E = []  # krawedzie
    n = len(A)
    for i in range(n-1):
        for j in range(i+1, n):
            E.append( (ceil((( A[i][0] - A[j][0] )**2 + ( A[i][1] - A[j][1] )**2)**(1/2)), i, j) ) # (waga, wierz1, wierz2)
    m = len(E)
    E.sort()
    best = INF
    res = (None, None)
    V = [None]*n
    for i in range(m-n+2):
        min_edge = E[i][0]
        max_edge = MST(E, i, m, n, V)
        if max_edge - min_edge < best:
            best = max_edge - min_edge
            res = (min_edge, max_edge)

    return res[1] - res[0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )
