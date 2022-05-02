def tasks(A):
    A.sort(key = lambda x: x[1])
    res = []
    res.append(A[0])
    curr = 0
    for i in range(1, len(A)):
        if A[i][0] >= res[curr][1]:
            res.append(A[i])
            curr += 1
    return res

A = [(0,5), (1,4), (2,6), (1,8), (3,4), (4, 5), (4, 8), (7, 9), (6, 11), (1, 2), (3, 4),(5, 6), (7, 8)]
print(tasks(A))