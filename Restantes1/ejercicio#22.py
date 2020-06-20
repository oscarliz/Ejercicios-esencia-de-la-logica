print("Leer 10 números enteros, almacenarlos en un vector y determinar cuáles son los números múltiplos de 5 y en qué posiciones están ")



count=1
lista=[]
while count<11:                
  numero=int(input("Introduzca su %d numero:" %(count)))
  lista.append(numero)
  count=count+1
contador=0
lista2 = []
listanueva=[]
s= ','
for x in lista:
  if x % 5 == 0:

    lista2.append(x) 
                                  
print("los multilplo de 5", lista2)

for element in lista:
  if element % 5 == 0:
    listanueva.append(lista.index(element))
posiciones= ','.join(str (x) for x in listanueva)
print("Los numeros multiplo de 5 se encuentran en las posiciones",posiciones)

input("presiona enter para cerrar")