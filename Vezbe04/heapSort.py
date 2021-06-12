

def parent(i):
    return (i-1)//2

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def maxHeapify(A, i, heap_size):   #i index cvora koji zelimo postaviti na pravo mesto....heap_size -> koliko elemenata unutar cvora a pripada heapu
    l = left(i)
    r = right(i)
    #koji od ovih cvorova je najveci
    if l < heap_size and A[l] > A[i]:    #levo dete pripada heapu i vece je od cvora i
        largest = l              #najvece je levo dete
    else:
        largest = i         #najveci je cvor i

    if r < heap_size and A[r] > A[largest]:
        largest = r

    if largest != i:                  #ako je najveci pronadjen cvor razlicit od pocetnog od kog smo krenuli, treba uraditi zamenu
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, largest, heap_size)  #rekurzivno pozivamo sada za pronadjen najveci element


def buildMaxHeap(A, heap_size):
    heap_size = len(A)
    for i in range(len(A)//2 , -1, -1):   #??????  -> jer range() ide od-do, ne ukljucuje poslednji element a nama je potreban i on, zato je -1
        maxHeapify(A, i, heap_size)


def HeapSort(A):
    heap_size = len(A)
    buildMaxHeap(A, heap_size)
    for i in range(len(A) - 1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heap_size -= 1
        maxHeapify(A, 0, heap_size)