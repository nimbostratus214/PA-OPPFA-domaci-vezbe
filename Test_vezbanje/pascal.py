#Pascalov trougao (zadatak 11)

def cif_num(n):
    cif = 1
    while n / 10 >= 1:
        cif += 1
        n = n//10

    return cif


def cif_num_list(l):  #koliko razmaka nam treba
    spacer = 0
    for i in l:
        spacer += cif_num(i)
    return spacer


def pascal():
    height = int(input("Unesite visinu trougla: "))
    t = []
    for i in range(height):
        t.append([])

    for i in range(len(t)):           # i -> ide po visini piramide
        t[i].append(1)               # svaki red pocinje sa jedinicom
        if i == 0:                  # ako smo u "nultom" redu, tu imamo samo jedan element tako da se prelazi na sledecu iteraciju
            continue
        for j in range(i - 1):       # j -> iterira po trenutnom redu, ide do (i-1) elementa, jer ce nam se na kraju nalaziti jedinica (svaki red se zavrsava sa jedinicom)
            t[i].append(t[i-1][j] + t[i-1][j+1])     #u listu t[i] dodajemo element iz prethodnog reda (t[i-1]) na poziciji [j] (dakle t[i-1][j]) koji se sabira sa njegovim sledbenikom dakle t[i-1][j+1]
        t[i].append(1)                # na kraj liste u trenutnom redu dodajemo jedinicu i prelazimo u novi red

    #print(t)       #prvi ispis
    #for i in t:
    #    print(i)

    #for i in range(len(t)):      #ispis bez zagrada iz liste
    #    for j in t[i]:
    #        print(j, end=" ")
    #    print()
    for i in range(len(t)):          #zajeban ispis -> idemo kroz piramidu po visini
        print(" " * ((cif_num_list(t[-1]) - cif_num_list(t[i]) + (height - i))//2), end="") # razmka * (broj cifara poslednjeg reda - broj cifara trenutnog reda + visina - trenutna_pozicija) // 2 +i na kraju se dodaje ""
        for j in t[i]:              #dodajemo na kraj svakog elementa trenutne liste razmak
            print(j, end=" ")
        print()     #novi red


if __name__ == "__main__":
    pascal()
    #print(cif_num(int(input())))
