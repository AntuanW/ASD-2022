"""
f(v) - maksymalna ścieżka wychodząca z węzła v.
C[v] - wartośc wierzchołka v
k[v] - dzieci wierzchołka v
f(v) - max(f(k) + C[v] | k £ C[v])
Po obliczeniu funkcji f dla kazdego wierzcholka przechodze po calym drzewie i sprawdzam parami wiecholki majace wspolnego rodzica.
Szukam najlepszej sciezki o wartosci best
best = max(best, f(a) + f(b) - C[i], f(a), f(b)), gdzie a, b - para wierzcholkow wychodzaca z węzła
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.path = 0


def the_most_valuable_path(v):
    if v is None:
        return 0, 0
    left_node, left_path = the_most_valuable_path(v.left)
    right_node, right_path = the_most_valuable_path(v.right)
    v.path = max(0, v.value, v.value + left_node, v.value + right_node)
    best_path = max(v.path, left_path, right_path)
    return v.path, best_path
