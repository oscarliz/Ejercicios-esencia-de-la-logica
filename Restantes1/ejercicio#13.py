print("Leer 10 números enteros, almacenarlos en un vector y determinar si el promedio entero de estos datos está almacenado en el vector. ")


count=1
lista=[]

while count<11:
  numero=int(input('Introduzca su %d numero:' %(count)))
  lista.append(numero)
  count=count+1

suma=0
suma2 =0
for numero in lista:
	suma=suma+numero

promedio= suma//10   

              

for x in lista:
	pass
if promedio == x:
	print("el promedio esta")
else:
	print("el promedio no esta.")  



input()