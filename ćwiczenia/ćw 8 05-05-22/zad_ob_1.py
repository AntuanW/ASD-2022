from collections import deque

def zad1(G):
    def Bfs_lists(G, s):
        n = len(G)
        Q = deque()
        dist = [-1] * n
        dist[s] = 0
        Q.append(s)

        while len(Q) != 0:
            u = Q.popleft()
            for v in G[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    Q.append(v)
        return dist

    dist = Bfs_lists(G, 0)
    n = len(G)
    for i in range(n):
        dist[i] = (i, dist[i])
    dist.sort(reverse=True, key=lambda x: x[1])
    for i in range(n):
        dist[i] = dist[i][0]

    return dist


G = [
    [1, 2],  # 0
    [0, 3],  # 1
    [0, 4],  # 2
    [1, 5, 6],  # 3
    [2, 7],  # 4
    [3, 9],  # 5
    [3, 9],  # 6
    [4, 8],  # 7
    [7, 9],  # 8
    [5, 6, 8, 10],  # 9
    [9, 11, 12],  # 10
    [10, 13],  # 11
    [10, 13],  # 12
    [11, 12],  # 13
]

print(zad1(G))