#todo
def silnie_spojne_skladowe(G):
    def reverse_edges(G):
        n = len(G)
        R = [[] for _ in range(n)]
        for i in range(n):
            for x in G[i]:
                R[x].append(i)
        return R

    def DFS_visit(G, u):
        nonlocal visited, post, time
        time += 1
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS_visit(G, v)
        time += 1
        post[u] = time

    def skladowe(u):
        nonlocal ssk, curr, G, visited
        visited[u] = True
        ssk[curr].append(u)
        for v in G[u]:
            if not visited[v]:
                skladowe(v)


    n = len(G)
    visited = [False]*n
    post = [0]*n
    time = 0
    R = reverse_edges(G)
    for u in range(n):
        if not visited[u]:
            DFS_visit(R, u)

    for i in range(n):
        post[i] = (i, post[i])
    post.sort(reverse= True, key= lambda x: x[1])
    for i in range(n):
        post[i] = post[i][0]

    ssk = []
    curr = -1
    visited = [False]*n
    for i in post:
        if not visited[i]:
            ssk.append([])
            curr += 1
            skladowe(i)
    return ssk


G = [
    [1],
    [2, 3, 4],
    [5],
    [],
    [1, 5, 6],
    [2, 7],
    [7, 9],
    [10],
    [6],
    [8],
    [11],
    [9]
]

x = silnie_spojne_skladowe(G)
for i in range(len(x)):
    print(i+1, end=" ")
    for j in range(len(x[i])):
        print(chr(ord("A")+x[i][j]), end=" ")
    print()