def cykl_na_cztery(G):
    n = len(G)
    if n < 4:
        return False

    for i in range(n-1):
        for j in range(i+1, n):
            cycle = []
            for k in range(n):
                if G[i][k] == G[j][k] == 1:
                    cycle.append(k)
                if len(cycle) == 2:
                    return [i, cycle[0], j, cycle[1]]
    return False
