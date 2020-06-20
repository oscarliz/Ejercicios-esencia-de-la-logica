print("Leer un entero y mostrar todos los multiplos de 5 comprendidos entre 1 y el numero leido\n")

var1 = int(input("Introduzca un valor numerico:"))
for x in range(1,var1):
  if x%5==0:
    print (x)

input()