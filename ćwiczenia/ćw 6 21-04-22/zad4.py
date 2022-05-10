def zaba(A):  # zaba ale dynamicznie
    n = len(A)
    """
    f(i, e) - minimalna liczba skoków do pozycji i-tej,
    aby pozostało nam e energii po dotarciu
    i zjedzeniu przekąski z pola i-tego

    f(i, e) = min{f(j, e - (j-i) - C[i])} + 1 | j£[0, ..., i-1]
    """
    sum_energy = sum(A)
    F = [[None for _ in range(sum_energy + 1)] for _ in range(n)]
    for i in range(sum_energy + 1):
        F[0][i] = float('inf')
    F[0][A[0]] = 0
    for i in range(1, n):
        for e in range(sum_energy + 1):
            best = float('inf')
            for j in range(i):
                if e - j + i - A[i] >= 0 and sum_energy >= e - j + i - A[i] >= A[j]:
                    best = min(best, F[j][e - j + i - A[i]])
            F[i][e] = best + 1

    return F


A = [1, 1, 1, 1, 1, 1, 1]
x = zaba(A)
for i in range(len(x)):
    print(x[i])
