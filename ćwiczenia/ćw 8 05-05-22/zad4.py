from collections import deque

def decreasing_path(G, x, y):

    n = len(G)
    visited = [[False for _ in range(n)] for _ in range(n)]
    Q = deque()
    for i in range(len(G[x])):
        Q.append((G[x][i][0], G[x][i][1]))
        visited[x][G[x][i][0]] = True
        visited[G[x][i][0]][x] = True

    while len(Q) != 0:
        v, weight = Q.popleft()
        for i in range(len(G[v])):
            if not visited[v][G[v][i][0]] and weight > G[v][i][1]:
                visited[v][G[v][i][0]] = True
                visited[G[v][i][0]][v] = True
                Q.append((G[v][i][0], G[v][i][1]))

    for i in range(n):
        if visited[i][y]:
            return True
    return False

G = [
    [(1, 8), (2, 8)],
    [(0, 8), (2, 6), (4, 4), (3, 9)],
    [(0, 8), (1, 6), (3, 7), (4, 1)],
    [(2, 7), (1, 9), (4, 10)],
    [(1, 4), (2, 1), (3, 10), (5, 2)],
    [(4, 2)],
]

print(decreasing_path(G, 0, 5))