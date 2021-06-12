import math
import random
import time


class Data:
    def __init__(self, key):
        self.key = key
        self.literal = str(key)

    def __str__(self):
        return str(self.key)


def randList(min, max, num):
    l = []
    for i in range(num):
        rand = random.randint(min, max)
        l.append(rand)
    return l

#pomocna f-ja
def h1(k, m):
    return k.key % m

#pomocna f-ja
def h2(k, m):
    return 1 + (k.key % (m - 1))

#linearna provera
# h(k, i) = (h'(k) + i) mod m
#h' = h1; k - vr. kljuca; m - br. mesta (slotova) za smestanje el., i - pokusaj provere (0, m-1)
def linProb(k, m, i):
    return (h1(k, m) + i) % m

#kvadratna provera
#h(k, i) (h'(k) + c1*i + c2 * i^2)mod m (c1,c2 - konstante
def quadProb(k, m, i):
    c1 = c2 = 1 / 2

    return (h1(k, m) + c1 * i + c2 * i * i) % m

#dvostruko hesiranje
# h(k, i) = (h1(k) + h2(k)) mod m (h1 i h2 - pomocne hash f-je
def doubleHash(k, m):
    return (h1(k, m) + h2(k, m)) % m

#pisanje u hash tabelu
def hashInsert(T, k, m):
    i = 0

    while (i != m):
        j = linProb(k, m, i)
        if T[j] == None or T[j] == "deleted":
            T[j] = k
            return j
        else:
            i += 1

    return -1

#pretraga
def hashSearch(T, k, m):
    i = 0

    while True:
        j = linProb(k, m, i)

        if T[j].key == k.key:
            return j

        i += 1

        if T[j] == None or i == m:
            return None


# brisanje
def hashDelete(T, k, m):
    j = hashSearch(T, k, m)

    T[j] = "deleted"


if __name__ == "__main__":

    for n in [10000, 50000, 100000]:
        L = randList(0, n * 2, n)

        for m in [n, n // 2, n // 4]:

            T = [None] * m

            startTime = time.perf_counter()
            print("\n")
            for l in L:
                k = Data(l)
                res = hashInsert(T, k, m)

                if res == -1:
                    print("Hash overflow")
                    break

            endTime = time.perf_counter() - startTime

            print("Time for table form(n=%d, m=%d):" % (n, m), endTime)

            r = random.randint(0, n)
            src = Data(L[r])
            print("Searching for %d" % (src.key))

            startTime = time.perf_counter()

            src_res = hashSearch(T, src, m)

            endTime = time.perf_counter() - startTime

            if src_res != None:
                print("Found! Took:", endTime)
            else:
                print("Not Found! Took:", endTime)

            # delete testing
            '''for t in T:
                print(t)

            hashDelete(T, src, m)
            for t in T:
                print(t)'''