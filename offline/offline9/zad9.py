#Antoni Wójcik
"""
Algorytm brute-force. Dla każdej pary wierzchołków u,v wsród których nie ma wierzchołka s, obliczam maksymalny przepływ algorytmem
Edmondsa - karpia. Sprowadza się to wtedy do problemu minimlanego przepływu z 2 ujściami - korzystam z triku i tworzę superujście.
Złożoność O(V^3 E^2)
"""


from zad9testy import runtests

def maxflow( G,s ):
    from collections import deque

    def build_graph(G, a, b):
        n = max(G, key=lambda x: x[1])[1] + 1
        graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in G:
            graph[i[0]][i[1]] = i[2]
        graph[a][n] = float('inf')
        graph[b][n] = float('inf')
        return graph

    def Edmonds_Karp(C, s, t):

        def BFS(C, s, t, F):
            n = len(C)
            Q = deque()
            visited = [False] * n
            visited[s] = True
            parent = [None] * n
            Q.append(s)
            while len(Q) != 0 and not visited[t]:
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
        F = [[0] * n for _ in range(n)]
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

    n = max(G, key=lambda x: x[1])[1] + 1
    best = -float('inf')
    for i in range(n):
        for j in range(i, n):
            if i != s and j != s:
                M = build_graph(G, i, j)
                res = Edmonds_Karp(M, s, n)
                if res > best:
                    best = res
    return best

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxflow, all_tests = True )
