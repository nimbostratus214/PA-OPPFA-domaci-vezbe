import math

def merge(A, pocetak, pivot, kraj, obrnuto = 0):
    L_len = pivot - pocetak + 1
    R_len = kraj - pivot
    L, R = [], []

    for i in range(0, L_len):
        L.append(A[pocetak + i])

    for j in range(0, R_len):
        R.append(A[pivot + j + 1])

    i = 0
    j = 0

    if obrnuto == 0:
        L.append(math.inf)
        R.append(math.inf)

        for k in range(pocetak, kraj + 1):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
    else:
        L.append(-math.inf)
        R.append(-math.inf)

        for k in range(pocetak, kraj + 1):
            if L[i] >= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1


def merge_sort(A, pocetak, kraj, obrnuto = 0):
    if pocetak < kraj:
        pivot = (pocetak + kraj) // 2
        merge_sort(A, pocetak, pivot, obrnuto)
        merge_sort(A, pivot + 1, kraj, obrnuto)
        merge(A, pocetak, pivot, kraj, obrnuto)


        