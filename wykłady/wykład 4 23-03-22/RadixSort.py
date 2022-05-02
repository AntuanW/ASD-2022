def counting_sort(A, index):#k = 25
    n = len(A)
    C = [0]*26
    B = [0]*n
    for x in A:
        C[ord(x[index]) - 97] += 1
    for i in range(1, 26):
        C[i] = C[i] + C[i-1]
    for i in range(n-1, -1, -1):
        B[ C[ord(A[i][index])-97] - 1 ] = A[i]
        C[ord(A[i][index])-97] -= 1
    for i in range(n):
        A[i] = B[i]


def radix_sort(A):
    k = len(A[0])
    for i in range(k-1, -1, -1):
        counting_sort(A, i)


arr = ['kot','tok', 'kot']
radix_sort(arr)
print(arr)
T = ['tok', 'kot', 'tok']
radix_sort(T)
print(T)