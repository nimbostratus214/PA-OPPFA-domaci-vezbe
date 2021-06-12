#Radenko Mihajlovic RA214/2018

class Histogram():
    def __init__(self, vrednost, frekvencija):
        self.vrednost = vrednost
        self.frekvencija = frekvencija
        self.parent = None

#cvor
class Node():
    def __init__(self, elem1, elem2, vrednost, frekvencija):
        self.left = elem1
        self.right = elem2
        self.vrednost = vrednost
        self.frekvencija = frekvencija

def GetHistogram(lista):
    d = dict()
    l = []

    for el in lista:
        if el in d:
            d[el] += 1
        else:
            d[el] = 1

    for el in d:
        pom = Histogram(el, d[el])
        l.append(pom)

    return l


def MinElement(l):
    min = l[0]

    for el in l:
        if el.frekvencija < min.frekvencija:
            min = el

    return min


def obrisiEl(el, lista):
    lista.remove(el)


def dodajEl(el, lista):
    lista.append(el)


def generateElement(elem1, elem2):
    frekvencija = elem1.frekvencija + elem2.frekvencija
    vrednost = elem1.vrednost + elem2.vrednost

    cvor = Node(elem1, elem2, vrednost, frekvencija)
    elem1.parent = cvor
    elem2.parent = cvor

    return cvor


def encode(el, lista):
    encoded = ""

    while el not in lista:
        if el.parent.left == el:
            encoded += "0"
        else:
            encoded += "1"
        el = el.parent

    return encoded[::-1]