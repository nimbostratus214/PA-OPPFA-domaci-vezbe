#Radenko Mihajlovic RA214/2018

from Huffman import *


def stampaj(ulaz, mod, brojac):

    histogram = GetHistogram(ulaz)
    temp = histogram[:]
    print("input", brojac, ": ", ulaz)
    size = 0
    for el in histogram:
        if mod == 0:
            print("Karakter: ", el.vrednost, " ; Frekvencija: ", el.frekvencija)
        size = size + el.frekvencija * 8  # 8-bit

    while len(histogram) > 1:
        elem1 = MinElement(histogram)
        obrisiEl(elem1, histogram)
        elem2 = MinElement(histogram)
        obrisiEl(elem2, histogram)
        histogram.append(generateElement(elem1, elem2))

    d = dict()
    huffman_size = 0
    if mod == 0:
        print("Enkodovane vrednosti karaktera: ")
    for el in temp:
        enc = encode(el, histogram)
        d[el.vrednost] = enc
        huffman_size += el.frekvencija * len(enc)
        if mod == 0:
            print(el.vrednost, " -> ", enc)

    izlaz = ""
    for el in ulaz:
        izlaz += d[el]

    print("Enkodovan input", cnt, ": ", izlaz)
    if mod == 0:
        print("Velicina teksta pre kodovanja: ", size, "bita. Nakon primene Huffmanovog algoritma velicina je: ",
              huffman_size, "bita")
    print("----------------------------------------------------------")


if __name__ == "__main__":

    input1 = ['a', 'b']
    input2 = ['a', 'b', 'a', 'b', 'a', 'b', 'a', 'b', 'a', 'b']
    input3 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c']
    input4 = ['a', 'a', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd']
    input5 = ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c', 'd', 'd', 'd', 'd', 'd', 'd', 'e', 'e', 'f']

    inputs = [input1, input2, input3, input4, input5]

    #obrada nad svakim ulazom

    mode = 0  # 0 - print all info; 1 - before and after encoding
    cnt = 1

    for i in inputs:
       stampaj(i, mode, cnt)
       cnt += 1





