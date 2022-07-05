"""
F[T] - min liczba klocków które należy ukraść aby ułożyć wieżę o wysokości >= T
Wartościami T są kolejne poziomy każdej klockowej wieży + 1.
Aby obliczyć F[T], należy najpierw brać z każdej wieży największe klocki tak aby każda z nich była wysokości < T.
Jeżeli uzyskana w ten sposób wieża nadal będzie za niska, kradniemy maksimum globalne z klocków tak długo aż nasza wieża spełni warunek.
Rozwiązaniem zadania jest minimum po wszystkich wartościach T.
"""
def build_tower(T):
    summary = []
    for i in range(len(T)):
        T[i].sort()
        summary.append(sum(T[i]))
    count = tower_height = 0
    while tower_height < max(summary):
        index = summary.index(max(summary))
        height = T[index].pop()
        tower_height += height
        summary[index] -= height
        count += 1
    return count