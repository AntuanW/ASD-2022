def find_min_max(T):
    counter = 0
    n = len(T)
    for i in range(n//2):
        counter += 1
        if T[i] > T[n-1-i]:
            T[i], T[n-1-i] = T[n-1-i], T[i]
    if n % 2 != 0 and T[0] > T[n//2]:
        counter += 1
        T[0], T[n//2] = T[n//2], T[0]

    worst = float('inf')
    for i in range(n//2):
        counter += 1
        worst = min(worst, T[i])
    best = (-1)*float('inf')
    for i in range(n//2, n):
        counter += 1
        best = max(best, T[i])

    return worst, best, counter
