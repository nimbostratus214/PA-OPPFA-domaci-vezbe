import random


def partition(A, pocetak, kraj):
    x = A[kraj]
    i = pocetak - 1
    for j in range(pocetak, kraj):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[kraj] = A[kraj], A[i+1]
    return i + 1

def randomized_partition(A, pocetak, kraj):
    i = random.randint(pocetak, kraj)
    A[kraj], A[i] = A[i], A[kraj]
    return partition(A, pocetak, kraj)

def randomized_quicksort(A, pocetak, kraj):
    if pocetak < kraj:
        q = randomized_partition(A, pocetak, kraj)
        randomized_quicksort(A, pocetak, q - 1)
        randomized_quicksort(A, q + 1, kraj)
        