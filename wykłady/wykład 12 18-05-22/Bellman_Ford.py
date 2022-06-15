def bellman_ford(G, W, s):

    def relax(u, v):
        nonlocal parent, G, dist, W
        if dist[v] > dist[u] + W[u][v]:
            dist[v] = dist[u] + W[u][v]
            parent[v] = u

    n = len(G)
    dist = [float('inf')]*n
    dist[s] = 0
    parent = [None]*n

    for _ in range(n-1):
        for u in range(n):
            for v in G[u]:
                relax(u, v)

    for u in range(n):
        for v in G[u]:
            if dist[v] > dist[u] + W[u][v]:
                return None

    return parent

