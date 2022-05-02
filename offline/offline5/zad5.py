#Antoni Wójcik
"""
Algorytm zachłanny. Ustalam zasięg jak daleko mozna pojechać. Chcemy, aby zasięg był równy lub wiekszy od n-1.
Jeżeli tak nie jest, oznacza to konieczność postoju. Chcemy wybrać więc stację między polem 0 a obecnym zasięgiem, o największej sumie paliwa
(pojemność baku jest nielimitowana). Do tego celu używam kolejki priorytetowej, gdzie przechowuję ilości ropy oraz ich indeksy.
Po wybraniu odpowiedniej stacji zwiekszam zaasieg i dodaje do kolejki nowe pola.
Złożnoność O(n logn)
"""
from zad5testy import runtests
from queue import PriorityQueue

def plan(T):
    Q = PriorityQueue()
    how_far = T[0]
    prev_idx = 0
    res = [0]
    while how_far < len(T)-1:
        for i in range(prev_idx + 1, how_far+1):
            Q.put((-T[i], i))
        x = Q.get()
        res.append(x[1])
        prev_idx = how_far
        how_far += -x[0]
    return sorted(res)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )
