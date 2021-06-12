# podrzane operacije
oper = ['+', '-', '*', '/']
# podrzane cifre
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# klasa opisuje jedan element stabla (cvor)
# svaki cvor ima svog roditelja, svoju vrednost, i levo i desno dete
class Node:
    def __init__(self, parent=None, left=None, right=None, value=None):
        self.parent = parent
        self.left = left
        self.right = right
        self.value = value


# funkcija koja ce nam vratiti rezultat odredjene operacije

def operation(oper1, oper2, operator):
    if operator == '+':
        return oper1 + oper2
    elif operator == '-':
        return oper1 - oper2
    elif operator == '*':
        return oper1 * oper2
    elif operator == '/':
        return oper1 / oper2
    else:
        print("Unsupported operation!")
        return None

#2.
def eval_tree(tree, dictionary):
    retVal = 0
    # bolje is nego ==
    if tree.left is None and tree.right is None:
        for i in range(0, len(tree.value)):
            if tree.value[i] not in nums:
                return float(dictionary[tree.value])
        return float(tree.value)
    else:
        left = eval_tree(tree.left, dictionary)
        right = eval_tree(tree.right, dictionary)
        if tree.value in oper:
            retVal = operation(left, right, tree.value)
            # print(s)
        return retVal

#3.
def make_infix(tree):
    retVal = ""
    if tree.left is None and tree.right is None:
        return str(tree.value)
    else:
        retVal += "("
        retVal += make_infix(tree.left)
        if tree.value in oper:
            retVal = retVal + " " + str(tree.value) + " "
        retVal += make_infix(tree.right)
        retVal += ")"
        return retVal

# retVal = "( (a + 5) * ( b - c ) ) "

#1.
def get_parse_tree(str):
    # global oper #- global se koristi kako bismo globalnu promenljivu definisanu izvan f-je mogli menjati unutar f-je
    # inace samo mozemo da je citamo !
    l = str.split()
    print(l)
    stack = []
    for x in l:
        n = Node()  # Node(value = x)
        n.value = x  # lepse ovako!
        if x in oper:
            right = stack.pop(-1)
            left = stack.pop(-1)
            n.left = left
            n.right = right
            left.parent = n
            right.parent = n
        stack.append(n)
    return stack[0]



def test(elem):
    list = elem[0]
    dict = elem[1]
    tree = get_parse_tree(list)
    # print(tree.value)
    print("MAKE_INFIX RETURNS: " + make_infix(tree))
    print("EVAL_TREE RETURNS: " + str(eval_tree(tree, dict)))


if __name__ == "__main__":
    for s in [["23 45 67 + -", None], ["a 5 + b c 3 / - *", {'a': 34, 'b': 65, 'c': 3}],
              ["vel_0 time * g time * time 2 / * +", {'vel_0': -10, 'time': 20, 'g': 9.81}]]:
        print("--------------------------------------------------")
        test(s)
        print("--------------------------------------------------\n")
