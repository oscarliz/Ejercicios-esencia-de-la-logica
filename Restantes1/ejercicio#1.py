print("Leer 10 enteros, almacenarlos en un vector y determinar en qué posición del vector está el mayor número leído")

count=1
lista=[]
while count<11:                
    num=int(input("Introduzca su %d numero:" %(count)))
    lista.append(num)
    count=count+1
pivot=lista[0]
for x in lista:             
   if x > pivot:
   	pivot=x
print("El numero mayor esta en la posicion %d" % (lista.index(pivot)))
input()
