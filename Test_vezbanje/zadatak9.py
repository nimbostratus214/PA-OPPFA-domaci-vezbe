
def CalculateSum(num):
    sum = 0
    while num != 0:
        sum += num % 10
        num //= 10

    return sum

def IsPrime(num):
    for x in range(2, num):
        if num % x == 0:
            return False

    return True
#u istom modulu implementiran i test, promeniti u edit_configurations script path na ovu skriptu!
if __name__ == "__main__":
    dict = {}
    while True:
        input_val = input("Unesite broj: ")
        if input_val.isdigit():  #provera da li je broj (umesto try->except)
            num = int(input_val)
        else:
            break

        sum = CalculateSum(num)
        isPrime = IsPrime(num)
        dict[num] = (sum, isPrime)

    print("Izlaz: ", dict)