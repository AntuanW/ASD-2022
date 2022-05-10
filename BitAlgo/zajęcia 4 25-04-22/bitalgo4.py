# todo
def zad_1(A):
    n = len(A)
    F = [[0 for _ in range(n)] for _ in range(n)]
    # F[i][j] - najwiekszy co do wartosci bezwzgl wynik tymczasowy na tablicy A[i, ..., j]
    # F[i][j] = max(sum(i, j), min(F[i][j-1], F[i-1][j])
    # F[i][i+1] = abs( A[i] + A[i+1])
    return 0


def zad_2():
    return 0


def zad_3(T):
    # Żab zbigniew
    # F[i][j] - min liczba skoków potrzebna by dotrzec na pole i i mieć w zapasie dokładnie j energii
    # (po zjedzeniu pola A[j])
    # F[i][j] = min( F[i-k][j + k - T[i]] | k £ [1, i]) + 1
    INF = float('inf')
    n = len(T)
    m = sum(T)
    F = [[None for _ in range(m)] for _ in range(n)]
    F[0][T[0]] = 0
    for i in range(1, n):
        for j in range(m):
            best = INF
            for k in range(1, i + 1):
                if j != 0:
                    if 1 <= j + k - T[i] < m and F[i - k][j + k - T[i]] is not None and j + k - T[i] >= k:
                        best = min(best, F[i - k][j + k - T[i]] + 1)
                else:
                    if 0 < k < m and T[i] == 0 and F[i - k][k] is not None and j + k - T[i] >= k:
                        best = min(best, F[i - k][k] + 1)
            if best != INF:
                F[i][j] = best

    return F


def zad_4():
    return 0


def zad_5():
    return 0


def zad_6():
    return 0


def zad_7():
    return 0


if __name__ == '__main__':

    test = [1, 1, 1, 1, 1]
    T = [2, 0, 3, 0, 0, 0]
    A = [1, 0, 2, 3, 4, 1]
    P = [2, 4, 3, 1]
    x = zad_3(P)
    # print(x)
    for i in range(len(x)): print(x[i])

    pass
