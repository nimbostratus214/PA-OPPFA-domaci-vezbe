from virus import *
from math import inf
from queue import Queue

#Comm je graf, s je pocetni cvor
def CalculateRisk(G, start):
    for u in G.humans:
        if u is not start:
            u.status = Infectivity.NotImmune
            u.risk = 0 #inf
            u.source = None

    start.status = Infectivity.Infected #status
    start.risk = 0
    start.source = None

    Q = Queue()
    Q.put(start)

    while not Q.empty():
        u = Q.get()
        for v in G.relations[u]:
            if v is not None:
                if v.status is Infectivity.NotImmune:
                    #check responsibility difference
                    if v.resp <= u.resp:
                        v.status = Infectivity.Infected
                        v.risk = u.resp - v.resp + 10 + u.risk #u.risk
                        v.source = u
                        Q.put(v)
                    else:
                        v.status = Infectivity.Immune #ne moze nikog zaraziti ako ovo vazi, zato je Immune
                        v.risk = v.risk
                        v.source = u
                        Q.put(v)

        u.status = Infectivity.Immune


#G - graf, s - pocetni cvor, v ciljni cvor- f-ja printa putanju od cvora do cvora
def printPath(G, start, end):
    if end is start:
        if start.source is None:
            print("Ime: " + str(start.name) + ", Rizik: " + str(end.risk) + ", Izvor zaraze nije poznat!") #funny
        else:
            print("Ime: " + str(start.name) + ", Rizik: " + str(end.risk) + ", Izvor zaraze: " + str(start.source.name))
    elif end.source is None:
        #print("No path from ", s.name, " to ", v.name, " exists.")
        print("Osoba " + str(end.name) + " se nece nikad zaraziti od osobe " + str(start.name))
    else:
        printPath(G, start, end.source)
        #print("Ime: " + str(v.name) + ": Rizik: " + str(v.risk) + " Status: " + str(v.status) + " Odgovornost: " + str(v.resp) + " Izvor zaraze: " + str(v.source.name))
        print("Ime: " + str(end.name) + ", Rizik: " + str(end.risk) + ", Izvor zaraze: " + str(end.source.name))

def printMatrix(G):
    print("--------------------------------------------------------------------------------------")
    outStr = "         "
    for el in G.humans:
        outStr = outStr + el.name + " | "
    print(outStr)

    for start in G.humans:
        #start = G.humans[1]
        outString = ""
        pom1 = ""
        pom2 = ""
        CalculateRisk(G, start)
        pom1 = str(start.name)
        while len(pom1) < 10:
            pom1 = pom1 + " "

        for el in G.humans:
            if el is start:
                pom2 = pom2 + "|  X    "
            else:
                pom3 = "|  " + str(el.risk) + "   "
                while len(pom3) < 8:
                    pom3 = pom3 + " "

                pom2 = pom2 + pom3

        print(pom1 + pom2 + "|")