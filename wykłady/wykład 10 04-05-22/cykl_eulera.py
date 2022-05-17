def czy_posiada_Eulera(G):
    # graf nieskierowany
    for i in G:
        if len(i) % 2 == 1:
            return False
    return True


def find_Euler_cycle(G):

    def dfs(prev, dest):
        nonlocal visited, G, cycle
        visited[prev][dest] = True
        visited[dest][prev] = True
        for v in G[dest]:
            if not visited[dest][v]:
                dfs(dest, v)
        cycle.append(dest)

    n = len(G)
    visited = [[False for _ in range(n)] for _ in range(n)]
    cycle = []

    for v in G[0]:
        if not visited[0][v]:
            dfs(0, v)
    cycle.append(0)
    return cycle


G = [
    [1, 2],
    [0, 2, 3, 5],
    [0, 1, 3, 5],
    [1, 2, 4, 5],
    [3, 5],
    [1, 2, 3, 4],
]

x = find_Euler_cycle(G)
for i in range(len(x)):
    print(chr(x[i]+ ord("A")), end=" -> ")