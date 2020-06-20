print("Mostrar en pantalla el promedio entero de los n primeros múltiplos de 3 para un número n leído.\n")



numero = int(input("Digite un numero: "))


num1 = ((numero * numero * 3) + (numero * 3)) / 2

num2 = int(num1 / numero)



print("el promedio entero de los n primeros múltiplos de 3 para un número n leído es: ", num2)
input("Presione enter para salir")