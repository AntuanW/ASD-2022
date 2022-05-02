def zad1(A, B):
    def binary_search(T, elem):
        left = 0
        right = len(T) - 1

        while left <= right:
            ind = (left + right) // 2
            if T[ind] < elem:
                left = ind + 1
            elif T[ind] > elem:
                right = ind - 1
            else:
                return ind

        return None

    m = len(A)
    n = len(B)
    A.sort()
    for x in B:
        if binary_search(A, x) != None:
            return False
    return True


def zad2(A):
    n = len(A)
    A.sort()
    res = []
    for i in range(n // 2):
        res.append((A[i], A[n - 1 - i]))
    return res


def zad3(A, x, k):
    cnt = 0

    def zad3_rec(A, k, x, ind):
        nonlocal cnt

        if A[ind] <= x:
            cnt += 1
            if cnt == k:
                return True

            return zad3_rec(A, k, x, 2 * ind + 1) or zad3_rec(A, k, x, 2 * ind + 2)

        return False

    return zad3_rec(A, k, x, 0)


def zad4(A, x):
    def find_id(A, x):
        ind = 1
        while A[ind] is not None and A[ind] <= x:
            ind *= 2
        return ind

    left = 0
    right = find_id(A, x)

    while left <= right:
        ind = (left + right) // 2

        if A[ind] is None or A[ind] > x:
            right = ind - 1

        elif A[ind] < x:
            left = ind + 1

        else:
            return ind

    return -1


def zad5(A):
    n = len(A)
    l = 0
    r = n - 1
    while l <= r:
        ind = (l + r) // 2
        if A[ind] > ind:
            r = ind - 1
        elif A[ind] < ind:
            l = ind + 1
        else:
            return ind
    return -1


def zad6(A):
    def partition(arr, low, high):
        x = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= x:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[high], arr[i + 1] = arr[i + 1], arr[high]
        return i + 1

    def quickselect(A, low, high, k):
        if low == high: return A[low]
        if low < high:
            q = partition(A, low, high)
            if q == k:
                return A[q]
            elif q < k:
                return quickselect(A, q + 1, high, k)
            else:
                return quickselect(A, low, q - 1, k)

    if len(A) % 2 == 0:
        x = quickselect(A, 0, len(A) - 1, len(A) // 2)
        y = quickselect(A, 0, len(A) - 1, len(A) // 2 + 1)
        minimum = min(A)
        maximum = max(A)
        if abs(maximum - x) < abs(y - minimum):
            return x
        else:
            return y

    else:
        return quickselect(A, 0, len(A) - 1, len(A) // 2)


def zad7(A, B, C):
    A.sort()
    a = len(A)
    B.sort()
    b = len(B)
    for x in C:
        i = 0  # A
        j = b - 1  # B
        while i < a and j >= 0:
            if A[i] + B[j] < x:
                i += 1
            elif A[i] + B[j] > x:
                j -= 1
            else:
                return (A[i], B[j], x)
    return False


def zad8(A, k):
    def bin_search(A, l, p, x):
        left = l
        right = p
        while left <= right:
            ind = (left + right) // 2
            if A[ind] > x:
                right = ind - 1
            elif A[ind] < x:
                left = ind + 1
            else:
                return ind
        return False

    A.sort()
    B = []
    B.append(A[0])
    for i in range(1, len(A)):
        if A[i] != A[i - 1]:
            B.append(A[i])
    counter = 0
    for i in range(len(B) - 1):
        if bin_search(B, i, len(B) - 1, A[i] + k) != False:
            counter += 1

    return counter


def zad9(T):
    def pretty(x):
        C = [0] * 10
        if x == 0:
            C[0] = 1
            return C
        num = x
        while num != 0:
            digit = num % 10
            C[digit] += 1
            num //= 10

        jedno = wielo = 0
        for i in range(10):
            if C[i] == 1:
                jedno += 1
            elif C[i] > 1:
                wielo += 1

        return (x, jedno, wielo)

    def count_sort(A, indeks, parameter):
        # True -> rosnąco, False -> malejąco
        n = len(A)
        C = [0] * 10
        B = [0] * n
        for x in A:
            C[x[indeks]] += 1

        if parameter:
            for i in range(1, 10):
                C[i] = C[i] + C[i - 1]
            for i in range(n - 1, -1, -1):
                B[C[A[i][indeks]] - 1] = A[i]
                C[A[i][indeks]] -= 1
        else:
            for i in range(8, -1, -1):
                C[i] = C[i] + C[i + 1]
            for i in range(n - 1, -1, -1):
                B[C[A[i][indeks]] - 1] = A[i]
                C[A[i][indeks]] -= 1

        for i in range(n):
            A[i] = B[i]

    n = len(T)
    for i in range(n):
        T[i] = pretty(T[i])

    count_sort(T, 2, True)
    count_sort(T, 1, False)

    for i in range(n):
        T[i] = T[i][0]

    return T


if __name__ == '__main__':

    pass