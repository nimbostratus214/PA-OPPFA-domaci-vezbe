class Node:
    """
    Tree node: left child, right child and data
    """

    def __init__(self, p=None, l=None, r=None, d=None):
        """
        Node constructor
        @param A node data object
        """
        self.parent = p
        self.left = l
        self.right = r
        self.data = d


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

    def print_tree(self):
        def display(root):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if root.right is None and root.left is None:
                line = '%s' % root.data
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if root.right is None:
                lines, n, p, x = display(root.left)
                s = '%s' % root.data
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if root.left is None:
                lines, n, p, x = display(root.right)
                s = '%s' % root.data
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(root.left)
            right, m, q, y = display(root.right)
            s = '%s' % root.data
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        lines, *_ = display(self.root)
        for line in lines:
            print(line)

    # z - čvor koji se dodaje u stablo
    def insert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z

    def walk(self, x):
        if x is not None:
            self.walk(x.left)
            #print("value: ", x.data)  # , ", parent: ", x.parent.data) # , ", left: ", x.left, ", right: ", x.right)
            if x.parent is not None and x.left is not None and x.right is not None:
                #ima i roditelja i levo i desno dete
                print("value: ", x.data, ", parent: ", x.parent.data, ", left: ", x.left.data, ", right: ", x.right.data)
            elif x.parent is not None and x.left is not None:
                #ima roditelja i levo dete, nema desno dete
                print("value: ", x.data, ", parent: ", x.parent.data, ", left: ", x.left.data, ", right: None")
            elif x.parent is not None and x.right is not None:
                #ima roditelja i desno dete, nema levo dete
                print("value: ", x.data, ", parent: ", x.parent.data, ", left: None, right: ", x.right.data)
            elif x.parent is not None:
                #ima roditelja nema ni levo ni desno dete
                print("value: ", x.data, ", parent: ", x.parent.data, ", left: None, right: None")
            else:
                #korenski cvor, nema roditelja
                print("value: ", x.data, ", parent: None, left: None, right: None")
            self.walk(x.right)

    # key - vrednost čvora koji se traži
    def search(self, x, key):
        if x is None or key == x.data:
            return x
        if key < x.data:
            return self.search(x.left, key)
        else:
            return self.search(x.right, key)

    def find_min(self, x):
        while x.left is not None:
            x = x.left
        return x

    # data - vrednost čvora čiji se naslednik traži
    def find_successor(self, data):
        x = self.root
        while x.data is not data:
            if  x.data > data:
                x = x.left
            else:
                x = x.right

        if x.right is not None:
            return self.find_min(x.right)
        y = x.parent
        while y is not None and x == y.right:
            x = y
            y = y.parent
        return y

    def addNode(self, cvor):
        if self.search(self.root, cvor.data) is None:
            T.insert(cvor)
            print("Cvor sa vrednoscu ", cvor.data, " je uspesno dodat u stablo!")
        else:
            print("Nije moguce dodati cvor (", cvor.data, "). Vec postoji u stablu!")

# T = Tree()
# l = [300,216,215,214,250,220,230,225, 270, 269, 271, 400, 350, 550, 351, 530, 535, 570, 580, 575]
# for el in l:
#   T.insert(z = Node(d = el))
# T.insert(z = Node(d = 200))

# T.print_tree()
# T.walk(T.root)
# print("\nsearch 214")
# print(T.search(T.root, 214).data)
# print(T.find_successor(350).data)


# imao sam problem sa dodavanjem main fajla, pa je main modul ovde implementiran
# Radenko Mihajlovic RA 214/2018
if __name__ == "__main__":
    T = Tree()
    l = [300, 216, 215, 214, 250, 220, 230, 225, 270, 269, 271, 400, 350, 550, 351, 530, 535, 570, 580, 575]
    for el in l:
        T.insert(z=Node(d=el))
    # T.insert(z = Node(d = 200))

    T.print_tree()
    T.walk(T.root)
    print("\n --------------------------------------------- \n")
    print("Cvor sa Minimalnom vrednoscu: ", T.find_min(T.root).data)
    print("Cvor naslednik minimalnog: ", T.find_successor(T.find_min(T.root).data).data)
    print("Crveni cvor (535) pronadjen: ", T.search(T.root, 535).data)
    print("Naslednik cvora 535: ", T.find_successor(T.search(T.root, 535).data).data)

    #dodavanje cvora u stablo ako ne postoji

    #dodajemo ova dva cvora!
    T.addNode(Node(d = 214))
    T.addNode(Node(d = 353))
    T.addNode(Node(d=352))
    T.addNode(Node(d=354))
    T.addNode(Node(d=575))
    T.print_tree()

