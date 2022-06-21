#todo

def fill(T, K):
    T.sort(reverse = True)
    i = 0
    n = len(T)
    curr = K
    res = []
    while i < n:
        if curr >= T[i]:
            res.append(T[i])
            curr -= T[i]
        i += 1
    return res
