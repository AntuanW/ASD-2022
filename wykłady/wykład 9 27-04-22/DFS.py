"""
Złożoność:
rep. macierzowa -> O(V^2)
rep. listowa -> O(V + E)

Zastosowania:
-spójność,
-dwudzielność,
-wykrywanie cykli,
-sortowanie topologiczne,
-cykl Eulera,
-silnie spójne składowe,
-mosty/pkt. artykulacji
"""
def DFS_lists(G):

    def DFS_visit(u):
        nonlocal time, visited, parent, G, prev, post
        time += 1
        prev[u] = time
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFS_visit(v)
        time += 1
        post[u] = time

    n = len(G)
    visited = [False]*n
    parent = [None]*n
    prev = [0]*n
    post = [0]*n
    time = 0
    for u in range(n):
        if not visited[u]:
            DFS_visit(u)
    return prev, post

G = [
    [1, 2], #A
    [0, 4], #B
    [0, 3, 5], #C
    [2, 4], #D
    [1, 3, 5], #E
    [2, 4, 6], #F
    [5,7], #G
    [6], #H
]

V = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 5, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0],
]

T =[
    [1, 4],         # A 0
    [0],            # B 1
    [3],            # C 2
    [2, 7],         # D 3
    [0, 8],         # E 4
    [],             # F 5
    [7, 10],        # G 6
    [3, 6, 11],     # H 7
    [4, 9],         # I 8
    [8],            # J 9
    [6],            # K 10
    [7],            # L 11
]

x, y = DFS_lists(T)
for i in range(len(x)):
    print(chr(ord("A") + i), x[i], y[i])

