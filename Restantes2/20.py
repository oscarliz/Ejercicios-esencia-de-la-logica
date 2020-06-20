import os

def validarContinuar():


	continuar = input("\n desea continuar (s/n)?")
	if continuar == "s":
		progrma()
	elif continuar == "n":
		return False
	else:
		validarContinuar()

def programa():

	os.system("cls")
	os.system("color e")
	print("Leer un numero entero y determinar cuantos digitos tiene\n")
	numero = input("ingrese un numero entero: ")
	print("----------------------------------- \n")
	print("el "+numero+" tiene "+str(len(numero))+".")
	validarContinuar()

programa()
input()