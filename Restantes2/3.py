import os
import sys

def validar():
	entrada = input("desea continuar? Y/N")
	if entrada.lower () == 's':
		numb ()
	elif entrada () == 'n' :
		sys.exit(1)
	else:
		validar()


def numb ():
	os.system('cls')

	print("leer un numero entero y mostrar todos los divisores exactos del numero comprendidos entre 1 y el numero leido\n")
	numero = int(input("escriba su fabuloso numero: "))

	contador = 1
	
	while contador <=numero:	
		print(contador)
		contador = contador + 2
	validar()
numb()
