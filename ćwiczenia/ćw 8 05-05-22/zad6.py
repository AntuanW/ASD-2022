def dfs(edges, source, finish, visited, t, result, optimal):
    if source[1] == finish:
        result[0] = True
        return True
    for i in range(len(edges)):
        if edges[i][0] == source[1] and not visited[i]:
            if edges[i][2] > optimal:
                if optimal + t >= edges[i][2]:
                    idx = edges.index(source)
                    visited[idx] = True
                    dfs(edges, edges[i], finish, visited, t, result, optimal)
            elif edges[i][2] <= optimal:
                if optimal - t <= edges[i][2]:
                    idx = edges.index(source)
                    visited[idx] = True
                    dfs(edges, edges[i], finish, visited, t, result, optimal)


def safe_flight(graph, t, optimal):
    edges = []
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j][0] > i:
                edges.append((i, graph[i][j][0], graph[i][j][1]))
    source = (0, graph[0][0][0])
    finish = graph.index(graph[-1])
    visited = [False] * len(edges)
    possible_edges = []
    for i in range(len(edges)):
        if edges[i][0] == source[0]:
            if edges[i][2] > optimal:
                if optimal + t >= edges[i][2]:
                    possible_edges.append(edges[i])
            elif edges[i][2] < optimal:
                if optimal - t <= edges[i][2]:
                    possible_edges.append(edges[i])
    result = [False]
    for i in range(len(possible_edges)):
        dfs(edges, possible_edges[i], finish, visited, t, result, optimal)
        if result[0]:
            return True
        for j in range(len(edges)):
            visited[j] = False
    return False