print("Leer un número entero y determinar si la suma de sus dígitos es también un número primo.\n ")





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


def suma_de_digitos(numero): 
    numero = str(numero)
    suma = 0
    for i in numero:
        suma += int(i)
    return suma

numero = int(input("Digite un numero que desee que se sume sus digitos: "))

suma_2_digitos = suma_de_digitos(numero)

suma_final = int(suma_2_digitos)

def klok():
    result = esprimo(suma_2_digitos)

    if result is True:
        print("el numero",suma_2_digitos," es primo")
    else:
        print("el numero",suma_2_digitos," no es primo")

if __name__ == "__main__":
    klok()


input("Presione enter para salir")