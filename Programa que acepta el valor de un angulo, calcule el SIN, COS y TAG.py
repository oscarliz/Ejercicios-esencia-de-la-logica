import math
print("Programa que acepta el valor de un angulo, calcule el SIN, COS y TAG")
s = input("escribe un numero: \n")
s1 = float (s)


x = math.radians(s1)
y = math.radians(s1)
z = math.radians(s1)



print("este es el seno: ",math.sin(x))
print("este es el coseno:",math.cos(y))
print("este es el tangente:",math.tan(z))

input("Preciona Enter Para Salir")