from random import randint #da ne pozivamo random.randint


def randomList(duzina):
    #vraca listu nasumicnih celih brojeva iz intervala [1,500]
    retList = []

    for i in range(duzina):
        el = randint(0,501)
        retList.append(el)   #alternativa retList += [el] ->konkatenacija listi

    return retList

def divisibleBy(lista, x):
    #iz liste vraca novu listu koja sadrzi brojeve deljive sa X
    retList = []
    #for i in range(len(lista)):
    #    if lista[i] % x == 0:
    #        retList.append(lista[i])
    # drugi nacin
    for el in lista:
        if el % x == 0:
            retList.append(el)
    return retList

def delioci(x):
    #vraca listu delioca broja X
    retList = []
    for i in range(1, x+1):
        if (x % i == 0):
            retList.append(i)

    return retList

def ChooseNumbers():
    x1 = randint(0, 100)
    x2 = randint(0, 100)
    x3 = randint(0, 100)

    if(x1 == x2 == x3):
        return True
    else:
        return False

