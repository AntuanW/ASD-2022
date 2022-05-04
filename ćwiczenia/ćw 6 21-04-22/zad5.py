def knapsack_2d(P, W, H, max_weight, max_height):
    n = len(P)
    # F[i][w][h] - maksymalny zysk z przedmiotow 0, ..., i nie prekraczajacych wagi w i wysokosci h
    # F[i][w][h] = max(f[i-1][w][h], f[i-1][w - W[i]][h - H[i])
    F = [[[0 for _ in range(max_height+1)] for _ in range(max_weight+1)] for _ in range(n)]
    for b in range(W[0], max_weight+1):
        for h in range(H[0], max_height+1):
            F[0][b][h] = P[0]
    for h in range(max_height+1):
        for b in range(max_weight+1):
            for i in range(1, n):
                F[i][b][h] = F[i-1][b][h]
                if b - W[i] >=0 and h - H[i] >=0:
                    F[i][b][h] = max(F[i][b][h], F[i-1][b - W[i]][h - H[i]] + P[i])
    return F[n-1][max_weight][max_height]
