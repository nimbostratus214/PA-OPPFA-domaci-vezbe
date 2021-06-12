from queue import LifoQueue


class Vertex:
    """
    Graph vertex: A graph vertex (node) with data
    """

    def __init__(self, c=None, p=None, n=None):
        """
        Vertex constructor
        @param c - color
        @param p - parent
        @param n - name
        """
        self.c = c
        self.p = p
        self.n = n

    def __str__(self):
        #old => return str(self.n)
        return "Cvor: " + str(self.n) + " Boja: " + str(self.c) #+ " Roditelj: " + str(self.p)


class Graph:
    def __init__(self, V=None, E=None):
        """
        Graph constructor
        @param V - list of vertexes
        @param E - list of edges
        """
        self.V = V
        self.E = E
        self.k = 4
        self.colors = ['RED', 'YELLOW', 'GREEN', 'BLUE']




def uproscavanjeGrafa(G):
    #ne valja ovo!!!!!!!!
    k = G.k
    stek = []
    while len(G.V) != 0:
        for u in G.V:
            if len(G.E[G.V.index(u)]) < k:
                #ako je manje od k treba jos proveriti da li je veci od ostalih
                for el in G.E:
                    if el is not G.E[G.V.index(u)]:
                        if len(el) < k and len(G.E[G.V.index(u)]) > len(el):
                            stek.append(u)
                            G.V.remove(u)
                            #kako ukloniti sve veze tog cvora?
                            break


    for el in stek:
        print(el)


if __name__ == "__main__":
    print("Main modul!\n")

    #cvorovi
    cvA = Vertex(n = "A")
    cvB = Vertex(n = "B")
    cvC = Vertex(n="C")
    cvD = Vertex(n="D")
    cvE = Vertex(n="E")
    cvF = Vertex(n="F")
    cvG = Vertex(n="G")

    V = [] #lista cvorova
    V.append(cvA)
    V.append(cvB)
    V.append(cvC)
    V.append(cvD)
    V.append(cvE)
    V.append(cvF)
    V.append(cvG)

    #for el in V:
    #    print(el)

    #lista veza (edges)
    E = []

    E.append([cvB, cvD, cvF]) #veze za A na indexu 0
    E.append([cvA, cvC, cvD, cvE]) #veze za B na indexu 1 itd...
    E.append([cvB, cvE]) #C
    E.append([cvA, cvB, cvE, cvF]) #D
    E.append([cvB, cvC, cvD, cvG]) #E
    E.append([cvA, cvD, cvG]) #F
    E.append([cvE, cvF]) #G

    G = Graph(V=V, E=E)

    #for el in G.V:
    #    print("GRAF: ",el)



    #simplify graph
    #queue je FIFO struktura
    #treba nam LifoQueue
    Q = LifoQueue()
    Q.put(G.V[0]) #A
    Q.put(G.V[1]) #B
    Q.put(G.V[3]) #D
    Q.put(G.V[4]) #E
    Q.put(G.V[6]) #G
    Q.put(G.V[5]) #F
    Q.put(G.V[2]) #C

    cvor = Q.get()
    cvor.c = G.colors[0] #C
    cvor = Q.get()
    cvor.c = G.colors[0] #F
    cvor = Q.get()
    cvor.c = G.colors[1] #G
    cvor = Q.get()
    cvor.c = G.colors[2] #E
    cvor = Q.get()
    cvor.c = G.colors[1] #D
    cvor = Q.get()
    cvor.c = G.colors[3] #B
    cvor = Q.get()
    cvor.c = G.colors[2] #A



    for el in G.E:
        for cvor in el:
            print("CVOR: ",cvor)
        print("NEXT")

    print("\nBoje cvorova:")

    for el in G.V:
        print(el)

    print("Uproscavanje: ")
    #uproscavanjeGrafa(G)

    lista = [1,2,3,4,5]
    lista.append(6)
    lista.pop(3) #po indexu brise
    lista.remove(1) #po vrednosti elementa

    #for el in lista:
        #print(el)