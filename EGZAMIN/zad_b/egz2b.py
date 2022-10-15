#Antoni Wójcik
"""
Opis algorytmu:
Algorytm bazuje na funkcji F[i][j], odpowiadającej na pytanie, czy można wejść do jaskini i-tej mając ze sobą j sztabek.
Dzięki regule, że nie ma dróg powrotnych, funkcję F obliczać można "falami", tzn. najpierw wiersz 0, następnie 1 itd.
Gdy badamy dany wiersz, szukamy w nim wartości True funkcji F. Gdy taki znajdziemy, sprawdzamy gdzie możemy w tej sytuacji iść dalej,
oraz ile sztab nam zostanie, odpowiednio aktualizując wartości funkcji F dla dalszych wierszy i rzędów.
Złożoność: O(n^2)
"""

from egz2btesty import runtests

def magic( C ):
    n = len(C)
    F = [[False]*(10*n+1) for _ in range(n)]
    F[0][0] = True
    for i in range(n):
        for j in range(10*n+1):
            if F[i][j]:
                in_chest = C[i][0]
                for k in range(1, 4):
                    path = C[i][k]
                    if path[1] != -1:
                        if in_chest >= path[0] and in_chest - path[0] <= 10:
                            F[path[1]][j + in_chest - path[0]] = True
                        elif in_chest < path[0] and abs(in_chest - path[0]) <=j:
                            F[path[1]][j - abs(in_chest - path[0])] = True
    for i in range(10*n -1, -1, -1):
        if F[n-1][i]: return i
    return -1

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
