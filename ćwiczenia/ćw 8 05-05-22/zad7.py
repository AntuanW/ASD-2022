from queue import PriorityQueue
from math import inf


def kings_path(T):
    queue = PriorityQueue()
    queue.put((T[0][0], 0, 0))
    visited = [[False] * len(T) for _ in range(len(T))]
    visited[0][0] = True
    cost = [[inf] * len(T) for _ in range(len(T))]
    cost[0][0] = T[0][0]
    while not queue.empty():
        dist, row, col = queue.get()
        visited[row][col] = True
        new_row = [row + 1, row + 1, row, row - 1, row - 1, row - 1, row, row + 1]
        new_col = [col, col + 1, col + 1, col + 1, col, col - 1, col - 1, col - 1]
        for i in range(len(new_row)):
            if len(T) > new_row[i] >= 0 and len(T) > new_col[i] >= 0:
                if not visited[new_row[i]][new_col[i]]:
                    if cost[new_row[i]][new_col[i]] > cost[row][col] + T[new_row[i]][new_col[i]]:
                        cost[new_row[i]][new_col[i]] = cost[row][col] + T[new_row[i]][new_col[i]]
                        queue.put((T[new_row[i]][new_col[i]], new_row[i], new_col[i]))
    return cost[-1][-1]
