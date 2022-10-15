#Antoni Wójcik
"""
Opis działania algorytmu:
Tworzę tablicę space, przechowującą obecny stan pojemności magazynów.
Mając informację, że pomieszczą cały węgiel, mozna wywnioskowac ze bedzie ich maksymalnie tyle co transportów.
Nastepnie, przechodząc po kolejnych transportach węgla,
szukam magazynu o najmniejszym numerze, który może pomieścić ładunek. Gdy go znajdę, zapamiętuje który to był magazyn.
Złożoność: O(n^2)
"""

from egz2atesty import runtests

def coal( A, T ):
    n = len(A)
    space = [T for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if space[j] >= A[i]:
                space[j] -= A[i]
                last_magazine = j
                break
    return last_magazine

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )
