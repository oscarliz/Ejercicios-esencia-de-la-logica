

def esprimo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True            

def klok():
    print("Leer un numero y determinar si es primo\n")

    num = int(input("Escribe un numero: "))
    result = esprimo(num)

    if result is True:
        print("el numero es primo")
    else:
        print("el numero no es primo")

if __name__ == "__main__":
    klok()

input()