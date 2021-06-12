class Data:
    """
    Data constructor
    @param val1 - Number representing Letter/character in morse tree - Naglaseno u zadatku da se svaki karakter  predstavi nekim brojem, jer je lakse za prolazak kroz stablo!
    @param val2 - letter/character in morse tree
    """

    def __init__(self, val1, val2):
        self.a1 = val1  #broj koji predstavlja odredjeni karakter
        self.a2 = val2 #sam karakter


class Node:
    """
    Node constructor
    @param p - node parent
    @param l - left child
    @param r - right child
    @param d - data
    """

    def __init__(self, p=None, l=None, r=None, d=None):
        self.parent = p  #roditelj
        self.left = l   #levo i desno dete
        self.right = r
        self.data = d  #objekat klase data (reprezentativni broj, sam karakter)


class Tree:
    """
    Tree constructor
    @param root - tree root
    """

    def __init__(self, root=None):
        self.root = root #prazno stablo, root cvor


# insert node z into tree T
def tree_insert(T, z): #ubacivanje elementa z (objekat klase Node) u stablo
    y = None
    x = T.root
    while x is not None:  # find empty place for z
        y = x
        if z.data.a1 < x.data.a1:
            x = x.left
        else:
            x = x.right

    z.parent = y
    if y is None:  # z should be root
        T.root = z
    elif z.data.a1 < y.data.a1:  # z should be left child
        y.left = z
    else:  # z should be right child
        y.right = z


def inorder_tree_walk(x):
    if x is not None:
        inorder_tree_walk(x.left)
        print(x.data.a1)
        inorder_tree_walk(x.right)


def search_tree(root, node):
    '''
    Print morse code from word - encoding
    @param root - (sub)tree root node
    @param node - one character in word
    '''
    if root is not None and root.data.a1 == node.a1:
        return node  # node has been found
    elif node.a1 < root.data.a1:  # if node is left child print code .
        print('.', end="")
        return search_tree(root.left, node)
    else:
        print('-', end="")  # if node is right child print code -
        return search_tree(root.right, node)


def find_character(node, code):
    '''
    Find word from morse code - decoding
    @param root - (sub)tree root node
    @param code - morse code
    '''
    global err
    err = 0

    if len(code) == 0:  # all characters are processed -> node has been found
        print(node.data.a2, end=' ')
        return

    if code[0] == '.':  # if first character in code is . look from character in left subtree
        if node.left is not None:
            find_character(node.left, code[1:])  # first charachter has been processed, check others
        else:
            err = 1  # error -> . in right
            return

    elif code[0] == '-':  # if first character in code is - look from character in right subtree
        if node.right is not None:
            find_character(node.right, code[1:])  # first charachter has been processed, check others
        else:
            err = 1  # error -> . in right
            return


def buildTree(T, morse_dict):
    for k, v in morse_dict.items():
        tree_insert(T, Node(d=Data(k, v)))


if __name__ == '__main__':
    morse_dict = {
        21: '',
        11: 'E', 32: 'T',
        6: 'I', 16: 'A', 28: 'N', 37: 'M',
        3: 'S', 8: 'U', 13: 'R', 18: 'W', 25: 'D', 30: 'K', 35: 'G', 40: 'O',
        1: 'H', 4: 'V', 7: 'F', 9: '', 12: 'L', 15: '', 17: 'P', 19: 'J',
        23: 'B', 27: 'X', 29: 'C', 31: 'Y', 34: 'Z', 36: 'Q', 39: '', 42: '',
        0: '5', 2: '4', 5: '3', 10: '2', 14: '+', 20: '1',
        22: '6', 24: '=', 26: '/', 33: '7', 38: '8', 41: '9', 43: '0'
    }

    # reverse dict - keys become values and values become keys
    reverse_morse_dict = {v: k for k, v in morse_dict.items()}  # needed for search by letter

    T = Tree()
    buildTree(T, morse_dict)
    # print(T.root.data.a1)
    inorder_tree_walk(T.root)

    # encoding
    word = "PERA PERIC"
    for ch in word:
        if ch == " ":
            print(' / ', end="")
        else:
            if ch in reverse_morse_dict:
                search_tree(T.root, Data(reverse_morse_dict[ch], ch))
                print(' ', end="")
            else:
                print('Invalid data ->', ch)

    print('\n\nreverse:\n')

    # decoding
    word = '.--. . .-. .-  / .--. . .-. .. -.-.'
    word_arr = word.split(' ')
    for ch in word_arr:
        if ch == '/':
            print('\n')
        else:
            find_character(T.root, ch)
            if err == 1:
                print('Invalid data ->', ch)


