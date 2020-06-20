print("Promediar los x primeros múltiplos de 2 y determinar si ese promedio es mayor que los y primeros múltiplos de 5 para valores de x y y leídos\n")


numero = int(input("Digite los multipls de 2 deseados: "))
numero1 = int(input("Digite los multipls de 5 deseados: "))

#multiplos de 2
num1 = ((numero * numero * 2) + (numero * 2)) / 2

num2 = int(num1 / numero)

#MUltiplos de 5
num3 = ((numero * numero * 5) + (numero * 5)) / 2

num4 = int(num3 / numero1)

if num2 < num4:
	print("El promedio de los",numero,"primeros multiplos de 2 son mayor que el promedio de los",numero1,"primeros multiplos de 5")
elif num2 > num4:
	print("El promedio de los",numero,"primeros multiplos de 2 son menor que el promedio de los",numero1,"primeros multiplos de 5")
input("Presione enter para salir")