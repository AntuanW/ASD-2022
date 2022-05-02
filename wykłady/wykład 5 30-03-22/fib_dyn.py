def fib_dyn(n):
    F = [1]*n
    for i in range(2, n):
        F[i] = F[i-1] + F[i-2]
    return F[n-1], F
