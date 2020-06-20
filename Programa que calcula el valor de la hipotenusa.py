import math
print("Programa que calcula el valor de la hipotenusa")
n1 = input("cateto one:")
n2 = input("cateto two:")

n1 = int (n1)
n2 = int (n2)

multiplicacion = n1**2 + n2**2
area = math.sqrt(multiplicacion) 

print("La hipotenusa es: ",area)
input()