def hamilton_DAG(G):    # reprezentacja listowa
    def topological_sort(G, n):
        def DFS_visit(u):
            nonlocal visited, G, res
            visited[u] = True
            for v in G[u]:
                if not visited[v]:
                    DFS_visit(v)
            res.append(u)

        res = []
        visited = [False] * n
        for u in range(n):
            if not visited[u]:
                DFS_visit(u)
        return res[::-1]

    n = len(G)
    M = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in G[i]:
            M[i][j] = True

    path = topological_sort(G, n)
    for i in range(n-1):
        if not M[path[i]][path[i+1]]:
            return []
    return path


G = [
    [1, 2, 3, 4],
    [2, 3],
    [3, 4],
    [4],
    [],
]

print(hamilton_DAG(G))