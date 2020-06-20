print("Leer un número entero de dos dígitos y mostrar en pantalla todos los enteros comprendidos entre un dígito y otro.\n")

num = int( input("Introduzca un numero de 2 digitos  "))
num2 = int(num/10)
num3 = num%10





if num > 100 or num < 10:
	print("Introduzca un numero de 2 digitos")
else:
	if num2 > num3:
		for h in range(num3,num2):
			print(h)
			pass
	else:
		for i in range(num2,num3):
			print(i)
			pass				
		
input("")