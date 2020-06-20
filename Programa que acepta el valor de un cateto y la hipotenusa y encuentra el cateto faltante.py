import math
print("Programa que acepta el valor de un cateto y la hipotenusa y encuentra el cateto faltante")
cateto = int(input("Introduzca el cateto "))
if cateto>0:
	hipotenusa = int(input("Introduzca la hipotenusa "))
	

if hipotenusa > cateto:
	h = cateto**2 - hipotenusa**2 
	h2 = h * -1
	s2 = math.sqrt(h2)
	print("El cateto que falta es ",s2)

input("Preciona Enter para salir")
