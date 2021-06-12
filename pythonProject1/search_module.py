

def linearSearch(A, x):
    retval = {}
    for i in range(0, len(A)):
        if A[i] == x:
            retval = {"Element " : A[i] , "Pozicija: ": i}
            return print(retval)
            #return print("\nTrazeni element ", A[i], " se nalazi na poziciji: ", i)

    return print("\nElement ne postoji u datoj listi! \n")

def binarySearch(A, pocetak, kraj, x):

    sredina = (pocetak+kraj)//2 #medijan niza, "deljenje sa zaokruzivanjem

    if A[sredina] > x:
        #print(A)
        return binarySearch(A, pocetak, sredina - 1, x)
    elif A[sredina] < x:
        #print(A)
        return binarySearch(A, sredina + 1, kraj, x)
    else:
        print(A)
        return sredina




# Kako resiti problem ako se izabere element koji ne postoji u nizu
# Ogranicen broj rekurzivnih poziva u pythonu na 1000 (moze da se setuje vise),
# ali u ovom slucaju to ide u nedogled?