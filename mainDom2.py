from funkcije import *


if __name__ == "__main__":
    print("\nAutor: Radenko Mihajlovic RA214/2018, Datum: 28.05.2021")
    print("--- Drugi domaci zadatak iz predmeta PA ; Tema: Grafovi ---")

    print("\n-------------------GRAF ZAJEDNICE => ZADATAK 1. -------------\n")
    #napravili cvorove
    cv1 = Human(name = "Ivan", responsibility= 20)
    cv2 = Human(name = "Ana", responsibility=6)
    cv3 = Human(name="Milan", responsibility=35)
    cv4 = Human(name="Marija", responsibility=54)
    cv5 = Human(name="Diana", responsibility=70)
    cv6 = Human(name="Igor", responsibility=82)
    cv7 = Human(name="Teodora", responsibility=22)
    cv8 = Human(name="Nikola", responsibility=82)

    relations = {}

    relations[cv1] = [cv2, cv8] #Ivan -> Ana, Nikola
    relations[cv2] = [None]     #Ana -> None
    relations[cv3] = [cv2]      #Milan -> Ana
    relations[cv4] = [cv3]      #Marija -> Milan
    relations[cv5] = [cv4]      #Diana -> Marija
    relations[cv6] = [cv4, cv5] #Igor -> Marija, Diana
    relations[cv7] = [cv1, cv8] #Teodora -> Ivan, Nikola
    relations[cv8] = [None]     #Nikola -> None

    print("----------------------- RELATIONS CHECK --------------------")

    for el in relations:
        veza = str(el.name)
        for cv in relations[el]:
            if cv is not None:
                print(veza + " -> " + str(cv.name))
            else:
                print(veza + " -> " + "no connections")
        print("-------------------- NEXT NODE --------------------------")

    print(" *************************************************************\n")

    print(" --------------------------Hummans list check -----------------------------------")
    humans = []
    humans.append(cv1)
    humans.append(cv2)
    humans.append(cv3)
    humans.append(cv4)
    humans.append(cv5)
    humans.append(cv6)
    humans.append(cv7)
    humans.append(cv8)

    for el in humans:
        print(el)

    print(" ------------------------------Finished------------------------------------\n")


    print("__________________________ CREATE COMMUNITY _____________________________________")

    Comm = Community(humans=humans, relations=relations)

    print(" ------------ check community -------------- ")

    for el in relations:
        for cvor in Comm.relations[el]:
            print(cvor)
        print(" ------------ next el from relations ------------- ")

    print(" ------------- community checked --------------\n")


    print(" ******************************************************************** \n")
    print(" ******************************************************************** \n")
    print(" ---------------------- Zadatak 2. - Racunanje pocinje od cvora sa nazivom: ", cv6.name, " -------------------------")

    CalculateRisk(Comm, cv6)
    print("--------- TEST CalculateRisk () ---------")

    for el in Comm.humans:
        print(str(el.name) + " risk: " + str(el.risk))

    print("--------- Test calculateRisk finished ---------")

    print("*************************************************************************\n")

    print("------------------- PrintPath test (Zadatak 3.) ------------------------\n")

    print("---------------Igor -> Diana (PrintPath)------------------")
    printPath(Comm, cv6, cv5)

    print("---------------Igor -> Marija (PrintPath)------------------")
    printPath(Comm, cv6, cv4)

    print("---------------Igor -> Milan (PrintPath)------------------")
    printPath(Comm, cv6, cv3)

    print("---------------Igor -> Ana (PrintPath)------------------")
    printPath(Comm, cv6, cv2)

    print("---------------Igor -> Ivan (PrintPath) (Nemoguce!)------------------")
    printPath(Comm, cv6, cv1)

    print("---------------Igor -> Nikola (PrintPath) (Nemoguce!)------------------")
    printPath(Comm, cv6, cv7)

    print("---------------Igor -> Nikola (PrintPath)------------------")
    printPath(Comm, cv6, cv8)

    print("\nSta ako postavimo za pocetni cvor, cvor koji nije bio pocetni u BFS algoritmu pretrage\n")
    print("-------------- Ivan -> Nikola --------------")
    printPath(Comm, cv1, cv8)

    print("-------------- Marija -> Ana --------------")
    printPath(Comm, cv4, cv2)

    print("------------- Diana -> Ana -----------")
    printPath(Comm, cv5, cv2)

    print("--------------- Diana -> Milan --------------")
    printPath(Comm, cv5, cv3)

    print("--------------- Diana -> Marija -------------")
    printPath(Comm, cv5, cv4)

    print("-------------- Marija -> Milan ------------ ")
    printPath(Comm, cv4, cv3)

    print("-------------- Milan -> Ana -------------")
    printPath(Comm, cv3, cv2)

    print("\n*******************************************************************************\n")
    print("------------------- Zadatak 4 -------------------\n")

    Radenko = Human(name="Radenko", responsibility=95)
    Marija = Human(name="Marija", responsibility=54)
    Diana = Human(name="Diana", responsibility=70)
    Milan = Human(name="Milan", responsibility=35)
    Ana = Human(name="Ana", responsibility=6)
    Ivan = Human(name="Ivan", responsibility=20)
    Nikola = Human(name="Nikola", responsibility=82)
    Marko = Human(name="Marko", responsibility=33)
    Teodora = Human(name = "Teodora", responsibility=22)
    Igor = Human(name = "Igor", responsibility=13)

    relations = {}

    relations[Radenko] = [Marija, Diana, Nikola]
    relations[Marija] = [Milan]
    relations[Diana] = [Ana, Marko, Ivan]
    relations[Nikola] = [None]
    relations[Milan] = [Ana, Diana]
    relations[Ana] = [None]
    relations[Ivan] = [Nikola]
    relations[Marko] = [Teodora]
    relations[Teodora] = [Ivan, Nikola, Igor]
    relations[Igor] = [Nikola]

    humans = []

    humans.append(Radenko)
    humans.append(Marija)
    humans.append(Diana)
    humans.append(Nikola)
    humans.append(Milan)
    humans.append(Ana)
    humans.append(Ivan)
    humans.append(Marko)
    humans.append(Teodora)
    humans.append(Igor)


    G = Community(humans=humans, relations=relations)
    #CalculateRisk(G, Radenko)
    #printPath(G, Radenko, Igor)

    print("\n______________MATRICA_______________")
    printMatrix(G)
