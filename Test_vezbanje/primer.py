# Napisati program koji cita podatke iz .txt datoteke i svaku rec iz jedne linije smesta
# u listu. Zatim brise prvu rec iz liste i kreira string od preostalih elemenata.
# Kreirani string se upisuje u novu datoteku.
# Imena datoteka se prosledjuju kao argumenit komandne linije.
# Pokretanje programa: python primer.py data.txt newdata.txt

import sys


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Command line arguments is not valid!")
        exit(-1)

    file1 = open(sys.argv[1], 'r')
    file2 = open(sys.argv[2], 'w')
    #print(file1.read()) #iscita sve iz datoteke
    #print(file1.readlines()) #cita linije iz datoteke u formatu liste
    lines = file1.readlines()

    for line in lines:
        words = line.split(' ') #razdvaja linije (separator je ' ', moze i nesto drugo)
        #print("PRVA LISTA", words)
        del words[0]
        #print()
        #print("NAKON BRISANJA" , words)
        str = " ".join(words) #metoda spaja listu u string, separator je razmka " "
        #print(str)
        file2.write(str)
    file2.close()
    file1.close()


    while True:
        a = input("Unesite slovo: ")
        if not a.isalpha():
            print("Niste uneli slovo!")
            break