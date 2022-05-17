from collections import deque


def czy_dwudzielny(G):
    n = len(G)
    Q = deque()
    visited = [0]*n
    visited[0] = 1
    Q.append(0)
    while not len(Q) == 0:
        u = Q.popleft()
        colour = visited[u]
        for v in G[u]:
            if visited[v] == colour:
                return False
            if visited[v] == 0:
                visited[v] = -1 * colour
                Q.append(v)
    return True


def liczba_spojnych_skladowych(G):

    def DFS_visit(u):
        nonlocal G, visited
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS_visit(v)

    n = len(G)
    counter = 0
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            counter += 1
            DFS_visit(i)

    return counter
