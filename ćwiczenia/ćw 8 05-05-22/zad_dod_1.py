from collections import deque


def kapitan(G, T):
    n = len(G[0])
    m = len(G)
    ruchy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    Q = deque()
    visited[0][0] = True
    Q.append((0, 0))
    while len(Q) != 0:
        row, col = Q.popleft()
        for x in ruchy:
            dest = (row + x[0], col + x[1])
            if 0 <= dest[0] < m and 0 <= dest[1] < n and not visited[dest[0]][dest[1]] and G[dest[0]][dest[1]] >= T:
                visited[dest[0]][dest[1]] = True
                Q.append(dest)
    if visited[m-1][n-1]:
        return True
    else:
        return False
