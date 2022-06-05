def Edmonds_Karp(C, s, t):

    def BFS(C, s, t, F):
        n = len(C)
        Q = deque()
        visited = [False]*n
        visited[s] = True
        parent = [None]*n
        Q.append(s)
        while len(Q) != 0:
            u = Q.popleft()
            for v in range(n):
                if C[u][v] - F[u][v] > 0 and not visited[v]:
                    parent[v] = u
                    visited[v] = True
                    Q.append(v)
        if not visited[t]:
            return 0, parent
        else:
            min_flow = float('inf')
            curr = t
            while curr != s:
                min_flow = min(min_flow, C[parent[curr]][curr] - F[parent[curr]][curr])
                curr = parent[curr]
            return min_flow, parent

    flow = 0
    n = len(C)
    F = [[0]*n for _ in range(n)]
    while True:
        m, parent = BFS(C, s, t, F)
        if m == 0:
            break
        flow += m
        curr = t
        while curr != s:
            u = parent[curr]
            C[u][curr] -= m
            F[curr][u] += m
            curr = u

    return flow