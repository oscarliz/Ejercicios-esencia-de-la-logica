


print("Leer 10 números enteros, almacenarlos en un vector y determinar cuántas veces se repite el promedio entero de los datos dentro del vector. ")


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

              
lista2= []
lista3 = []
contador = 0
for x in lista:
	if promedio == x:
	  contador =  contador +1


		

lista2.append(contador)	
print("Se repite ",lista2[-1], "veces")	

if promedio != x:
  print("el promedio no esta")



input()