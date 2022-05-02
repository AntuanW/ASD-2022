def sort(A, n):
    def base(x, n, index):
        if index == 1:
            return x // n
        else:
            return x % n

    def counting_sort(A, n, index):
        C = [0]*n
        B = [0]*n

        for x in range(n):
            C[ base(A[x], n, index) ] += 1
        for i in range(1, n):
            C[i] = C[i] + C[i-1]
        for i in range(n-1, -1, -1):
            B[ C[ base(A[i], n, index)] -1 ] = A[i]
            C[base(A[i], n, index)] -= 1
        for i in range(n):
            A[i] = B[i]

    for i in range(2):
        counting_sort(A, n, i)
