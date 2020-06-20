import os
import json
from pathlib import Path

ninjas = []

ubicacion = Path("cosa.txt")
if ubicacion.exists():
	archivo = open("cosa.txt", "r")
	datos = archivo.read()
	archivo.close()
	ninjas = json.loads(datos)


def menu():
	os.system("cls")
	print("bienvenid@ a al creador de ninjas\n")
	print("a - agregar ninja\n")
	print("v - ver ninja\n")
	print("e - eliminar ninja\n")
	print("x - salir\n")

continuar = True

while(continuar):
	menu()
	opt = input("digite su opcion: ")

	if opt == 'a':

		print("vamos a agregar un ninja\n")
		pmk = []
		pmk.append(input("digite el nombre del ninja: "))
		pmk.append(input("digite la fecha en que nacio el ninja: "))
		pmk.append(input("digite la aldea del ninja: "))
		pmk.append(input("digite el tipo de chakra del ninja: "))
		pmk.append(input("digite el rango del ninja: "))
		pmk.append(input("digite las tecnicas ninja: "))
		ninjas.append(pmk)
		datos = json.dumps(ninjas)
		f = open('cosa.txt','w')
		f.write(datos)
		f.close()
		input("ninja agregado presione enter")



	elif opt == 'v':
		print("aqui estan los ninja que hemos atrapado")
		for pkm in ninjas:
			print(pkm[0], "\t", pkm[1], "\t", pkm[2], "\t", pkm[3], "\t", pkm[4], "\t", pkm[5])
		input("esto son lo que estan")

	elif opt == 'x':
		continuar = False

	elif opt == 'e':
		os.remove("cosa.txt")
		input("el ninja fue eliminado con exito")

	else:
		print("opcion no valida, amig@ digite una opcion valida")
		input("presione enter para continuar")
