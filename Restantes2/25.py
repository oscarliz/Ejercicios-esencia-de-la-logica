print("Leer un número entero y determinar a cuánto es igual el promedio entero de sus dígitos.\n")


def suma_de_digitos(numero): 
    numero = str(numero)
    suma = 0
    for i in numero:
        suma += int(i)
    return suma

numero = int(input("Digite un numero: "))
numero2 = str(numero)
numero3 = len(numero2)

suma_2_digitos = suma_de_digitos(numero)

suma_final = int(suma_2_digitos)
 
suma_total = suma_final / numero3

print(suma_total) 


input()