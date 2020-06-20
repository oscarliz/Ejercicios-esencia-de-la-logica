print("Leer 10 números enteros, almacenarlos en un vector y determinar a cuánto es igual el promedio entero de los datos del vector.")

count=1
lista=[]

while count<11:
  numero=int(input('Introduzca su %d numero:' %(count)))
  lista.append(numero)
  count=count+1

suma=0

for numero in lista:
	suma=suma+numero

promedio= suma//10                   
   
print(promedio)

input()

