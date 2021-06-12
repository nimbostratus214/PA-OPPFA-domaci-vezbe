#Paskalov trougao

#input
paskalov_trougao = []

def pascal_triangle(visina):
    while len(paskalov_trougao) < visina:
        paskalov_trougao.append([0])

    for element in range(visina):
        count = 1
        while count < visina - element:
            paskalov_trougao[count+element].append(0)
            count += 1

        for row in paskalov_trougao:
            row.insert(0, 1)
            row.append(1)
        paskalov_trougao.insert(0, [1, 1])
        paskalov_trougao.insert(0, [1])




n = int(input("Unesite visinu Paskalovog trougla: "))

