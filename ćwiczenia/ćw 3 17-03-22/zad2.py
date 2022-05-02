def insert_to_heap(H, x):
    def parent(i): return (i-1)//2

    H.append(x)
    curr = len(H)-1
    while curr != 0:
        if H[parent(curr)] < x:
            H[parent(curr)], H[curr] = H[curr], H[parent(curr)]
        else:
            break
        curr = parent(curr)
