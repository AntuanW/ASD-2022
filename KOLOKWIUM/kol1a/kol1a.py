#Antoni Wójcik

"""
Algorytm grupuje wyrazy względem ich dlugosci, naspepnie szuka sil kazdego wyrazu wsrod wyrazow majacych taka sama sile. Zmienna global_best zwraca liczbe najsilniejszego wyrazu
"""
from kol1atesty import runtests

def g(T):
    def reverseable(w1, w2, n):
        w3 = w2[::-1]
        if w1 == w2: return True
        for i in range(n):
            if w1[i] != w3[i]:
                return False
        return True

    best = 0
    for i in T:
        if len(i) > best:
            best = len(i)
    C = [[] for _ in range(best)]
    for i in T:
        C[len(i) - 1].append([i, 0])

    global_best = 0
    for i in range(best):
        if len(C[i]) > 2:
            for j in range(len(C[i]) - 1):
                for k in range(j+1, len(C[i])):
                    if reverseable(C[i][j][0], C[i][k][0], i):
                        C[i][j][1] += 1
                        C[i][k][1] += 1
            for j in range(len(C[i])):
                global_best = max(global_best, C[i][j][1])


    return global_best +1


#Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=False )
