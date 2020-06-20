print("Leer 10 números enteros, almacenarlos en un vector y determinar en qué posiciones se encuentran los números terminados en 4. ")


count=1
lista=[]
while count<11:
  numero=int(input('Introduzca su %d numero:' %(count)))
  lista.append(numero)
  count=count+1
listanueva=[]
s= ','
for element in lista:
  if element % 4 == 0:
    listanueva.append(lista.index(element))
posiciones= ','.join(str (x) for x in listanueva)
print("Los numeros con mas de tres digitos se encuentran en las posiciones",posiciones)
input("presione enter para salir")

