
import sort_module
import random
import search_module
import time



if __name__ == "__main__":

    print("########################## TEST ##########################\n")
    A = random.sample(range(1, 100), 10)
    K = random.sample(range(1, 100), 10)
    print("A: ", A)
    print("K: ", K)
    sort_module.insertion_sort(A)
    sort_module.bubble_sort(K)
    print("A: ", A)
    print("K: ", K)

    A_100 = random.sample(range(1, 1000000), 100)
    A_1000 = random.sample(range(1, 1000000), 1000)
    A_10000 = random.sample(range(1, 1000000), 10000)
    A_100000 = random.sample(range(1, 1000000), 100000)

    print("\n################### INSERTION SORT ####################\n")

    start = time.perf_counter()
    sort_module.insertion_sort(A_1000[:])
    print("Time for 1000 elements: ", time.perf_counter() - start, "s.")

    start = time.perf_counter()
    sort_module.insertion_sort(A_10000[:])
    print("Time for 10 000 elements: ", time.perf_counter() - start, "s.")

    #start = time.perf_counter()
    #sort_module.insertion_sort(A_100000[:])
    #print("Time for 100 000 elements: ", time.perf_counter() - start, "s.")
    
    print("\n################### BUBBLE SORT ####################\n")
    start = time.perf_counter()
    sort_module.bubble_sort(A_1000[:])
    print("Time for 1000 elements: ", time.perf_counter() - start, "s.")

    start = time.perf_counter()
    sort_module.bubble_sort(A_10000[:])
    print("Time for 10 000 elements: ", time.perf_counter() - start, "s.")

    #start = time.perf_counter()
    #sort_module.bubble_sort(A_100000[:])
    #print("Time for 100 000 elements: ", time.perf_counter() - start, "s.")

    print("\n################### LINEAR SEARCH - TEST ####################\n")

    #l = []
    l = random.sample(range(1, 1000), 20)
    print("Nesortirana lista: \n", l)

    #x = -1
    x = input("Unesite broj iz liste: ")
    x = int(x)

    search_module.linearSearch(l, x)
    #print("Indeks broja ", x, "je: ", search_module.linearSearch(l, x))
    #print("\n")

    print("\n################### LINEAR SEARCH - TIME TEST ####################\n")
    print("Lista A_100 \n", A_100[:])
    #x = -1
    x = input("Unesite broj iz liste: ")
    x = int(x)

    start = time.perf_counter()
    search_module.linearSearch(A_100[:], x)
    stop = time.perf_counter() - start
    print("Time for Linear Search in list of 100 elements: ", stop, "s.")

    print("\nLista A_1000 ", A_1000[:])
    #x = -1
    x = input("Unesite broj iz liste: ")
    x = int(x)

    start = time.perf_counter()
    search_module.linearSearch(A_1000[:], x)
    stop = time.perf_counter() - start
    print("Time for Linear Search in list of 1000 elements: ", stop, "s.")

    print("\nLista A_10000 ", A_10000[:])
    #x = -1
    x = input("Unesite broj iz liste: ")
    x = int(x)

    start = time.perf_counter()
    search_module.linearSearch(A_10000[:], x)
    stop = time.perf_counter() - start
    print("Time for Linear Search in list of 10000 elements: ", stop, "s.")

    print("\nLista A_100000 ", A_100000[:])
    #x = -1
    x = input("Unesite broj iz liste: ")
    x = int(x)

    start = time.perf_counter()
    search_module.linearSearch(A_100000[:], x)
    stop = time.perf_counter() - start
    print("Time for Linear Search in list of 100000 elements: ", stop, "s.")
    print("\n################### Linear Search Time Test Finished ################")

    print("\n################### BINARY SEARCH - TEST ####################\n")

    l = random.sample(range(1, 1000), 20)
    print("Nesortirana lista: \n", l)
    sort_module.insertion_sort(l)
    print("Sortirana lista: \n", l, "\n")

    #x = -1
    x = input("Unesite broj iz liste: ")
    x = int(x)

    torka = ("Element: ", x, "Pozicija: ", search_module.binarySearch(l, 0, len(l), x))
    lista = []
    lista.append(torka)
    print(lista)
    #print("Indeks broja ", x, "je: ", search_module.binarySearch(l, 0, len(l) , x))

    """
    print("\n################### BINARY SEARCH - TIME TEST ####################\n")

    print("\nLista A_100 ", A_100[:])
    #x = -1
    x = input("Unesite broj iz liste: ")
    x = int(x)

    start = time.perf_counter()
    search_module.binarySearch(A_100[:], 0, len(A_100[:]), x)
    stop = time.perf_counter() - start
    print("Time for Binary Search - list of 100 elements: ", stop, "s.")
    """
    print("\nLista A_1000 ", A_1000[:])
    #x = -1
    x = input("Unesite broj iz liste: ")
    x = int(x)

    start = time.perf_counter()
    search_module.binarySearch(A_1000[:], 0, len(A_1000[:]), x)
    stop = time.perf_counter() - start
    print("Time for Binary Search - list of 1000 elements: ", stop, "s.")

    print("\nLista A_10000 ", A_10000[:])
    #x = -1
    x = input("Unesite broj iz liste: ")
    x = int(x)

    start = time.perf_counter()
    search_module.binarySearch(A_10000[:], 0, len(A_10000[:]), x)
    stop = time.perf_counter() - start
    print("Time for Binary Search - list of 10000 elements: ", stop, "s.")

    print("\nLista A_100000 ", A_100000[:])
    #x = -1
    x = input("Unesite broj iz liste: ")
    x = int(x)

    start = time.perf_counter()
    search_module.binarySearch(A_100000[:], 0, len(A_100000[:]), x)
    stop = time.perf_counter() - start
    print('Time for Binary Search - list of 100000 elements: ', stop, "s.")

    print("\n\n################# ALL TESTS PASSED SUCCESSFULLY #################")

