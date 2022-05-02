#Antoni Wójcik
"""
Algorytm opiera się na następującej zależności:
g(x) - liczba przedziałów kończących sie na pozycji x lub wcześniej
f(x) - liczba przedziałów zaczynających się wcześniej niż na pozycji x
Liczba przedziałów zawierających się w przedziale [a,b]: c = g(b) - f(a) -1
Dowód (uproszczony): Załóżmy, że dla przedziału [a,b] algorytm podał prawidłowy wynik c. Zastanówmy się, czy dołozenie nowego
przedziału [x,y] zwiększające odpowiednio g(b) lub f(a) sprawi, że wynik c wzrośnie prawidłowo o 1 lub 0.
Okazuje się, że dla każdego możliwego ułożenia x oraz y wynik algorytmu poprawnie rośnie o 1 lub wcale.
Wyjątkiem jest sytuacja, gdzie x < a oraz y > b. Jednak w takiej konfguracji [a,b] nie może i tak byc poprawnym rozwiązaniem,
ponieważ [a,b] zawiera się w [x,y]. Algorytm działa więc w sposób poprawny.
Złożnoność obliczeniowa: O(n) + sortowanie => O(n log n)
Złożoność pamięciowa: O(n)
"""


from zad2testy import runtests


def depth(L):
    def partition(A, p, r, index):

        pivot_index = p
        x = A[pivot_index][index]
        A[pivot_index], A[r] = A[r], A[pivot_index]
        i = p - 1
        for j in range(p, r):
            if A[j][index] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1

    def quick_sort(A, p, r, index):

        if p < r:
            q = partition(A, p, r, index)
            quick_sort(A, p, q - 1, index)
            quick_sort(A, q + 1, r, index)


    n = len(L)
    for i in range(n):
        L[i].append(i)

    result = [[None, None] for _ in range(n)]

    quick_sort(L, 0, n-1, 0)
    result[ L[0][2] ][1] = 0

    for i in range(1,n):
        if L[i][0] == L[i-1][0]:
            result[ L[i][2] ][1] = result[ L[i-1][2] ][1]
        else:
            result[ L[i][2] ][1] = i

    quick_sort(L, 0, n-1, 1)
    result[ L[n-1][2] ][0] = n

    for i in range(n-2, -1, -1):
        if L[i][1] == L[i+1][1]:
            result[ L[i][2] ][0] = result[ L[i+1][2] ][0]
        else:
            result[ L[i][2] ][0] = i + 1

    best = 0
    for i in range(n):
        best = max(best, result[i][0] - result[i][1] - 1)

    return best


runtests( depth ) 
