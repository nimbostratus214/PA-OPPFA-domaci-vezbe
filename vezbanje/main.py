from tree import *


L = [15, 11, 26, 8, 12, 20, 30, 6, 9, 14, 35]

nodeList = []


for e in L:
    nodeList.append(Node(key = e))
#svi su none, dakle napravili smo cvorove
for n in nodeList:
    print(n)

T = Tree()
for n in nodeList:
    treeInsert(T, n)
print("TEST CVOR 12")
print(nodeList[4])
print(nodeList[4].p)
print(nodeList[4].r)

print("InOrderTreeWalk")
inOrderTreeWalk(nodeList[0])

print("treeMin")
print(treeMin(nodeList[0])) #indeks, ne vrednost :D

print("treeMax")
print(treeMax(nodeList[0]))

print("treeSuccessor od cvora: ", nodeList[8])
print(treeSuccessor(nodeList[8]))

print("treeSearch for ", 9, " in tree ", nodeList[2])
print(treeSearch(nodeList[2], 9))

#treba nam za brisanje
print("Transplant/TreeDelete")
treeDelete(T, nodeList[0]) #brisemo koren
print(T.root) #ko je sad koren


print("Search for ", nodeList[8], " in tree ", nodeList[0])
print(iterativeSearch(nodeList[0], 9))
print("Search for ", nodeList[8], " in tree ", nodeList[2])
print(iterativeSearch(nodeList[2], 9))

