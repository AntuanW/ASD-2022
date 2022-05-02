from queue import Queue

# lista sąsiedztwa
def BFS_lists(G, s):
    Q = Queue()
    n = len(G)
    visited = [False]*n
    parent = [None]*n
    dist = [-1]*n

    dist[s] = 0
    visited[0] = True
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                parent[v] = u
                Q.put(v)
    return visited, parent, dist

# macierz sasiedztwa
def BFS_matrix(G, s):
    Q = Queue()
    n = len(G)
    parent = [None]*n
    visited = [False]*n
    dist = [-1]*n

    dist[s] = 0
    visited[0] = True
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for i in range(n):
            if not visited[i] and G[u][i] == 1:
                parent[i] = u
                visited[i] = True
                dist[i] = dist[u] + 1
                Q.put(i)
    return visited, parent, dist

G = [
    [1, 2], #A
    [0, 4], #B
    [0, 3, 5], #C
    [2, 4], #D
    [1, 3, 5], #E
    [2, 4, 6], #F
    [5,7], #G
    [6], #H
]

V = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 5, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0],
]
