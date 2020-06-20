print("Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos entre 1 y cada uno de los dígitos.")

num = int( input("Introduzca un numero de 3 digitos  "))
num2 = int(num/100)
num3 = int(num/10)
num4 = num3%10
num5 = num%10
i = 1
p = 1
h = 1


if num < 100 or num > 1000:
	print("Introduzca un numero de 3 digitos")
else:
	
	while i < num2:
		print("\t",i)
		i = i + 1	

	while p < num4:
		print(p,"\t")
		p = p + 1	
	while h < num5:
		print("\t",h)
		h = h + 1	
		pass				
		

   
			
		
	
		
		
input("presione enter para salir")
				
