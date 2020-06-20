print("Leer 10 enteros, almacenarlos en un vector y determinar en qué posición del vector está el mayor número par leído")


count=1
lista=[]
while count<11:                
    num=int(input("Introduzca su %d numero:" %(count)))
    lista.append(num)
    count=count+1
listapar=[]
for x in lista:             
  if x % 2==0:
    listapar.append(x)
pivot=listapar[0]
for element in listapar:            
  if element > pivot:
    pivot= element
print("El mayor numero par leido esta en la posicion %d " %(lista.index(pivot)))
input()