print("Leer 10 números enteros, almacenarlos en un vector y determinar en qué posición está el número con mas dígitos")

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
print("El numero con mas digitos esta en la posicion %d" % (lista.index(pivot)))
input()
