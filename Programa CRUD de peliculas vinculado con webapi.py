import os;
import sys;
import requests;

def limpiar():
	os.system("cls")

def agregar():
	limpiar()
	print("vamos a agregar una pelicua ")
	titulo = input("como se llama?: ")
	autor =input("cual es el autor?: ")
	genero = input("cual es el genero principal?: ")
	cont = titulo + "~"+autor+"~"+genero
	rs = requests.post("http://adamix.net/api/itla/registrarDato",data={'matricula': '20186212', 'clave': 'root', 'contenido': cont })
	print(rs)
	input("Datos guardados, presione enter para continuar")
	menu()

def listar():
	limpiar()
	print("estos son los que has agregado")
	datos = requests.get("http://adamix.net/api/itla/misDatos/20186212/root").text
	datos = datos.split("\n")
	print("aqui estan")
	for f in datos:
		fila = f.split("&")
		peli = fila[2]
		peli = peli.split("~")
		print("titulo: " + peli[0])
		print("autor: " + peli[1])
		print("genero: " + peli[2])
		print("--------------- \n")
	input("presione enter para continuar")
	menu()

def eliminar():
	limpiar()
	print("vamos a borrar una pelicula, dime cual")
	datos = requests.get("http://adamix.net/api/itla/misDatos/20186212/root").text
	datos = datos.split("\n")
	print("aqui estan")
	for f in datos:
	    fila = f.split("&")
	    peli = fila[2]
	    peli = peli.split("~")
	    print("ID: "+fila[0])
	    print("titulo: " + peli[0])
	    print("--------------- \n")
	num = input("digite la pelicula que quieres borrar: " + " ") #chekea aqui
	rs = requests.get("http://adamix.net/api/itla/eliminarDato/" +num+ "/root")
	print(rs)#chekea esto
	print("asunto borrado")
	input()
	menu()

def menu():
	limpiar()
	print("programa que usa api para pelicula")
	print("1- agregar pelicula")
	print("2- lista de peliculas")
	print("3- eliminar pelicula")
	print("4- salir")
	tmp = input("que opcion desea: ")
	if(tmp == "1"):
		agregar()
	elif(tmp == "2"):
		listar()
	elif(tmp == "3"):
		eliminar()
	elif(tmp =="4"):
		limpiar()
		print("adios :")
		sys.exit()
	else:
		print("amigo debe de elegir algo valido")
		menu()
	input()
menu()