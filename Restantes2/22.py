
print("Leer un número entero y determinar cuántas veces tiene el dígito 1.\n")


num2 = []
num = int( input("Introduzca un numero  "))
num1 = str(num)
num3 = len(num1)


if num3 >= 1:
	for x in range(0,num3):
		num2.append(num1[x])
		pass
		pass

veces = num2.count('1')
print("El digito 1 se repite" ,veces ,"vez o veces")		
 



input("presione enter para salir")