def DFS_lists(G):

    def DFS_visit(u):
        nonlocal time, visited, parent, G
        time += 1
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFS_visit(v)
        time += 1

    n = len(G)
    visited = [False]*n
    parent = [None]*n
    time = 0
    for u in range(n):
        if not visited[u]:
            DFS_visit(u)
    return parent

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
