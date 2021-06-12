from function import *

if __name__ == "__main__":
    x = "aacttcgg"
    y = "cacgtatag"

    log = "logaritam"
    alg = "algoritam"


    print("x =", x)
    print("y =", y)

    m = LCS(x, len(x) - 1, y, len(y) - 1)
    print("Recursive LCS : ", m)

    (c, b) = LCS_Length(x, y)
    print("Dynamic LCS : ", end = "")
    print_LCS(b, x, len(x), len(y))
    print()

    print()
    print("x =", log)
    print("y =", alg)

    m = LCS(log, len(log) - 1, alg, len(alg) - 1)
    print("Recursive LCS : ", m)

    (c, b) = LCS_Length(log, alg)
    print("Dynamic LCS : ", end="")
    print_LCS(b, log, len(log), len(alg))
    print()


