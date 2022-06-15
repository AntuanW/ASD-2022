from queue import PriorityQueue

"""
Faster find:
    def find(x):
        while x.parent != x:
            x.parent = x.parent.parent
            x = x.parent
        return x
"""
class Node:
    def __init__(self, value):
        self.parent = self
        self.value = value
        self.rank = 0


def MST(G):     # reprezentacja listowa

    def find(x):
        if x.parent != x:
            x.parent = find(x.parent)
        return x.parent

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        if x.rank > y.rank:
            y.parent = x
        else:
            x.parent = y
            if x.rank == y.rank:
                y.rank += 1
        return

    n = len(G)
    vertex = [None]*n
    for i in range(n):
        vertex[i] = Node(i)

    Q = PriorityQueue()
    for i in range(n):
        for u in G[i]:
            Q.put((u[1], i, u[0]))

    mst = []
    while not Q.empty():
        weight, u, v = Q.get()
        u = vertex[u]
        v = vertex[v]
        if find(u) != find(v):
            mst.append((u.value, v.value))
            union(u, v)

    return mst
