

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
	print("Leer un número entero y determinar a cuánto es igual el promedio entero de sus dígitos.\n")
	numero = int(input("escriba su fabuloso numero: "))

	contador = 1
	
	while contador <=numero:	
		print(contador)
		contador = contador + 1
	validar()
numb()