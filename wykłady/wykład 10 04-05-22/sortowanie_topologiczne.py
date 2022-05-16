def topological_sort(G):

    def DFS_visit(u):
        nonlocal visited, G, res
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS_visit(v)
        res.append(u)

    res = []
    n = len(G)
    visited = [False]*n
    for u in range(n):
        if not visited[u]:
            DFS_visit(u)
    return res[::-1]

T =[
    [1, 2],         # A 0
    [4],            # B 1
    [3],            # C 2
    [7],         # D 3
    [5, 7],         # E 4
    [6],             # F 5
    [],        # G 6
    [6],     # H 7
]

x = topological_sort(T)
for i in range(len(T)):
    print(chr(ord("A")+x[i]))