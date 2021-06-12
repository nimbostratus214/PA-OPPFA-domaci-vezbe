
#Verzija sa recnikom (iz pdf-a za pripremu)

elements = ['PAPIR', 'KAMEN', 'MAKAZE', 'PREDAJA']

def check_validity(s):
    if s.upper() in elements:
        return False
    print("Invalid input: ", s)
    return True

#def funny(cnt1, cnt2):
#    if (cnt1 > cnt2):
#        print("Igrac jedan je unistio drugog igraca!")
#    elif(cnt1 < cnt2):
#        print("Drugi igrac je otkinuo od zivota prvog igraca!")
#    else:
#        print("Aj ponovo, nereseno je!")

def pkm():

    #cnt1 = 1
    #cnt2 = 1
    while True:
        p1 = input("Prvi igrac bira: ")
        if p1.upper() == elements[3]:
            print("Predao se prvi igrac!")
            #funny(cnt1, cnt2)
            break
        while check_validity(p1):
            p1 = input("Prvi igrac bira: ")

        p2 = input("Drugi igrac bira: ")
        if p2.upper() == elements[3]:
            print("Predao se drugi igrac.")
            #funny(cnt1, cnt2)
            break
        while check_validity(p2):
            p2 = input("Drugi igrac bira: ")

        dict = {}
        dict[1] = p1.upper()
        dict[2] = p2.upper()

        if (dict[1] == dict[2]):
            print("Nereseno je, igrajte ponovo igru!")

        for it in range(0, 3):
            if elements[it] == dict[1]:
                x = it

        if dict[2] == elements[(x+1)%3]:
            print("Pobednik je prvi igrac jer ", dict[1], " pobedjuje ", dict[2], ".")
            #cnt1 += 1
        else:
            print("Pobednik je drugi igrac jer ", dict[2], " pobedjuje ", dict[1], ".")
            #cnt2 += 1

if __name__ == "__main__":
    pkm()