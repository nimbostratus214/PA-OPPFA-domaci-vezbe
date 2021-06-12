import random
import bucketSort
import heapSort




def rand_list(min, max, num):
    l = random.sample(range(min, max), num)
    return l


if __name__ == "__main__":
    A = rand_list(0, 20, 10)
    print("Pocetna lista: ", A)
    sorted_list = bucketSort.bucket_sort(A)
    print("Sortirana lista (Bucket): ", sorted_list)

    A = rand_list(0, 20, 10)
    print("Pocetna lista: ", A)
    heapSort.HeapSort(A)
    print("Sortirana lista (Heap): ", A)

