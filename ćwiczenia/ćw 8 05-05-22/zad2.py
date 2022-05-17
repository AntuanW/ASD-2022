# uniwersalne ujście
# reprezentacja macierzowa
def ujscie(G):
    n = len(G)
    row = 0
    col = 0
    while row < n and col < n:
        if G[row][col] == 0:
            col += 1
        else:
            row += 1
    if col == n:
        candidate = row
    else:
        candidate = col

    for i in range(n):
        if i != candidate:
            if G[candidate][i] != 0:
                return False
            if G[i][candidate] != 1:
                return False
        else:
            if G[i][i] != 0:
                return False

    return candidate
