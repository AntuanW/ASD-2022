#todo
from collections import deque
def path(G, start, meta):

    def BFS(s):
        nonlocal G, parent, visited
        Q = deque()
        visited[s] = True
        Q.append(s)
        while len(Q) != 0:
            u = Q.popleft()
            for v in G[u]:
                if not visited[v]:
                    visited[v] = True
                    parent[v] = u
                    Q.append(v)

    n = len(G)
    parent = [None]*n
    visited = [False]*n

    BFS(start)
    res = []

    if not visited[meta]:
        return res

    curr = meta
    while curr != None:
        res.append(curr)
        curr = parent[curr]
    return res
