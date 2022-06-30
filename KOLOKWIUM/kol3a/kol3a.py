#Antoni Wójcik
"""
Opis algorytmu:
1. Tworze graf g na podstawie listy krawedzi
2. Obliczam odleglosci od wierzholka a i od wierzcholka b za pomoca dijkstry
3. Rozwiazaniem bedzie albo odlegosc od a do b albo odleglosc od a do najblizszej supergwiazdy + odl z b do najblizszej supergwiazdy
"""
from kol3atesty import runtests
import heapq

def spacetravel( n, E, S, a, b ):
    def dijkstra(G, s):
        def relax(u, v, w):
            nonlocal G, dist, Q
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(Q,(dist[v], v))
        n = len(G)
        dist = [float('inf')] * n
        dist[s] = 0
        Q = []
        heapq.heappush(Q, (0, s))
        while len(Q) != 0:
            u = heapq.heappop(Q)[1]
            for v in G[u]:
                relax(u, v[0], v[1])
        return dist

    G = [[] for _ in range(n)]
    for i, j, w in E:
        G[i].append((j, w))
        G[j].append((i, w))
    dist_from_a = dijkstra(G, a)
    dist_from_b = dijkstra(G, b)
    curr_dist = dist_from_a[b]
    star_a = float('inf')
    star_b = float('inf')
    for x in S:
        star_a = min(star_a, dist_from_a[x])
        star_b = min(star_b, dist_from_b[x])

    curr_dist = min(curr_dist, star_a + star_b)
    if curr_dist != float('inf'):
        return curr_dist
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
