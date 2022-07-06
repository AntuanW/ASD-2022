from zad1testy import runtests


def chaos_index( T ):
    for i in range(len(T)):
        T[i] = (T[i], i)
    T.sort(key = lambda x: x[0])
    k = 0
    for i in range(len(T)):
        if abs(i - T[i][1]) > k:
            k = abs(i - T[i][1])
    return k


runtests( chaos_index )
