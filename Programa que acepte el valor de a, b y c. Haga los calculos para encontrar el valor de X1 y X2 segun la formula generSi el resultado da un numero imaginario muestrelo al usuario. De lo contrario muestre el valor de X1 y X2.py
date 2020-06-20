import math 

a = float(input("ingrese el valor de (a):"))
b = float(input("ingrese el valor de (b):"))
c = float(input("ingrese el valor de (c):"))

d = (b*b)-4*a*c

if d<0:
	print("no existen soluciones reales")

else:
	x1 = (-b+math.sqrt(d))/(2*a)
	x2 = (-b-math.sqrt(d))/(2*a)

	print("solucion x1: ",x1)
	print("solucion x2: ",x2)

input()
