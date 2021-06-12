import random
import time
import MergeSort
import QuickSort

def random_list(min, max, broj_elemenata):
    list = random.sample(range(min, max), broj_elemenata)
    return list

if __name__ == "__main__":
    print("------------Test------------")
    A = random_list(0, 20, 10)
    print("\nNiz: ", A)
    MergeSort.merge_sort(A, 0, len(A) - 1)
    print("\nSortiran: ", A)
    print("----------------------------\n")

    A = random_list(0, 1000, 100)
    start = time.perf_counter()
    MergeSort.merge_sort(A, 0, len(A) - 1)
    stop = time.perf_counter() - start
    print("Vreme za ", len(A), ": ", stop)

    A = random_list(0, 10000, 1000)
    start = time.perf_counter()
    MergeSort.merge_sort(A, 0, len(A) - 1)
    stop = time.perf_counter() - start
    print("Vreme za ", len(A), ": ", stop)

    A = random_list(0, 100000, 10000)
    start = time.perf_counter()
    MergeSort.merge_sort(A, 0, len(A) - 1)
    stop = time.perf_counter() - start
    print("Vreme za ", len(A), ": ", stop)

    A = random_list(0, 1000000, 100000)
    start = time.perf_counter()
    MergeSort.merge_sort(A, 0, len(A) - 1)
    stop = time.perf_counter() - start
    print("Vreme za ", len(A), ": ", stop)

    A = random_list(0, 3000000, 1000000)
    start = time.perf_counter()
    MergeSort.merge_sort(A, 0, len(A) - 1)
    stop = time.perf_counter() - start
    print("Vreme za ", len(A), ": ", stop)

    print("\n----------QuickSortTest----------")
    A = random_list(0, 20, 10)
    print("Niz: ", A)
    QuickSort.randomized_quicksort(A, 0, len(A) - 1)
    print("Slozen niz: ", A)
    print("-----------------------------------\n")

    print("------QuickSortTimeTests-----------\n")

    A = random_list(0, 1000, 100)
    start = time.perf_counter()
    QuickSort.randomized_quicksort(A, 0, len(A) - 1)
    stop = time.perf_counter() - start
    print("Vreme za", len(A), ": ", stop)

    A = random_list(0, 10000, 1000)
    start = time.perf_counter()
    QuickSort.randomized_quicksort(A, 0, len(A) - 1)
    stop = time.perf_counter() - start
    print("Vreme za", len(A), ": ", stop)

    A = random_list(0, 100000, 10000)
    start = time.perf_counter()
    QuickSort.randomized_quicksort(A, 0, len(A) - 1)
    stop = time.perf_counter() - start
    print("Vreme za", len(A), ": ", stop)

    A = random_list(0, 1000000, 100000)
    start = time.perf_counter()
    QuickSort.randomized_quicksort(A, 0, len(A) - 1)
    stop = time.perf_counter() - start
    print("Vreme za", len(A), ": ", stop)

    A = random_list(0, 3000000, 1000000)
    start = time.perf_counter()
    QuickSort.randomized_quicksort(A, 0, len(A) - 1)
    stop = time.perf_counter() - start
    print("Vreme za", len(A), ": ", stop)