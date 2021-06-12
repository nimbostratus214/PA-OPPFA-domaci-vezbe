
#papir pobedjuje kamen, kamen pobedjuje makaze, makaze pobedjuju papir
#index 0 pobedjuje index 1; index jedan pobedjuje index 2; index 2 pobedjuje index 0

elements = ['PAPIR', 'KAMEN', 'MAKAZE']

#f-ja proverava da li je unet neki od elemenata (papir, kamen, makaze)
def check_validity(s):
    if s.upper() in elements:
        return False
    print("Invalid input: ", s)
    return True

def pkm():
    p1 = input("Player 1: ")  #pokupimo ulaz prvog
    while check_validity(p1):  #ako je dobar unos, preskocice ovo, ako nije ponovo mu nudi da unese ispravno
        p1 = input("Player 1: ")

    p2 = input("Player 2: ") #isto kao za prvog
    while check_validity(p2):
        p2 = input("Playyer 2: ")

    for i in range(len(elements)):   #uzmemo index unetog elementa iz liste (za prvog igraca)
        if elements[i] == p1.upper():
            x = i

    #alternativno mozemo odrediti i index drugog igraca pa izmeniti dole logiku!
    #for i in range(len(elements)):
    #    if elements[i] == p2.upper():
    #        y = i

    if p2.upper() == elements[(x+1) % 3]:  #ako index biranog elementa igraca p2 odgovara sledbeniku igraca p1, pobednik je p1
        print("Player 1 wins because ", p1.upper(), " beats ", p2.upper())
    elif p2.upper() == elements[((x+1) % 3 + 1)%3]:  #ako index drugog sledi dva mesta iza prvog pobednik je prvi
        print("Player 2 wins because ", p2.upper(), " beats ", p1.upper())
    else:
        print("It's a Tie!")