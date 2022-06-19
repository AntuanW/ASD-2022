#Antoni Wójcik
"""
Opis algorytmu:
Algorytm bazuje na algorytmie Dijkstry.
Najpierw przygotowuję graf dodając krawędzie miedzy osobliwościami z wagą 0.
Następnie znajduję najkrótszą ścieżkę między wierzchołkami a i b uzywając algorytmu Dijkstry.
Złożoność czasowa: O(n^2)
"""

from kol3atesty import runtests
import heapq

def spacetravel( n, E, S, a, b ):
    def dijkstra(G, W, s):
        def relax(u, v):
            nonlocal parent, G, dist, W, Q
            if dist[v] > dist[u] + W[u][v]:
                dist[v] = dist[u] + W[u][v]
                parent[v] = u
                heapq.heappush(Q,(dist[v], v))
        n = len(G)
        dist = [float('inf')] * n
        dist[s] = 0
        parent = [None] * n
        Q = []
        heapq.heappush(Q, (0, s))
        while len(Q) != 0:
            u = heapq.heappop(Q)
            u = u[1]
            for v in G[u]:
                relax(u, v)
        return dist

    G = [[] for _ in range(n)]
    W = [[-1 for _ in range(n)] for _ in range(n)]
    for i, j, k in E:
        W[i][j] = k
        W[j][i] = k
    for i in range(len(S)):
        for j in range(len(S)):
            if S[i] != S[j]:
                W[S[i]][S[j]] = 0
                W[S[j]][S[i]] = 0
    for i in range(n):
        for j in range(n):
            if W[i][j] != -1:
                G[i].append(j)
    dist = dijkstra(G, W, a)
    if dist[b] != float('inf'):
        return dist[b]
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
