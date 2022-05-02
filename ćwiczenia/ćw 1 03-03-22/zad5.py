class Node:
    def __init__(self):
        self.next = None
        self.val = None


def tab2list( A ):
    H = Node()
    C = H
    for i in range(len(A)):
        X = Node()
        X.val = A[i]
        C.next = X
        C = X
    return H.next


def printlist( L ):
    while L != None:
        print( L.val, "->", end=" ")
        L = L.next
    print("|")


def invert(head):
    current = head
    prev = None
    while current != None:
        tmp = current
        current = current.next
        tmp.next = prev
        prev = tmp
    return prev
