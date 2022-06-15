from queue import PriorityQueue

def Prim(G):
    n = len(G)
    INF = float('inf')
    parent = [None]*n
    weight = [INF for _ in range(n)]
    weight[0] = 0
    visited = [None]*n
    Q = PriorityQueue()
    Q.put((0, 0))
    while not Q.empty():
        w, t = Q.get()
        visited[t] = True
        for u in G[t]:
            if weight[u[0]] > u[1] and not visited[u[0]]:
                weight[u[0]] = u[1]
                parent[u[0]] = t
                Q.put((u[1], u[0]))
    return parent


G = [
    [(1, 1), (5, 1), (6, 3)],
    [(0, 1), (2, 1), (6, 2)],
    [(1, 1), (3, 6), (6, 5)],
    [(2, 6), (4, 1)],
    [(3, 1), (5, 2), (6, 7)],
    [(0, 1), (4, 2)],
    [(0, 3), (1, 2), (2, 5), (4, 7)],
]

print(Prim(G))
