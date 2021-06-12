
def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key

def bubble_sort(A):
    for i in range(0, len(A)-1):
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j-1]:
                #exchange
                A[j], A[j-1] = A[j-1], A[j]

