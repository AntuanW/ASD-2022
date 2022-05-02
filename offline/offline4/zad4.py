#Antoni Wójcik
"""
Algorytm zaczyna od posortowania budynkow wzgledem ich koncow.
Nastepnie wykorzystywane sa pomocnicze funkcje:
prev(i) = pierwszy budynek z lewej strony budynku i nienachodzacy na niego (koszt obliczenia O(n^2))
students(i) = liczba studentow mogaca zamieszkac w budnku i (O(1))
cost(i) = koszt budynku i (O(1))

Algorytm dynamiczny przypomina problem plecakowy i bazuje na funkcji:
f(i, p) - max liczba studentow mogaca zamieszkac w budynkach 0, ... i, ktore na siebie nie nachodza i nie przekraczaja kosztu p
zaleznosc rekurencyjna:
f(i, p) = max(f(i-1, p), students(i) + f(prev(i), p - cost(i)))
Zlozonosc czasowa:
O(n^2 + np)
Zlozonosc pamieciowa:
O(np)
"""
from zad4testy import runtests

def select_buildings(T, p):

    def students(i, T): return (T[i][2]-T[i][1])*T[i][0]
    def cost(i, T): return T[i][3]

    n = len(T)
    G = [None]*n
    for i in range(n):
        G[i] = (T[i][0], T[i][1], T[i][2], T[i][3], i)
    G.sort(key= lambda x: x[2])
    prev = [None]*n
    for i in range(n):
        j = i
        while j >= 0:
            if G[j][2] < G[i][1]:
                prev[i] = j
                break
            j -= 1

    F = [[0 for _ in range(p + 1)] for _ in range(n)]
    P = [[None for _ in range(p + 1)] for _ in range(n)]
    for b in range(cost(0, G), p + 1):
        F[0][b] = students(0, G)
        P[0][b] = (0, 0, 0)
    for b in range(p+1):
        for i in range(1,n):
            F[i][b] = F[i-1][b]
            P[i][b] = P[i-1][b]
            if b - cost(i, G) >=0:
                if prev[i] is not None:
                    if F[prev[i]][b - cost(i, G)] + students(i, G) >= F[i][b]:
                        F[i][b] = F[prev[i]][b - cost(i, G)] + students(i, G)
                        P[i][b] = (prev[i], b - cost(i, G), i)
                else:
                    if students(i, G) >= F[i][b]:
                        F[i][b] = students(i, G)
                        P[i][b] = (0, 0, i)
    res = []
    current = P[n-1][p]
    while current is not None:
        res.append(G[current[2]][4])
        current = P[current[0]][current[1]]
    return res

runtests( select_buildings )