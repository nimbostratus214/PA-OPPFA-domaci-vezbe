from vortex import *
from funs import *

if __name__ == "__main__":

    undershorts = Vortex(n="undershorts")
    socks = Vortex(n="socks")
    watch = Vortex(n="watch")
    pants = Vortex(n="pants")
    shoes = Vortex(n="shoes")
    shirt = Vortex(n="shirt")
    belt = Vortex(n="belt")
    tie = Vortex(n="tie")
    jacket = Vortex(n="jacket")

    undershorts.connection = [pants, shoes]
    socks.connection = [shoes]
    watch.connection = []
    pants.connection = [belt, shoes]
    shoes.connection = []
    shirt.connection = [tie, belt]
    belt.connection = [jacket]
    tie.connection = [jacket]
    jacket.connection = []

    G = [shirt, tie, jacket, belt, watch, undershorts, pants, shoes, socks]
    L = topological_sort(G)
    for l in reversed(L):
        print(l.name + "(" + str(l.data) + "/" + str(l.time) + ")")