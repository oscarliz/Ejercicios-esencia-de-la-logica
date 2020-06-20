

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
	print("Leer dos numeros y mostrar todos los enteros comprendidos entre ellos\n")
	numero = int(input("escriba su fabuloso numero: "))
	numero2 = int(input("escriba su fabuloso numero: "))

	contador = numero + 1
	numero2 = numero2 - 1
	while contador<=numero2:
		print(contador)
		contador = contador +1
	validar()
numb()


				
