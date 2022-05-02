def pojemniki(T, A):
    n = len(T)
    punkty = []
    for h1, h2 in T:
        punkty.append((h1, "p"))
        punkty.append((h2, "k"))

    punkty.sort(key=lambda x: x[0])

    curr_width = 1
    prev_height = punkty[0][0]
    filled = 0
    for i in range(1, 2 * n):

        A -= curr_width * (punkty[i][0] - prev_height)
        if A < 0:
            return filled
        prev_height = punkty[i][0]
        if punkty[i][1] == "p":
            curr_width += 1
        else:
            curr_width -= 1
            filled += 1

    return filled
