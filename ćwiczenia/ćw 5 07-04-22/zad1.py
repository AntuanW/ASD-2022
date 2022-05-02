# Ciągly problem plecakowy
def knapsack(V, P, B):
    n = len(V)
    ratio = [(None, None)] * n
    for i in range(n):
        ratio[i] = (P[i] / V[i], i)

    ratio.sort(key=lambda x: x[0], reverse=True)

    result = []
    i = 0
    current = B
    while current > 0 and i < n:
        if V[ratio[i][1]] < current:
            result.append((ratio[i][1], V[ratio[i][1]]))
            current -= V[ratio[i][1]]
        else:
            result.append((ratio[i][1], current))
            current = 0
        i += 1
    return ratio, result
