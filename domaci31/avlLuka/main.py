
from class_example import *

def buildTree (T, list):
    for el in list:
        tree_insert(T, Node(d = el))



if __name__ == "__main__":
    list = [4, 2, 7, 0, 3, 5, 8, 1, 6, 9]

    T = Tree()
    buildTree(T, list)



    inorder_tree_walk(T.root)
    print("\n Zadatak 6. \n")
    list = [40, 20, 10, 25, 30, 22, 50]

    T = Tree()
    buildTree(T, list)

    inorder_tree_walk(T.root)

    # height = node_height(T.root)
    # print(height)
    # bf = node_bf(T.root.right.right.right)
    # print(bf)