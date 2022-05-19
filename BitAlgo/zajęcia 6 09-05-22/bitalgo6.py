from collections import deque


def zad1(G):
    n = len(G)
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            Q = deque()
            visited[i] = True
            Q.append((i, i))
            while len(Q) != 0:
                prev, curr = Q.popleft()
                for v in G[curr]:
                    if v != prev:
                        if visited[v]: return True
                        else:
                            visited[v] = True
                            Q.append((curr, v))
    return False


def zad2(A, n):
    G = [[] for _ in range(n)]
    for x in A:
        G[x[0]].append(x[1])
        G[x[1]].append(x[0])

    dist = [0]*n
    visited = [False]*n
    dist[0] = 1
    visited[0] = True
    Q = deque()
    Q.append(0)
    while len(Q) != 0:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                Q.append(v)

    maxi = max(dist)
    T = [0]*(maxi+1)
    for i in dist:
        T[i] += 1

    best = -1
    idx = -1
    for i in range(maxi+1):
        if T[i] > best:
            best = T[i]
            idx = i
    return idx, best


def zad3(M):
    # 0 - woda, 1- ląd
    n = len(M)
    ruchy = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    parent = [[None for _ in range(n)] for _ in range(n)]
    number_of_lakes = 0
    biggest_lakes = 0
    for i in range(n):
        for j in range(n):
            if M[i][j] == 0 and not visited[i][j]:
                number_of_lakes += 1
                curr_size = 1
                visited[i][j] = True
                Q = deque()
                Q.append((i, j))
                while len(Q) != 0:
                    row, col = Q.popleft()
                    for x in ruchy:
                        if n > row + x[0] >= 0 == M[row + x[0]][col + x[1]] and 0 <= col + x[1] < n and not visited[row + x[0]][col + x[1]]:
                            curr_size += 1
                            visited[row + x[0]][col + x[1]] = True
                            Q.append((row + x[0], col + x[1]))
                if curr_size > biggest_lakes:
                    biggest_lakes = curr_size

    Q = deque()
    Q.append((0, 0))
    visited[0][0] = True
    while len(Q) != 0:
        row, col = Q.popleft()
        for x in ruchy:
            if 0 <= row + x[0] < n and 0 <= col + x[1] < n and M[row + x[0]][col + x[1]] == 1 and not visited[row + x[0]][col + x[1]]:
                visited[row + x[0]][col + x[1]] = True
                parent[row + x[0]][col + x[1]] = (row, col)
                Q.append((row + x[0], col + x[1]))

    path = []
    curr = (n-1, n-1)
    if parent[n-1][n-1] is None: path = False
    else:
        while curr is not None:
            path.append(curr)
            curr = parent[curr[0]][curr[1]]
        path = path[::-1]

    return number_of_lakes, biggest_lakes, path


def zad4(A, a, b):
    """
    Tworzymy graf: każdy przedział jest wierzchołkiem, wierzchołki są połączone jeżeli mają 1 pkt wspólny.
    Następnie przeglądamy graf z wierzchołków będących przedziałami zaczynającymi się w a i sprawdzamy czy mozna dojść
    do któregokolwiek wierzchołka zakończonego na b.
    W celu zbicia złożoności można użyć słowników.
    """
    n = len(A)
    G = [[] for _ in range(n)]
    A.sort(key=lambda x: x[0])
    for i in range(n-1):
        j = i+1
        while j < n and A[j][0] <= A[i][1]:
            if A[j][0] == A[i][1]:
                G[i].append(j)
            j += 1

    Q = deque()
    visited = [False]*n
    parent = [None]*n
    i = 0
    while i < n and A[i][0] <= a:
        if A[i][0] == a:
            Q.append(i)
            visited[i] = True
        i += 1

    while len(Q) != 0:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                Q.append(v)

    res = []
    for i in range(n):
        if A[i][1] == b and visited[i]:
            curr = i
            while curr is not None:
                res.append(A[curr])
                curr = parent[curr]
            break

    if len(res) == 0:
        return False
    else:
        return res[::-1]


def zad5(A, pin, curr):
    Q = deque()
    G = [[] for _ in range(10000)]
    visited = [None]*10000
    visited[curr] = True
    parent = [None]*10000
    Q.append(curr)
    while len(Q) != 0:
        u = Q.popleft()
        for v in A:
            if u + v > 9999:
                if not visited[(u+v)%10000]:
                    visited[(u+v)%10000] = True
                    parent[(u+v)%10000] = u
                    Q.append((u+v)%10000)
            elif not visited[u+v]:
                visited[u+v] = True
                parent[u+v] = u
                Q.append(u+v)
            if visited[pin]:
                break

    if visited[pin]:
        res = []
        a = pin
        while a is not None:
            res.append(a)
            a = parent[a]
        return res[::-1]
    else:
        return None


def zad6(G, v):
    n = len(G)
    F = [0]*n
    def rek(u):
        nonlocal F
        if len(G[u]) == 0:
            return 1
        counter = 0
        for v in G[u]:
            counter += rek(v)
        F[u] = counter + 1
        return counter + 1

    rek(v)

    return F


def zad7(G, shops):
    n = len(G)
    Q = deque()
    visited = [False]*n
    dist = [0]*n
    for v in shops:
        Q.append(v)
        visited[v] = True

    while len(Q) != 0:
        u = Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                dist[v] = dist[u] + 1
                Q.append(v)

    return dist


def zad8(G, v):

    def BFS(v):
        Q = deque()
        visited = [False] * n
        dist = [0] * n
        Q.append(v)
        visited[v] = True

        while len(Q) != 0:
            u = Q.popleft()
            for v in G[u]:
                if not visited[v]:
                    visited[v] = True
                    dist[v] = dist[u] + 1
                    Q.append(v)
        return dist

    n = len(G)
    best = -1
    idx = -1
    dist = BFS(v)
    for i in range(n):
        if dist[i] > best:
            best = dist[i]
            idx = i

    dist = BFS(idx)
    return max(dist)


if __name__ == '__main__':

    pass