import sys
import random
from funkcije import *
from zadatak9 import *
from zadatak10 import *

def numbers_counter(x):
    #sabrati od 1 dok zbir ne predje x, ispisati konacan rezultat i
    #poslednji sabran broj
    pom = 0
    zbir = 0
    while zbir <= x:
        pom += 1
        zbir += pom


    print("Izlaz: Zbir iznosi ", zbir, ", a poslednji sabran broj je ", pom)

def factoriel(x):
    #f-ja racuna faktorijel unetog broja sa tastature
    fact = 1
    for i in range(1, x+1):
        fact = fact * i

    print("Faktorijel broja ", x, " je: ", fact)

def prosecna_temperatura(recnik):
    #f-ja racuna prosecnu temperaturu za "n" dana iz recnika
    pomocna = 0.0
    for it in recnik:
        pomocna += recnik[it]

    return pomocna / len(recnik)

def zamisljen_broj(zamisljen, unesen, i):
    #f-ja poredi zamisljen i unesen broj
    if(zamisljen == unesen):
        print("Bravo, pogodili ste iz " + str(i) + ". pokusaja.")
        return 0
    elif(unesen < zamisljen):
        print("Pokusajte sa vecim brojem.")
        return 1
    else:
        print("Pokusajte sa manjim brojem.")
        return 1


def foo(key, value):

    #d = {key: value}
    d = {}
    d[key] = value

    del value[0]

    for it in d:
        print("key: ", it)
        print("value: ", d[it])

    print("List(d): ", list(d))

if __name__ == "__main__":
    pkm()

"""
    if len(sys.argv) < 2:
        print("Problem with command line arguments!")
    else:
        key = sys.argv[1]

        l = []
        for i in range(1, 10, 2):
            l.append((i, i+1))

        print("List before deep copy: ")
        for it in l:
            print(it)

        foo(key, l[:])

        print("List after deep copy: ")
        for it in l:
            print(it)

        key2 = "torke"
        a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        foo(key2, a)

        print("################################")

        recnik = {}
        recnik["key1"] = l
        recnik["key2"] = a

        for it in recnik:
            print("key: ", it)
            print("value: ", recnik[it])

        print("List of keys: ", list(recnik))

        print("############### PRVI ZADATAK ###################")
        x = int(input("Krajnji zbir: "))
        numbers_counter(x)


        print("############### DRUGI ZADATAK #################")
        x = int(input("Unesite broj ciji faktorijel zelite izracunati: "))
        factoriel(x)


        print("############## TRECI ZADATAK ##################")
        rjecnik = {}
        i = 0
        while True:
            try:
                ulaz = int(input("Temperatura za "+ str(i+1)+ ". dan:"))
                i += 1
                rjecnik[i] = ulaz

            except ValueError:
                print("Prosecna temperatura iznosi ", round(prosecna_temperatura(rjecnik), 2), " stepeni.")
                print("Recnik: ", rjecnik)

                break



        print("########### CETVRTI ZADATAK ######################")

        x = random.randrange(0, 101) #mozda je bolje randint()
        print("Program je zamislio jedan broj. Pokusajte da ga pogodite!")
        i = 0
        while True:
            try:
                ulaz = int(input("Unesite Vas broj:"))
                i += 1
                if(ulaz == x):
                    print("Bravo, pogodili ste iz " + str(i) + ". pokusaja.")
                    break
                elif(ulaz < x):
                    print("Probajte sa vecim brojem.")
                else:
                    print("Probajte sa manjim brojem")

            except ValueError:
                print("Greska!")
                break



        print("############### CETVRTI ZADATAK - elegantnije resenje ##############")
        x = random.randrange(0, 101)   #randint
        print("Program je zamislio broj, Pogadjajte!")
        #print(x)
        i = 0
        while True:
            try:
                ulaz = int(input("Unesite Vas broj:"))
                i += 1
                if(zamisljen_broj(x, ulaz, i) == 0):
                    break
            except ValueError:
                print("Greska!")
                break


        print("############### PETI ZADATAK ####################")
        tacni = 0
        netacni = 0
        while True:
            try:
                x1 = random.randint(10, 100)
                x2 = random.randint(10, 100)
                ulaz = int(input(str(x1) + " + " + str(x2) + "= "))
                if ((x1 + x2) == ulaz):
                    print("Tacno!")
                    tacni += 1
                else:
                    print("Netacno!")
                    netacni += 1
                                                                        #round(a,b) -> zaokruzi broj a, na b decimala !!!
            except ValueError:
                print("Tacno ste odgovorili na ", tacni, " pitanja, a pogresno na ", netacni, " pitanja. Procenat uspesnosti iznosi ", round(tacni * 100/(tacni+netacni),2), "%.")
                break

        print("\n######################### SESTI ZADATAK ###########################")
        d = sys.argv[1]
        x = sys.argv[2]

        try:
            x = int(x)  #ako ovo prodje, uradi ostalo (ovo moze da baci gresku)
            d = int(d)  #ako ovo prodje, uradi ostalo (ovo moze da baci gresku)
            l = randomList(d)
            divs = divisibleBy(l, x)

            print("Duzina liste:", d)
            print("Broj X:", x)
            print("Izlaz: U listi: ", l, ", brojevi deljivi sa 3 su: ", divs)

        except ValueError: #ako nisu validne vrednosti ispisemo poruku
            print("Ulazni parametri nisu validni")

        print("################## SEDMI ZADATAK ##############")

        x = int(sys.argv[3])
        deliociX = delioci(x)
        print("Delioci broja X su: ", deliociX)

        print("################### OSMI ZADATAK ################")

        counter = 0
        while (ChooseNumbers() != True):
            counter += 1

        print("Bilo je potrebno ", counter, " biranja.")

        print("################## DEVETI ZADATAK #################")

        dict = {}
        unete_vrednosti = []
        while True:
            input_val = input("Unesite broj: ")
            unete_vrednosti.append(input_val)
            if input_val.isdigit():
                num = int(input_val)
            else:
                break

            sum = CalculateSum(num)
            isPrime = IsPrime(num)
            dict[num] = (sum, isPrime)

        print("Unete vrednosti: ", unete_vrednosti)
        print("\nIzlaz (zadatak9): ", dict)
"""
        #print("\n################## DESETI ZADATAK ##############")
        