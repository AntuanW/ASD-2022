#Antoni Wójcik
"""
Algorytm dynamiczny opierający sie na 2 funkcjach (przy założeniu, że na początku parkingi zostaną posortowane względem odległości od A):
F[i] - min koszt dodarcia do i-tego parkingu trasy przy założeniu, że gdzieś wcześniej skorzystliśmy z zasady nr 2 jazdy ciężarówki, oraz, ze odpoczywamy na C[i]
G[i] - min koszt dodarcia do i-tego parkingu przy założeniu, że jedziemy bez szaleństw i nie korzystaliśmy nigdy z zasady nr 2 oraz, że odpoczywamy na C[i]

Rozwiązanie: F[n-1]

rekurencyjny zapis:
G[i] =  min (G[i-k]) + C[i] ngdzie k to koszt parkingu oddalonego maksymalnie o T

F[i] = min( F[i-k] ) + C[i]), min( G[i-k]) + C[i])

Złożoność O(n^2)
"""

from kol2btesty import runtests

def min_cost( O, C, T, L ):

    INF = float('inf')
    n = len(O)
    P = [None]*n
    for i in range(n):
        P[i] = (O[i], C[i]) #(odl, koszt)
    P.append((L, 0))
    P.append((0, 0))
    P.sort(key=lambda x: x[0])
    n += 2

    G = [None]*n
    G[0] = 0
    for i in range(1, n):
        j = i-1
        best = INF
        while j >= 0 and P[i][0] - P[j][0] <= T:
            best = min(best, G[j])
            j -= 1
        G[i] = best + P[i][1]

    F = [None]*n
    F[0] = 0
    for i in range(1, n):
        best = INF
        j = i-1
        while j >= 0 and P[i][0] - P[j][0] <= 2*T:
            best = min(best, G[j])
            j -= 1
        j = i-1
        while j >= 0 and P[i][0] - P[j][0] <= T:
            best = min(best, F[j])
            j -= 1
        F[i] = best + P[i][1]

    return F[n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )