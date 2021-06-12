import sys


def mapiranje(str, list):
    dict = {}
    dict[str] = list

    del list[0]

    print("Recnik: ", dict)

def zbir_n(n):
    zbir = 0
    for i in range(n):
        zbir += i
    return zbir

def zbir2_n(n):
    zbir = 0
    for i in range(n+1):
        zbir += i**2
    #zbir += n**2 #ako stavimo range(n) moramo izracunati posebno za n nakon for petlje
    return zbir

def strings(s1, s2):
    return s1[0:3] + s1[0:3] + s2[-3:]

if __name__ == "__main__":
    """
    N = int(input("Unesite N: "))
    sum = zbir_n(N)
    print("zbir prvih", N, " brojeva: ", sum)
    """
    if len(sys.argv) < 2:
        print("Unesite N kao argument")
    else:
        sum = zbir2_n(int(sys.argv[1]))
        print("Zbir kvadrata prvih N brojeva: ", sum)

    s = input('Unesite dva stringa: ')
    s1, s2 = s.split(' ')
    print(strings(s1, s2))

    l = []
    for i in range(100): # [0, 99]
        l.append(i)

    print(l[::-1])

    #koriscenjem recnika izracunati broj ponavljanja reci
    #koje se nalaze u datoteci dict_test.txt

    file = open('dict_test.txt', 'r')
    d = {}
    for line in file:
        words = []
        words += line.split(' ') #lista reci za svaku liniju iz datoteke
        for word in words: #i za svaku rec proverimo da li postoji u recniku
            if word in d:
                d[word] += 1 #ako da uvecamo za jedan
            else:            #akko ne, dodamo je, kljuc je rec, a vrednost je broj ponavljanja
                d[word] = 1

    print(d)  #stampamo recnik
    file.close()  #zatvorimo fajl

    #program u listu smesta 4 torke formata (integer, float, string)
    #ispisuje ih, i onda brise prvu torku iz liste

    l = []
    l.append((1, 3.21, "prva"))
    l.append((2, 4.32, "druga"))
    l.append((3, 5.43, "treca"))
    l.append((4, 6.54, "cetvrta"))

    print("Pre brisanja: ", l)
    l.remove(l[0])
    print("Nakon brisanja prve: ", l)

    #isto kao zadatak iznad, samo umesto torke koristiti skup
    s = set()
    s.add((1, 3.21, "prva"))
    s.add((2, 4.32, "druga"))
    s.add((3, 5.43, "treca"))
    s.add((4, 6.54, "cetvrta"))

    print('Pre brisanja: ', s)
    s.pop()
    print("Posle brisanja: ", s)

    """
    list = []
    for i in range(10):
        list.append((i, i+1))

    print(list)
    mapiranje("string", list[:])

    print("Lista: ", list)

    a = complex(1,2)
    b = complex(1,2)
    print(a)
    print(b)

    if (a is b):
        print("True")
    elif (type(a) == type(b)):
        print("same type")
    else:
        print("not true")

    print("\n\n\n")

    a = "pera pepric"
    print(a[0:8:2])
    print(a[-1])
    print(a[::-1])
    
    """