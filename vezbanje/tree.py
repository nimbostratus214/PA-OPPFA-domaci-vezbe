
class Tree:
    def __init__(self, root = None):
        #root je koren stabla
        self.root = root


class Node:
    def __init__(self, key, l = None, r = None, p = None):
        self.key = key
        self.l = l
        self.r = r
        self.p = p

    def __str__(self):
        return "{" + str(self.key) + "}"



def treeInsert(T, z):
    #T - stablo, z - cvor
    y = None
    x = T.root
    while x is not None:
        y = x
        if z.key < x.key:
            x = x.l
        else:
            x = x.r
    z.p = y
    if y is None:
        T.root = z
    elif z.key < y.key:
        y.l = z
    else:
        y.r = z

def inOrderTreeWalk(x):
    if x is not None:
        inOrderTreeWalk(x.l)
        print(x)
        inOrderTreeWalk(x.r)


def treeMin(x):
    while x.l is not None:
        x = x.l
    return x

def treeMax(x):
    while x.r is not None:
        x = x.r
    return x

def treeSuccessor(x):
    if x.r is not None:
        return treeMin(x.r)
    y = x.p
    while y is not None and x is y.r:
        x = y
        y = y.p
    return y

def treeSearch(x, k):
    if x is None or k == x.key:
        return x
    if k < x.key:
        return treeSearch(x.l, k)
    else:
        return treeSearch(x.r, k)

def transplant(T, u, v):
    if u.p == None:
        T.root = v
    elif u == u.p.l:
        u.p.l = v
    else:
        u.p.r = v

    if v is not None:
        v.p = u.p


def treeDelete(T, z): #treba proslediti cvor a ne vrednost !!!
    if z.l == None:
        transplant(T, z, z.r)
    elif z.r is None:
        transplant(T, z, z.l)
    else:
        y = treeMin(z.r)
        if y.p is not z:
            transplant(T, y, y.r)
            y.r = z.r
            y.r.p = y
        transplant(T,z,y)
        y.l = z.l
        y.l.p = y


def iterativeSearch(x, k):
    while x is not None and k != x.key:
        if k < x.key:
            x = x.l
        else:
            x = x.r
    return x