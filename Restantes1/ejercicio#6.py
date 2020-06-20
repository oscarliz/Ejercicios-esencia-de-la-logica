print("Leer dos números enteros y almacenar en un vector los 10 primeros números primos comprendidos entre el menor y el mayor. Luego mostrarlos en pantalla.")



count =1
lista=[]
lista1=[]
num=int(input("Introduzca su primer numero:" ))
num0=int(input("Introduzca su segundo numero:" ))


if num < num0:
	while num < num0:
		num += 1
		if num % 2 != 0 or num == 2:
			lista.append(num)

	print(lista[:10])	

elif num0 < num:
	while num0 < num:
		num0 += 1
		if num0 % 2 != 0 or num0 == 2:
			lista1.append(num0)
	print(lista1[:10])				



			




input("Presione enter para salir")
