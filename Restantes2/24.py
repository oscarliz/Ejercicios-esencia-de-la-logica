print("Leer un número entero y determinar a cuánto es igual al suma de sus dígitos pares.\n")


numero = int(input("Digite un numero: "))


def suma_de_digitos(numero): 
    numero = str(numero)
    numero1 = int(numero)
    suma = 0
    for i in numero:
    	numero2 = int(i)
    	if numero2 % 2 == 0 :
    		suma += int(i)
    return suma


suma_2_digitos = suma_de_digitos(numero)
	



print(suma_2_digitos) 






input("Presione enter para salir")