class Task:
    def __init__(self, profit, deadline, number):
        self.deadline = deadline
        self.profit = profit
        self.number = number


def zad2(T, start, finish):
    n = finish - start
    plan = [None] * n
    T.sort(key=lambda x: x.profit, reverse=True)

    for task in T:
        if task.deadline >= finish - 1:
            time = n - 1
        else:
            time = task.deadline - start - 1
        curr = time
        while plan[curr] is not None and curr >= 0:
            curr -= 1

        if curr >= 0:
            plan[curr] = task.number

    return plan


def convert(A):
    res = []
    for x in A:
        res.append(Task(x[0], x[1], x[2]))
    return res


A = [
    (4, 13, 0), (6, 13, 1), (9, 13, 2), (10, 13, 3),
    (2, 19, 4), (5, 13, 5), (8, 13, 6), (11, 13, 7),
    (1, 15, 8), (3, 10, 9), (1, 78, 10)
]
A = convert(A)
start = 8
finish = 16
print(zad2(A, start, finish))