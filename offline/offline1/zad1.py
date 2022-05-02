#Antoni Wójcik
"""
Algorytm opiera się na strukturze kopca minimum wielkości k. Przechowywane są w nim elementy w odległości k w posortowanej liście.
Następnie z kopca ściągane jest minimum i doklejane na koniec listy wynikowej. Dzięki kopcu,
dostęp do lokalnego minimum odbywa się w czasie O(1), a przywrócenie własności kopca nastepuje w czasie O(log k).
Alorytm posiada złożoność czasową O(n*log k), w szczególności dla:
k = O(1) -> O(n)
k = O(log n) -> O(n*log log n)
k = O(n) -> O(n* log n)
"""

from zad1testy import Node, runtests


def SortH(p,k):

    def left(i): return 2*i + 1
    def right(i): return 2*i + 2
    def parent(i): return (i - 1)//2

    def heapify(A, n, i):
        l = left(i)
        r = right(i)
        min_ind = i
        if l < n and A[l].val < A[min_ind].val:
            min_ind = l
        if r < n and A[r].val < A[min_ind].val:
            min_ind = r
        if min_ind != i:
            A[i], A[min_ind] = A[min_ind], A[i]
            heapify(A, n, min_ind)

    def build_heap(A):
        n = len(A)
        for i in range(parent(n-1), -1, -1):
            heapify(A, n, i)

    def how_big_heap(p, k):
        l = p
        counter = 0
        while l is not None:
            counter += 1
            l = l.next
            if counter > k:
                return k + 1
        return counter

    if k == 0:
        return p

    heap_size = how_big_heap(p, k)
    H = [None]*heap_size
    for i in range(heap_size):
        H[i] = p
        p = p.next
        H[i].next = None
    build_heap(H)

    result_node = Node()
    current_node = result_node

    while p is not None:
        current_node.next = H[0]
        current_node = current_node.next
        H[0] = p
        p = p.next
        H[0].next = None
        heapify(H, heap_size, 0)

    for i in range(heap_size-1, 0, -1):
        current_node.next = H[0]
        current_node = current_node.next
        H[0], H[i] = H[i], H[0]
        heapify(H, i, 0)
    current_node.next = H[0]

    return result_node.next


runtests( SortH ) 

