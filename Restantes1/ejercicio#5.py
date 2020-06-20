print("Almacenar en un vector de 10 posiciones los 10 números primos comprendidos entre 100 y 300. Luego mostrarlos en pantalla.\n")
lista = []
numero = 100
while numero < 300:
	numero += 1
	if numero % 2 != 0:
		lista.append(numero)
		pass

print(lista)

input("Presione enter para salir")
