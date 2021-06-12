

class Histogram():

    def __init__(self, vrednost, frekvencija):
        self.vrednost =  vrednost
        self.frekvencija = frekvencija
        self.parent = None


class Node():
    def __init__(self, l, r, vrednost, frekvencija):
        self.left = l
        self.right = r
        self.vrednost = vrednost
        self.frekvencija = frekvencija

def GetHistogram(list):
    recnik = dict()
    l = []

    for el in list:
        if el in recnik:
            recnik[el] += 1
        else:
            recnik[el] = 1

    for d in recnik:
        ch = Histogram(d, recnik[d])
        l.append(ch)
    return l

def MinFrekvElem(l):
    min = l[0]

    for el in l:
        if el.frekvencija < min.frekvencija:
            min = el

    return min

def deleteElem(e, l):
    l.remove(e)

def addElem(e, l):
    l.append(e)

def GenerateElem(e1, e2):
    frekv = e1.frekvencija + e2.frekvencija
    vr = e1.vrednost + e2.vrednost

    n = Node(e1, e2, frekv, vr)
    e1.parent = n
    e2.parent = n

    return n

def encoder(e, l):
    enkodovano = ""
 #0 0 11 ---- e = f, l = ceo_histogram
    while e not in l:
        if e.parent.left == e:
            enkodovano += "0"
        else:
            enkodovano += "1"

        e = e.parent

    return enkodovano[::-1] #1100



if __name__ == "__main__":

    input1 = ['a', 'b']
    size = 0

    hist = GetHistogram(input1)
    temp = hist[:]

    for l in hist:
        print("Vrednost: ", l.vrednost, ", Frekvencija: ", l.frekvencija, sep='')
        size += l.frekvencija * 8

    while (len(hist)) > 1:
        e1 = MinFrekvElem(hist)
        deleteElem(e1, hist)
        e2 = MinFrekvElem(hist)
        deleteElem(e2, hist)
        hist.append(GenerateElem(e1, e2))

    d = dict()
    print("Char codes: ")
    huf_size = 0
    for h in temp:
        a = encoder(h, hist)
        d[h.vrednost] = a
        print("|", h.vrednost, "|", a, "|", sep="")
        huf_size += h.frekvencija * len(a)

    out = ""

    for c in input1:
        out += d[c]


    print("encoded input: ", out)
    print("Text size: ", size, "bits, Huffman size: ", huf_size, "bits", sep="")
    print("************************************")


