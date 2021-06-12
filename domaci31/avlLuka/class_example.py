class Node:
    """
    Tree node: left child, right child and data
    """
    def __init__(self, p = None, l = None, r = None, d = None, h = None, bf = None):
        """
        Node constructor
        @param A node data object
        """
        self.parent = p
        self.left = l
        self.right = r
        self.data = d
        self.heigth = h
        self.bf = bf



class Tree:
    """
    Tree class: contains tree nodes
    """

    def __init__(self, root=None):
        """
        Tree constructor
        @param root element
        """
        self.root = root


def tree_insert(T, z):
    y = None
    x = T.root
    while x is not None:
        y = x
        if z.data < x.data:
            x = x.left
        else:
            x = x.right

    z.parent = y
    if y is None:
        T.root = z
    elif z.data < y.data:
        y.left = z
    else:
        y.right = z




def inorder_tree_walk(x):
    if x is not None:
        inorder_tree_walk(x.left)
        print("data : " + str(x.data) + " height : " + str(node_height(x)) + " bilans faktor : " + str(node_bf(x)))
        inorder_tree_walk(x.right)


def node_height(x):
    if x is None:
        return -1
    else:
        left_height = node_height(x.left)
        right_height = node_height(x.right)

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

def node_bf(x):
    left_height = node_height(x.left)
    right_height = node_height(x.right)
    left_height - right_height
    return left_height - right_height