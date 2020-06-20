print("Leer un número entero y determinar a cuánto es igual al suma de sus dígitos.\n")



def funcion_1(numero): 
    numero = str(numero)
    suma = 0
    for i in numero:
        suma += int(i)
    return suma

numero = int(input("Digite un numero que desee que se sume sus digitos: "))

suma_2_digitos = funcion_1(numero)

suma_final = int(suma_2_digitos)

print(suma_2_digitos) 


input("Presione enter para salir")