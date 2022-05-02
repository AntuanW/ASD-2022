def find_missing(A):
    l = 0
    r = len(A) - 1
    while l < r:
        mid = (l + r)//2
        if A[mid] == mid:
            l = mid + 1
        else:
            r = mid
    if A[r] == r:
        return False
    else:
        return r


A = [0,1,2,4,5,6,7,9]
print(find_missing(A))