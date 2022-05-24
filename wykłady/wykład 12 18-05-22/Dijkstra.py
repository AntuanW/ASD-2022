from queue import PriorityQueue


def dijkstra(G, W, s):

    def relax(u, v):
        nonlocal parent, G, dist, W, Q
        if dist[v] > dist[u] + W[u][v]:
            dist[v] = dist[u] + W[u][v]
            parent[v] = u
            Q.put((dist[v], v))

    n = len(G)
    dist = [float('inf')]*n
    dist[s] = 0
    parent = [None]*n
    Q = PriorityQueue()
    Q.put((0, s))

    while not Q.empty():
        u = Q.get()
        u = u[1]
        for v in G[u]:
            relax(u, v)

    return parent, dist


G = [
    [1, 6],
    [0, 2, 7],
    [1, 3],
    [2, 4],
    [3, 5, 8],
    [4, 6, 8],
    [0, 5, 7],
    [1, 6, 8],
    [4, 5, 7],
]

W =[
    [0, 1, 0, 0, 0, 0, 2, 0, 0],
    [1, 0, 2, 0, 0, 0, 0, 3, 0],
    [0, 2, 0, 5, 0, 0, 0, 0, 0],
    [0, 0, 5, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 4, 0, 0, 8],
    [0, 0, 0, 0, 4, 0, 7, 0, 1],
    [2, 0, 0, 0, 0, 7, 0, 1, 0],
    [0, 3, 0, 0, 0, 0, 1, 0, 3],
    [0, 0, 0, 0, 8, 1, 0, 3, 0],
]

print(dijkstra(G, W, 0))
