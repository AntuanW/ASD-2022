#todo

"""
f(v) - maksymalna ścieżka wychodząca z węzła v.
C[v] - wartośc wierzchołka v
k[v] - dzieci wierzchołka v
f(v) - max(f(k) + C[v] | k £ C[v])
Po obliczeniu funkcji f dla kazdego wierzcholka przechodze po calym drzewie i sprawdzam parami wiecholki majace wspolnego rodzica.
Szukam najlepszej sciezki o wartosci best
best = max(best, f(a) + f(b) - C[i], f(a), f(b)), gdzie a, b - para wierzcholkow wychodzaca z węzła
"""