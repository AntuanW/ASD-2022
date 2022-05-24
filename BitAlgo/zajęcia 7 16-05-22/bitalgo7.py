#todo
from collections import deque


def zad1():
    """
    Szukamy mostów, potem sprawdzamy kazdy most pod kątem ile troli odetnie od wioski krasnoludów.
    O(k(V+E)) - oddzielic mosty i sprwdzac
    O(V+E) - dla kazdego mostu zapamietac ile jest troli za nim i wybrac ten z max liczba
    """
    return 0


def zad2():
    """
    Jest to drzewo. Usuwamy poddrzewa nie zawierajace zadnego miasta bez paczki.
    Szukamy średnicy w grafie, będzie to rdzen naszej trasy.
    Nastepnie idac ta trasa dodajemy odleglosci tras kiedy musimy zejsc ze sciezki
    """
    return 0


def zad3():
    """
    Kazde miasto traktujemy jak przedluzenie krawedzi.
    Nowa reprezentacja grafu: Graf, w ktorym wierzcholkami są oazy.
    Jezeli miedzy oazami jest krawedz -> scalamy je w jedna oaze
    Nastepnie szukamy cyklu Eulera

    Algorytm:
    1) łaczenie oaz
    2) eliminacja mist -> staja sie krawedziemi
    3) Szukanie cyklu Eulera
    """
    return 0


def zad4():
    """
    Klocki są wierchołkami.
    Szukamy wierzchołków bez krawędzi wchodzących.
    O(V+E)
    """
    return 0


def zad5():
    return 0


if __name__ == "__main__":

    pass