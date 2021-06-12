import sys

def sumOfN(n):

    retVal = 0
    for i in range(0, n+1):
        retVal += i

    return retVal

def sumaKvadrata(n):

    retVal = 0

    for i in range(0, n+1):
        retVal += (i * i)

    return retVal

def strings(prviString, drugiString):

    pomocniPrvi = prviString[0:3]
    pomocniDrugi = drugiString[len(drugiString) - 3:len(drugiString)]

    retVal = pomocniPrvi * 2 + pomocniDrugi

    return retVal

def obrnutaLista():
    l = []

    for i in range(0, 101):
        l.append(i)

    print(l[::-1])

def recnik():

    retVal = {}
    in_file = open("dict_test.txt", 'r')

    for line in in_file:
        reci = line.split()
        for rec in reci:
            if rec not in retVal:
                retVal[rec] = 1
            else:
                retVal[rec] += 1

    in_file.close()
    return retVal

def torka():
    prvaTorka = (8, 2.71, "Telefon")
    drugaTorka = (10, 9.81, "Sveska")
    trecaTorka = (29, 67.76, "Marker")
    cetvrtaTorka = (77, 77.77, "Racunar")

    l = []

    l.append(prvaTorka)
    l.append(drugaTorka)
    l.append(trecaTorka)
    l.append(cetvrtaTorka)

    print(l)

def skup():
    prviSkup = {8, 2.71, "Telefon"}
    drugiSkup = {10, 9.81, "Sveska"}
    treciSkup = {29, 67.76, "Marker"}
    cetvrtiSkup = {77, 77.77, "Racunar"}

    l = []

    l.append(prviSkup)
    l.append(drugiSkup)
    l.append(treciSkup)
    l.append(cetvrtiSkup)

    print(l)

if __name__ == "__main__":
    print("Zadaci za vezbu: ")

    print("Suma prva 4 broja: ", sumOfN(4))
    print("Suma prvih 7 brojeva: ", sumOfN(7))
    print("Suma prvih 15 brojeva:", sumOfN(15))

    print("Suma kvadrata prvih 5 brojeva: ", sumaKvadrata(int(sys.argv[1])) )

    print("Stringovi: ", strings("Radenko", "Mihajlovic"))

    obrnutaLista()

    print("\n\nRecnik: ")
    print(recnik())

    print("\n\nTorke:")
    torka()

    print("\n\nSkup:")
    skup()
