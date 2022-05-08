def ad_1(T, L):

    n = len(T)
    curr = 0
    res = []
    while curr + L < n - 1:
        counter = L
        while not T[curr + counter] and counter >= 0:
            counter -= 1
        curr += counter
        res.append(curr)
    return res

def ad_2(T, L):
    """
    Patrzymy na każdą stacje w naszym zasięgu. Jezeli ktoras stacja ma tansze paliwo, tankujemy z obecnej tyle aby tam dojachac
    i jedziemy. Jezeli juz jestesmy na najtanszej stacji to tankujemy do pelna i jedziemy na nastepnej najtanszej.
    Calosc powtarzamy az dojedziemy do konca.
    """
    return 0
