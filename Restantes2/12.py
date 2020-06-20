print("Leer un número entero de 3 dígitos y determinar si tiene el dígito 1.\n")


num = int( input("Introduzca un numero de 3 digitos  "))
num2 = str(num)


if num2.find("1") == -1:
	print("El numero",num,"no contiene el digito 1")
elif num2.find("1") == 0:
	print("El numero",num,"contiene el digito 1")

	print(num2.find("1"))	 


input("presione enter para salir")