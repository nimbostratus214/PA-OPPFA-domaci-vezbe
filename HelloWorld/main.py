import sys    #biblioteka za sistemske pozive

print("__name__value:", __name__) #donja crta je za sistemske funkcije (ovo daje ime glavne skripte koja pokrece ovaj kod)

"""
print("Hello from module")
"""

def main():
    print("Hello from main()")
    myfoo("moj argument")

def myfoo(arg1):
    print("Hello from myfoo()")
    print("arg1 value: ", arg1)

if __name__ == '__main__':
    print("Hello from executable module")
    main()

