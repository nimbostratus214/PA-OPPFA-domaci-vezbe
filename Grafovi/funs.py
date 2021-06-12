from vortex import *
from queue import *
import math


def print_n(V):
    print("Susedi cvora " + V.name + ": ", end='')
    for c in V.connection:
        print(c.name, end=' ')

    print(" ")


def print_n_of_n(V):
    print_n(V)
    print("Susedi suseda")
    for c in V.connection:
        print_n(c)


def print_path(G, s, d):
    if d == s:
        print(s.name, end=" ")
    elif d.parent == None:
        print("No path from " + s.name + " to " + d.name + " exist")
    else:
        print_path(G, s, d.parent)
        print(d.name, end=" ")


def bfs_script(G, source, destination):
    bfs(G, source)
    print("Path from " + source.name + " to " + destination.name + ": ", end="")
    print_path(G, source, destination)


def dfs_script(G, source, destination):
    dfs(G)
    print("Path from " + source.name + " to " + destination.name + ": ", end="")
    print_path(G, source, destination)


def bfs(G, s):
    for v in G:
        v.color = VortexColor.WHITE
        v.data = math.inf
        v.parent = None

    s.color = VortexColor.GRAY
    s.data = 0
    s.parent = None

    Q = Queue()
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for c in u.connection:
            if c.color == VortexColor.WHITE:
                c.color = VortexColor.GRAY
                c.data = u.data + 1
                c.parent = u
                Q.put(c)

        u.color = VortexColor.BLACK


def dfs_visit(G, u, L):
    global time
    time = time + 1
    u.data = time
    u.color = VortexColor.GRAY

    for conn in u.connection:
        if conn.color == VortexColor.WHITE:
            conn.parent = u
            dfs_visit(G, conn, L)

    u.color = VortexColor.BLACK
    time = time + 1
    u.time = time
    L.append(u)


def dfs(G):
    L = []
    global time
    for v in G:
        v.color = VortexColor.WHITE
        v.parent = None

    time = 0

    for v2 in G:
        if v2.color == VortexColor.WHITE:
            dfs_visit(G, v2, L)

    return L


def topological_sort(G):
    L = dfs(G)
    return L
