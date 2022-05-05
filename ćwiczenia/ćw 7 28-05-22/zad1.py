def przedzialy(T):
    T.sort()
    curr = (0, 0)
    res = []
    for i in T:
        if i > curr[1]:
            res.append((i, i+1))
            curr = (i, i+1)
    return res
