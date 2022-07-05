def bridge(graph):
    inf = float("inf")
    visited = [False] * len(graph)
    time_visit = [0] * len(graph)
    low = [inf] * len(graph)
    parent = [None] * len(graph)
    time = 0
    for i in range(len(graph)):
        if not visited[i]:
            dfs(graph, i, visited, parent, time_visit, time, low)
    for i in range(len(graph)):
        if time_visit[i] == low[i] and parent[i] is not None:
            print(parent[i], i)


def dfs(graph, source, visited, parent, time_visit, time, low):
    visited[source] = True
    time_visit[source] = time
    time += 1
    low[source] = time_visit[source]
    for v in graph[source]:
        if not visited[v]:
            parent[v] = source
            dfs(graph, v, visited, parent, time_visit, time, low)
            low[source] = min(low[source], low[v])
        elif parent[source] != v:
            low[source] = min(low[source], time_visit[v])
