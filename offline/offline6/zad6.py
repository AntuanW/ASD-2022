#Antoni Wójcik
"""
Algorytm bazuje na BFS. Na początku ustalam odległości z wierzchołka s do pozostałych oraz z t do pozostałych.
Następnie wybieram te wierzchołki, z których odległość do s + odległośc do t równa jest najkrótszej scieżce.
W wyniku tego otrzymam liste wszystkich wierzchołków leżących na najkrótszych ścieżkach. Następnie zliczam ilość wierzchołków
względem odległości od s(bądź t). Na koniec szukam takich odległości, które różnią się o 1 i obie reprezentowane są przy pomocy zbioru o mocy 1.
Gdy znajdę takie 2 wierzchołki, oznacza to, że znalazłem krawędź, której nie da się obejść, co za tym idzie usunięcie jej wydłuzy
najkrótsza scieżkę.
Złożoność: O(V + E)
"""

from zad6testy import runtests
from queue import Queue

def longer( G, s, t ):
    def BFS(G, s):
        n = len(G)
        Q = Queue()
        dist = [-1]*n
        dist[s] = 0
        Q.put(s)

        while not Q.empty():
            u = Q.get()
            for v in G[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    Q.put(v)
        return dist

    n = len(G)
    dist_s = BFS(G, s)
    dist_t = BFS(G, t)
    shortest_path = dist_s[t]
    vertex = [[] for _ in range(shortest_path+1)]

    for i in range(n):
        if dist_t[i] + dist_s[i] == shortest_path:
            vertex[dist_t[i]].append(i)

    for i in range(shortest_path):
        if len(vertex[i]) == 1 and len(vertex[i+1]) == 1:
            return (vertex[i][0], vertex[i+1][0])

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )
