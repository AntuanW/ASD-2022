#todo
def zad_1(P):   #ciecie preta
    n = len(P)
    F = [0]*(n+1)
    parent = [None]*(n+1)
    #F[i] - max zysk z pociecia preta o dlugosci i
    #F[i] = max(F[i-a] + P[a-1] | 1 <= a <= i)
    for i in range(1, n+1):
        best = 0
        for a in range(1, i+1):
            if F[i-a] + P[a-1] > best:
                best = F[i-a] + P[a-1]
                parent[i] = i-a
        F[i] = best

    curr = parent[n]
    idx = n
    res = []
    while curr is not None:
        res.append(idx - curr)
        idx = curr
        curr = parent[idx]

    return res


def zad_3(A):   #schody amazona
    n = len(A)
    F = [0]*n   #F[i] - na ile sposobów mozna dojsc na pozycje i
    F[0] = 1
    for i in range(n):
        for j in range(1, A[i]+1):
            if i+j < n:
                F[i+j] += F[i]

    return F


def zad_4(T):

    def ruchy(i, j):
        nonlocal n, m
        moves = [(i, j-1), (i-1, j)]
        res = []
        for x in moves:
            if  0 <= x[0] < m and  0 <=x[1] < m:
                res.append(x)
        return res



    def rek(i, j):
        nonlocal F, n, m, INF
        if F[i][j] is not None: return F[i][j]
        best = INF
        for x in ruchy(i, j):
            best = min(best, rek(x[0], x[1]))
        F[i][j] = best + T[i][j]
        return F[i][j]


    INF = float('inf')
    m = len(T)
    n = len(T[0])
    F = [[None for _ in range(n)] for _ in range(m)]
    F[0][0] = T[0][0]
    for i in range(1, n):
        F[0][i] = F[0][i-1] + T[0][i]

    F[m-1][n-1] = rek(m-1, n-1)

    return F[m-1][n-1]


def zad_5():
    return 0


def zad_6(n):
    #f(n) = f(n-1) +  f(n-2)
    #f(0) = 1
    #f(1) = 2

    F = [0]*(n+1)
    F[0] = 1
    F[1] = 2
    for i in range(2, n+1):
        F[i] = F[i-1] + F[i-2]

    return F[n]


def zad_7(A):
    """
    f(i, j) - max wartosc mozliwa do uzyskania z A[i, ..., j] przy optymalnej grze
    f(i, j) = max( min( f(i+2, j) + A[i], f(i+1, j-1) + A[i]), min( f(i+1, j-1) + A[j], f(i, j-2) + A[j]))
                my z lewej przeciwnik tez, z lewo przeciwnik prawo  my prawo przeciwnik lewo, my prawo przeciwnik tez
    """
    return 0


def zad_8(word):

    def rek(i, j):
        nonlocal word, F
        if F[i][j] is not None: return F[i][j]
        else:
            F[i][j] = False
            if word[i] == word[j]:
                F[i][j] = False or rek(i+1, j-1)
        return F[i][j]

    n = len(word)
    F = [[None for _ in range(n)] for _ in range(n)]
    #F[i][j] - czy wyraz word[i, ..., j] jest palindromem
    for i in range(n):
        F[i][i] = True
    for i in range(n-1):
        if word[i] == word[i+1]:
            F[i][i+1] = True
        else:
            F[i][i+1] = False
    for i in range(n):
        for j in range(i+2, n):
            F[i][j] = rek(i, j)

    res = -1
    res_word = None
    for i in range(n):
        for j in range(i, n):
            if F[i][j] and j-i+1 > res:
                res = j-i+1
                res_word = word[i:j+1]


    return res, res_word


def zad_9():
    """
    Szukamy kandydatów na początek sciezki: wierzcholki z ktorych jedynie wychodza krawedzie.
    nastepnie obliczamuy f(v) = max(f(u)+1 | u £ G[v]) dla kazdego z kandydatow i wybieramy wartosc najdluzszej sciezki
    """
    return 0


if __name__ == '__main__':

    pass